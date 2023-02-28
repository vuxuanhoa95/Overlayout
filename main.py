import os
import sys
from functools import partial

from PySide6.QtCore import QPointF, QEvent, Qt, QSize
from PySide6.QtGui import QPainter, QColor, QPen, QResizeEvent, QAction
from PySide6.QtWidgets import QMainWindow, QSizeGrip, QApplication, QMenu

import main_ui
import Container
import Drawing


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


RESOURCE = resource_path('img') + '\\'
IMAGE_POOL = ['rule3_white.png', 'rule3_black.png']
COLOR_POOL = [Qt.white, Qt.black, Qt.red, Qt.green, Qt.blue, Qt.cyan, Qt.magenta, Qt.yellow, Qt.gray]
WIDTH_POOL = [2, 4, 6, 8, 10]
ALPHA_POOL = [0, 25, 50, 75, 100]


def show_window(x=None, y=None, width=640, height=360):
    w = Window()

    if None not in (x, y):
        w.setGeometry(x + 50, y + 50, width, height)

    w.show()
    w.resize(width, height)
    w.repaint()


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = main_ui.Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setWindowOpacity(0.7)

        self.clickPosition = QPointF()
        self.current_width_index = -1
        self.current_width = None
        self.current_color_index = -1
        self.current_color = None
        self.current_alpha = 128
        self.rules = Drawing.RuleOfThirds(self.ui.label.geometry())

        self.connect_event()

        self.menu_color = QMenu(self)
        for color in COLOR_POOL:
            a = QAction(str(color).split('.')[-1], self)
            a.triggered.connect(partial(self.switch_color_style, color=color))
            self.menu_color.addAction(a)

        self.menu_width = QMenu(self)
        for width in WIDTH_POOL:
            a = QAction(f'{width} px', self)
            a.triggered.connect(partial(self.switch_width, width=width))
            self.menu_width.addAction(a)

        self.menu_alpha = QMenu(self)
        for alpha in ALPHA_POOL:
            a = QAction(f'{alpha} %', self)
            a.triggered.connect(partial(self.change_opacity, value=alpha))
            self.menu_alpha.addAction(a)

        self.switch_color_style(False)
        self.switch_width(False)

        container = Container.SectionExpandButton(self.ui.widget_Settings, expanded_size=QSize(0, 23))
        self.ui.layout_BR.insertWidget(0, container)
        container.collapse()

    def connect_event(self):
        self.ui.btn_Exit.clicked.connect(self.close)
        self.ui.btn_SwitchImage.clicked.connect(lambda: self.switch_color_style())
        self.ui.btn_SwitchWidth.clicked.connect(lambda: self.switch_width())
        self.ui.btn_Add.clicked.connect(lambda: show_window(self.x(), self.y(), self.width(), self.height()))

        self.ui.btn_SwitchImage.customContextMenuRequested.connect(self.menu_color_request)
        self.ui.btn_SwitchWidth.customContextMenuRequested.connect(self.menu_width_request)

        self.ui.label_Move.installEventFilter(self)

        self.ui.slider_Opacity.valueChanged.connect(self.change_opacity)
        self.ui.slider_Opacity.customContextMenuRequested.connect(self.menu_opacity_request)
        QSizeGrip(self.ui.label_ResizeBR)
        QSizeGrip(self.ui.label_ResizeTL)

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPosition()

    def resizeEvent(self, event: QResizeEvent) -> None:
        self.rules.draw(self.ui.label.geometry())
        self.update()

    def eventFilter(self, source, event):
        if source == self.ui.label_Move and event.type() == QEvent.MouseMove:
            if event.buttons() == Qt.LeftButton:
                delta = event.globalPosition() - self.clickPosition
                delta = delta.toPoint()
                self.move(self.x() + delta.x(), self.y() + delta.y())

                self.clickPosition = event.globalPosition()

        return super().eventFilter(source, event)

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(self.current_color, self.current_width)
        pen.setStyle(Qt.DotLine)

        painter.setPen(pen)
        painter.drawPath(self.rules.path)
        painter.end()

        super().paintEvent(event)

    def menu_color_request(self, pos):
        self.menu_color.exec(self.ui.btn_SwitchImage.mapToGlobal(pos))

    def menu_width_request(self, pos):
        self.menu_width.exec(self.ui.btn_SwitchWidth.mapToGlobal(pos))

    def menu_opacity_request(self, pos):
        self.menu_alpha.exec(self.ui.slider_Opacity.mapToGlobal(pos))

    def change_opacity(self, value):
        self.current_alpha = value * 0.01 * 255
        self.current_color.setAlpha(self.current_alpha)
        self.update()

    def switch_color_style(self, redraw=True, color: QColor = None):
        if color is None:
            self.current_color_index += 1
            if self.current_color_index >= len(COLOR_POOL):
                self.current_color_index = 0

            self.current_color = QColor(COLOR_POOL[self.current_color_index])

        else:
            self.current_color = QColor(color)
            if color in COLOR_POOL:
                self.current_color_index = COLOR_POOL.index(color)

        self.current_color.setAlpha(self.current_alpha)
        if redraw:
            self.update()

    def switch_width(self, redraw=True, width: int = None):
        if width is None:
            self.current_width_index += 1
            if self.current_width_index >= len(WIDTH_POOL):
                self.current_width_index = 0

            self.current_width = WIDTH_POOL[self.current_width_index]
        else:
            self.current_width = width
            if width in WIDTH_POOL:
                self.current_width_index = WIDTH_POOL.index(width)

        if redraw:
            self.update()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication([])

    with open(RESOURCE + "style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    show_window()

    sys.exit(app.exec())
