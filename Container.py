from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import QSize

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


class Container(QtWidgets.QWidget):
    """Class for creating a collapsible group similar to how it is implement in Maya

        Examples:
            Simple example of how to add a Container to a QVBoxLayout and attach a QGridLayout

            >>> layout = QtWidgets.QVBoxLayout()
            >>> container = Container("Group")
            >>> layout.addWidget(container)
            >>> content_layout = QtWidgets.QGridLayout(container.contentWidget)
            >>> content_layout.addWidget(QtWidgets.QPushButton("Button"))
    """
    def __init__(self, name, color_background=False):
        """Container Class Constructor to initialize the object

        Args:
            name (str): Name for the header
            color_background (bool): whether or not to color the background lighter like in maya
        """
        super(Container, self).__init__()
        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        self._content_widget = QtWidgets.QWidget()
        if color_background:
            self._content_widget.setStyleSheet(".QWidget{background-color: rgb(73, 73, 73); "
                                               "margin-left: 2px; margin-right: 2px}")
        header = Header(name, self._content_widget)
        layout.addWidget(self._content_widget)
        layout.addWidget(header)

        # assign header methods to instance attributes so they can be called outside of this class
        self.collapse = header.collapse
        self.expand = header.expand
        self.toggle = header.mousePressEvent

    @property
    def contentWidget(self):
        """Getter for the content widget

        Returns: Content widget
        """
        return self._content_widget