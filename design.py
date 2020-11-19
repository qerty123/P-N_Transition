# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(921, 705)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.menu_layout = QtWidgets.QVBoxLayout()
        self.menu_layout.setObjectName("menu_layout")
        self.label_source = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_source.sizePolicy().hasHeightForWidth())
        self.label_source.setSizePolicy(sizePolicy)
        self.label_source.setMaximumSize(QtCore.QSize(400, 16777215))
        self.label_source.setObjectName("label_source")
        self.menu_layout.addWidget(self.label_source)
        self.voltage_source = QtWidgets.QSlider(self.centralwidget)
        self.voltage_source.setMaximumSize(QtCore.QSize(400, 16777215))
        self.voltage_source.setMaximum(10)
        self.voltage_source.setOrientation(QtCore.Qt.Horizontal)
        self.voltage_source.setObjectName("voltage_source")
        self.menu_layout.addWidget(self.voltage_source)
        self.label_barrier = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_barrier.sizePolicy().hasHeightForWidth())
        self.label_barrier.setSizePolicy(sizePolicy)
        self.label_barrier.setMaximumSize(QtCore.QSize(400, 16777215))
        self.label_barrier.setObjectName("label_barrier")
        self.menu_layout.addWidget(self.label_barrier)
        self.voltage_barrier = QtWidgets.QSlider(self.centralwidget)
        self.voltage_barrier.setMaximumSize(QtCore.QSize(400, 16777215))
        self.voltage_barrier.setMinimum(1)
        self.voltage_barrier.setMaximum(100)
        self.voltage_barrier.setProperty("value", 10)
        self.voltage_barrier.setOrientation(QtCore.Qt.Horizontal)
        self.voltage_barrier.setObjectName("voltage_barrier")
        self.menu_layout.addWidget(self.voltage_barrier)
        self.is_alternating = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.is_alternating.sizePolicy().hasHeightForWidth())
        self.is_alternating.setSizePolicy(sizePolicy)
        self.is_alternating.setMaximumSize(QtCore.QSize(400, 16777215))
        self.is_alternating.setObjectName("is_alternating")
        self.menu_layout.addWidget(self.is_alternating)
        self.label_alternating = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_alternating.sizePolicy().hasHeightForWidth())
        self.label_alternating.setSizePolicy(sizePolicy)
        self.label_alternating.setMaximumSize(QtCore.QSize(400, 16777215))
        self.label_alternating.setObjectName("label_alternating")
        self.menu_layout.addWidget(self.label_alternating)
        self.alternating_frequency = QtWidgets.QSlider(self.centralwidget)
        self.alternating_frequency.setMaximumSize(QtCore.QSize(400, 16777215))
        self.alternating_frequency.setMinimum(1)
        self.alternating_frequency.setMaximum(30)
        self.alternating_frequency.setProperty("value", 10)
        self.alternating_frequency.setOrientation(QtCore.Qt.Horizontal)
        self.alternating_frequency.setObjectName("alternating_frequency")
        self.menu_layout.addWidget(self.alternating_frequency)
        self.is_back = QtWidgets.QCheckBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.is_back.sizePolicy().hasHeightForWidth())
        self.is_back.setSizePolicy(sizePolicy)
        self.is_back.setMaximumSize(QtCore.QSize(400, 16777215))
        self.is_back.setObjectName("is_back")
        self.menu_layout.addWidget(self.is_back)
        self.error_msg = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_msg.sizePolicy().hasHeightForWidth())
        self.error_msg.setSizePolicy(sizePolicy)
        self.error_msg.setMaximumSize(QtCore.QSize(400, 16777215))
        font = QtGui.QFont()
        font.setItalic(True)
        self.error_msg.setFont(font)
        self.error_msg.setText("")
        self.error_msg.setAlignment(QtCore.Qt.AlignCenter)
        self.error_msg.setObjectName("error_msg")
        self.menu_layout.addWidget(self.error_msg)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.menu_layout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.menu_layout)
        self.canvas_layout = QtWidgets.QVBoxLayout()
        self.canvas_layout.setObjectName("canvas_layout")
        self.horizontalLayout.addLayout(self.canvas_layout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 921, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Визуализация P-N перехода"))
        self.label_source.setText(_translate("MainWindow", "Напряжение на источнике, В:"))
        self.label_barrier.setText(_translate("MainWindow", "Запирающее напряжение, В:"))
        self.is_alternating.setText(_translate("MainWindow", "Переменный ток"))
        self.label_alternating.setText(_translate("MainWindow", "Частота переменного тока, Гц:"))
        self.is_back.setText(_translate("MainWindow", "Обратное направление тока"))