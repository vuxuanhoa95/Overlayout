# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpacerItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_ResizeTL = QLabel(self.centralwidget)
        self.label_ResizeTL.setObjectName(u"label_ResizeTL")
        self.label_ResizeTL.setMaximumSize(QSize(20, 20))
        self.label_ResizeTL.setPixmap(QPixmap(u":/icons/img/icons8-enlarge-32.png"))
        self.label_ResizeTL.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_ResizeTL)

        self.label_Move = QLabel(self.centralwidget)
        self.label_Move.setObjectName(u"label_Move")
        self.label_Move.setMaximumSize(QSize(20, 20))
        self.label_Move.setFrameShape(QFrame.NoFrame)
        self.label_Move.setPixmap(QPixmap(u":/icons/img/icons8-drag-32.png"))
        self.label_Move.setScaledContents(True)
        self.label_Move.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_Move)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setSizeConstraint(QLayout.SetMinimumSize)
        self.btn_Add = QPushButton(self.centralwidget)
        self.btn_Add.setObjectName(u"btn_Add")
        self.btn_Add.setMaximumSize(QSize(20, 20))
        icon = QIcon()
        icon.addFile(u":/icons/img/icons8-plus-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Add.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_Add)

        self.btn_Exit = QPushButton(self.centralwidget)
        self.btn_Exit.setObjectName(u"btn_Exit")
        self.btn_Exit.setMaximumSize(QSize(20, 20))
        icon1 = QIcon()
        icon1.addFile(u":/icons/img/icons8-close-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_Exit.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_Exit)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(1, 1))
        self.label.setStyleSheet(u"background: transparent;\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border-style: dashed;\n"
"padding: 0px;")
        self.label.setScaledContents(True)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.layout_BR = QHBoxLayout()
        self.layout_BR.setObjectName(u"layout_BR")
        self.label_ResizeBR = QLabel(self.centralwidget)
        self.label_ResizeBR.setObjectName(u"label_ResizeBR")
        self.label_ResizeBR.setMaximumSize(QSize(20, 20))
        self.label_ResizeBR.setFrameShape(QFrame.NoFrame)
        self.label_ResizeBR.setPixmap(QPixmap(u":/icons/img/icons8-enlarge-32.png"))
        self.label_ResizeBR.setScaledContents(True)

        self.layout_BR.addWidget(self.label_ResizeBR)


        self.horizontalLayout_7.addLayout(self.layout_BR)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.widget_Settings = QWidget(self.centralwidget)
        self.widget_Settings.setObjectName(u"widget_Settings")
        self.widget_Settings.setMaximumSize(QSize(16777215, 20))
        self.layout_Settings = QHBoxLayout(self.widget_Settings)
        self.layout_Settings.setSpacing(1)
        self.layout_Settings.setObjectName(u"layout_Settings")
        self.layout_Settings.setSizeConstraint(QLayout.SetMaximumSize)
        self.layout_Settings.setContentsMargins(0, 0, 0, 0)
        self.btn_SwitchWidth = QPushButton(self.widget_Settings)
        self.btn_SwitchWidth.setObjectName(u"btn_SwitchWidth")
        self.btn_SwitchWidth.setMaximumSize(QSize(20, 20))
        self.btn_SwitchWidth.setContextMenuPolicy(Qt.CustomContextMenu)

        self.layout_Settings.addWidget(self.btn_SwitchWidth)

        self.btn_SwitchImage = QPushButton(self.widget_Settings)
        self.btn_SwitchImage.setObjectName(u"btn_SwitchImage")
        self.btn_SwitchImage.setMaximumSize(QSize(20, 20))
        self.btn_SwitchImage.setContextMenuPolicy(Qt.CustomContextMenu)

        self.layout_Settings.addWidget(self.btn_SwitchImage)

        self.slider_Opacity = QSlider(self.widget_Settings)
        self.slider_Opacity.setObjectName(u"slider_Opacity")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.slider_Opacity.sizePolicy().hasHeightForWidth())
        self.slider_Opacity.setSizePolicy(sizePolicy1)
        self.slider_Opacity.setMaximumSize(QSize(50, 20))
        self.slider_Opacity.setContextMenuPolicy(Qt.CustomContextMenu)
        self.slider_Opacity.setValue(50)
        self.slider_Opacity.setOrientation(Qt.Horizontal)

        self.layout_Settings.addWidget(self.slider_Opacity)


        self.horizontalLayout_2.addWidget(self.widget_Settings)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_Exit, self.btn_Add)
        QWidget.setTabOrder(self.btn_Add, self.btn_SwitchWidth)
        QWidget.setTabOrder(self.btn_SwitchWidth, self.btn_SwitchImage)
        QWidget.setTabOrder(self.btn_SwitchImage, self.slider_Opacity)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_ResizeTL.setText("")
        self.label_Move.setText("")
        self.btn_Add.setText("")
        self.btn_Exit.setText("")
        self.label.setText("")
        self.label_ResizeBR.setText("")
        self.btn_SwitchWidth.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.btn_SwitchImage.setText(QCoreApplication.translate("MainWindow", u"C", None))
    # retranslateUi

