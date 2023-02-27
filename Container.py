from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import QSize

import resource_rc


class SectionExpandButton(QtWidgets.QPushButton):
    """a QPushbutton that can expand or collapse its section
    """
    def __init__(self, widget, text="", parent=None, expanded_size=None):
        super().__init__(text, parent)
        self.section = widget
        self.setMaximumSize(QSize(20, 20))

        self.expanded_size = expanded_size

        self.expand_ico = QtGui.QPixmap(":/icons/img/icons8-expand-arrow-32.png")
        self.collapse_ico = QtGui.QPixmap(":/icons/img/icons8-collapse-arrow-32.png")
        self.clicked.connect(self.on_clicked)
        # self.collapse()

    def on_clicked(self):
        """toggle expand/collapse of section by clicking"""
        self.expand() if not self.section.isVisible() else self.collapse()

    def get_expanded_size(self):
        pass

    def maintain_size(self, expand=True):
        if self.expanded_size is not None:
            window = self.window()
            if expand:
                window.resize(window.size() + self.expanded_size)
            else:
                window.resize(window.size() - self.expanded_size)

    def expand(self):
        self.section.setVisible(True)
        self.section.setMaximumSize(1000, 20)
        self.setIcon(self.collapse_ico)
        self.maintain_size(expand=True)

    def collapse(self):
        self.section.setVisible(False)
        self.section.setMaximumSize(0, 20)
        self.setIcon(self.expand_ico)
        self.maintain_size(expand=False)
