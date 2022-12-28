import os
import sys
from functools import partial

from PySide2.QtCore import QPointF, QEvent, Qt, QSize
from PySide2.QtGui import QPixmap, QPainter, QColor, QPen, QResizeEvent
from PySide2.QtWidgets import QMainWindow, QSizeGrip, QApplication, QMenu, QAction

import main_ui
import Container


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


RESOURCE = resource_path('img') + '\\'
IMAGE_POOL = ['rule3_white.png', 'rule3_black.png']
COLOR_POOL = [Qt.white, Qt.black, Qt.red, Qt.green, Qt.blue, Qt.cyan, Qt.magenta, Qt.yellow, Qt.gray]
WIDTH_POOL = [2, 4, 6, 8, 10]
ALPHA_POOL = [0, 25, 50, 75, 100]


def show_window(x=None, y=None):
    w = Window()
    if x is not None and y is not None:
        w.setGeometry(x+50, y+50, 800, 600)
    w.show()
    w.draw_pixmap()


def draw_rule_thirds(rect_size: QSize, width: int = 2, color: QColor = Qt.white, alpha: int = 128):
    h = rect_size.height()
    w = rect_size.width()

    pixmap = QPixmap(rect_size)
    pixmap.fill(Qt.transparent)

    painter = QPainter(pixmap)
    color.setAlpha(alpha)

    pen = QPen(color, width)
    pen.setStyle(Qt.DotLine)
    painter.setPen(pen)
    painter.drawLine(0, h / 3, w, h / 3)
    painter.drawLine(0, 2 * h / 3, w, 2 * h / 3)
    painter.drawLine(w / 3, 0, w / 3, h)
    painter.drawLine(2 * w / 3, 0, 2 * w / 3, h)

    pen = QPen(color, 2 * width)
    painter.setPen(pen)
    painter.drawLine(0, 0, 25, 0)
    painter.drawLine(0, 0, 0, 25)
    painter.drawLine(w, 0, w - 25, 0)
    painter.drawLine(w, 0, w, 25)
    painter.drawLine(0, h, 25, h)
    painter.drawLine(0, h, 0, h - 25)
    painter.drawLine(w, h, w - 25, h)
    painter.drawLine(w, h, w, h - 25)

    painter.end()
    return pixmap


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
        self.draw_pixmap()

        container = Container.SectionExpandButton(self.ui.widget_Settings, expanded_size=QSize(0, 23))
        self.ui.layout_BR.insertWidget(0, container)
        container.collapse()

    def connect_event(self):
        self.ui.btn_Exit.clicked.connect(self.close)
        self.ui.btn_SwitchImage.clicked.connect(lambda: self.switch_color_style())
        self.ui.btn_SwitchWidth.clicked.connect(lambda: self.switch_width())
        self.ui.btn_Add.clicked.connect(lambda: show_window(self.x(), self.y()))

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
        self.draw_pixmap()

    def eventFilter(self, source, event):
        if source == self.ui.label_Move and event.type() == QEvent.MouseMove:
            if event.buttons() == Qt.LeftButton:
                delta = event.globalPosition() - self.clickPosition
                delta = delta.toPoint()
                self.move(self.x() + delta.x(), self.y() + delta.y())

                self.clickPosition = event.globalPosition()

        return super().eventFilter(source, event)

    def menu_color_request(self, pos):
        self.menu_color.exec(self.ui.btn_SwitchImage.mapToGlobal(pos))

    def menu_width_request(self, pos):
        self.menu_width.exec(self.ui.btn_SwitchWidth.mapToGlobal(pos))

    def menu_opacity_request(self, pos):
        self.menu_alpha.exec(self.ui.slider_Opacity.mapToGlobal(pos))

    def draw_pixmap(self):
        new_pix = draw_rule_thirds(self.ui.label.size(),
                                   width=self.current_width,
                                   color=self.current_color,
                                   alpha=self.current_alpha)

        self.ui.label.setPixmap(new_pix)

    def change_opacity(self, value):
        self.current_alpha = value * 0.01 * 255
        self.draw_pixmap()

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

        if redraw:
            self.draw_pixmap()

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
            self.draw_pixmap()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication([])
    with open(RESOURCE + "style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
    show_window()
    sys.exit(app.exec_())
