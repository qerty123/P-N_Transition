#!/usr/bin/python3

import os
import random
import sys

from time import time
from PyQt5 import QtWidgets, QtGui, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT
from matplotlib.figure import Figure

import design

tfps = 20
switch_time = time()
log_time = time()
amperage = []
carriers = []
vahx = [0]
vahy = [0]
stime = time()
barrier_capacity = 30

is_secondary = True
is_back = False
is_alternating = False
voltage_source = 0
voltage_barrier = 10
alternating_frequency = 0

spacer = '                                                                                '


class Carrier:
    def __init__(self, is_electron, posx, posy, extra):
        self.is_electron = is_electron
        self.posx = posx
        self.posy = posy
        self.extra = extra


class AmpermetrWidget(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.setScaledContents(True)
        self.pixmap = QtGui.QPixmap(resource_path('amper.png'))
        self.setPixmap(self.pixmap)

    def draw(self):
        self.pixmap = QtGui.QPixmap(resource_path('amper.png'))
        value = 0.1
        for i in range(len(amperage) - 1, len(amperage) - 10, -1):
            value += amperage[i]
        value /= 10
        x = round(400 * (value / 10)) + 40
        y = 100
        # y = round(75 * abs(sin(value * 18))) + 100
        if value > 5:
            y += round(7.5 * (value - 5))
        else:
            y += min(round(75 // value), 75)
        qp = QtGui.QPainter()
        qp.begin(self.pixmap)
        qp.setPen(QtGui.QPen(QtCore.Qt.red, 2, QtCore.Qt.SolidLine))
        qp.drawLine(243, 370, x, y)
        self.setPixmap(self.pixmap)


class SchemaWidget(QtWidgets.QLabel):
    def __init__(self):
        super().__init__()
        self.setScaledContents(True)
        self.pixmap = QtGui.QPixmap(resource_path('diod.png'))
        self.setPixmap(self.pixmap)

    def draw(self):
        self.pixmap = QtGui.QPixmap(resource_path('diod.png'))
        qp = QtGui.QPainter()
        qp.begin(self.pixmap)
        qp.setFont(QtGui.QFont('Decorative', 20))
        # Draw current source
        qp.setPen(QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine))
        if is_back:
            qp.drawLine(800, 350, 800, 450)
            qp.drawLine(750, 375, 750, 425)
            qp.setPen(QtGui.QPen(QtCore.Qt.red, 2, QtCore.Qt.SolidLine))
            qp.drawLine(810, 350, 830, 350)
            qp.drawLine(820, 340, 820, 360)
            qp.drawLine(720, 350, 740, 350)
            if voltage_source > 0:
                qp.drawText(450, 200, '<======   I')
        else:
            qp.drawLine(750, 350, 750, 450)
            qp.drawLine(800, 375, 800, 425)
            qp.setPen(QtGui.QPen(QtCore.Qt.red, 2, QtCore.Qt.SolidLine))
            qp.drawLine(720, 350, 740, 350)
            qp.drawLine(730, 340, 730, 360)
            qp.drawLine(810, 350, 830, 350)
            if voltage_source > 0:
                qp.drawText(450, 200, 'I   ======>')
        # Draw barrier
        qp.setPen(QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine))
        qp.setBrush(QtCore.Qt.green)
        qp.drawRect(500 - barrier_capacity, 50, barrier_capacity * 2, 100)
        # Draw carriers
        for i in carriers:
            if i.is_electron:
                qp.setBrush(QtCore.Qt.blue)
            else:
                qp.setBrush(QtCore.Qt.red)
            qp.drawEllipse(i.posx, i.posy, 15, 15)
        self.setPixmap(self.pixmap)


class PlotWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.navToolbar = NavigationToolbar2QT(self.canvas, self)
        self.mainLayout.addWidget(self.canvas)
        self.mainLayout.addWidget(self.navToolbar)

    def draw(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#DCDCDC')
        # ax.set_xlim([0, 60])
        ax.set_ylim([0, max(amperage) + 2])
        ax.grid()
        ax.plot(amperage, linestyle='-', color='#008000')
        # ax.set(title='Осцилограф', xlable='t, сек', ylable='V, В')
        # ax.set_xlable('t, сек')
        ax.set_title('Оcцилограф')
        self.canvas.draw()


class VAHWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.mainLayout = QtWidgets.QVBoxLayout(self)
        self.figure = Figure()
        self.canvas = FigureCanvasQTAgg(self.figure)
        self.navToolbar = NavigationToolbar2QT(self.canvas, self)
        self.mainLayout.addWidget(self.canvas)
        self.mainLayout.addWidget(self.navToolbar)

    def draw(self):
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.set_facecolor('#DCDCDC')
        if is_back:
            ax.set_ylim([-10, 1])
        else:
            ax.set_ylim([-1, 10])
        ax.grid()
        ax.plot(vahx, vahy, linestyle='-', color='#FF0000')
        ax.set_title('Вольт-амперная характеристика')
        self.canvas.draw()


class VisualApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # Size policy
        self.sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        # Plot widget
        self.PlotWidget = PlotWidget()
        self.PlotWidget.setSizePolicy(self.sizePolicy)
        self.PlotWidget.setMinimumSize(QtCore.QSize(500, 200))
        self.canvas_layout.addWidget(self.PlotWidget)
        self.PlotWidget.draw()
        # Canvas widget
        self.SchemaWidget = SchemaWidget()
        self.SchemaWidget.setSizePolicy(self.sizePolicy)
        self.SchemaWidget.setMinimumSize(QtCore.QSize(500, 200))
        self.canvas_layout.addWidget(self.SchemaWidget)
        self.SchemaWidget.draw()
        # VAH widget
        self.VAHWidget = VAHWidget()
        self.VAHWidget.setSizePolicy(self.sizePolicy)
        self.VAHWidget.setMinimumSize(QtCore.QSize(400, 500))
        self.horizontal_layout.addWidget(self.VAHWidget)
        self.VAHWidget.draw()
        # Ampermetr widget
        self.AmpermetrWidget = AmpermetrWidget()
        self.AmpermetrWidget.setSizePolicy(self.sizePolicy)
        self.AmpermetrWidget.setMinimumSize(QtCore.QSize(300, 300))
        self.AmpermetrWidget.setMaximumSize(QtCore.QSize(400, 300))
        self.menu_layout.addWidget(self.AmpermetrWidget)
        self.AmpermetrWidget.draw()
        # Timer
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.tick)
        self.timer.start(1000 // tfps)
        # Bind changes
        self.voltage_source.valueChanged.connect(self.update_params)
        self.voltage_barrier.valueChanged.connect(self.update_params)
        self.alternating_frequency.valueChanged.connect(self.update_params)
        self.is_back.clicked.connect(self.update_params)
        self.is_alternating.clicked.connect(self.update_params)
        self.is_secondary.clicked.connect(self.update_params)
        # Menu bar
        self.actionExit.triggered.connect(self.close)

        self.is_secondary.setChecked(is_secondary)
        self.update_params()

    def tick(self):
        global barrier_capacity
        global switch_time
        global log_time
        global is_back
        global amperage
        self.PlotWidget.draw()
        self.SchemaWidget.draw()
        self.AmpermetrWidget.draw()
        self.statusbar.showMessage('I = %s А    V = %s В    R = 1 Ом    Vзап = %s В    %s    Время симуляции: %s'
                                   % (voltage_source, voltage_source, voltage_barrier, spacer, round(time() - stime, 1)))
        # Change barrier
        if voltage_source > voltage_barrier and not is_back and barrier_capacity > 0:
            barrier_capacity -= 1
        elif barrier_capacity < 50 and is_back:
            barrier_capacity += 1
        elif barrier_capacity < 25:
            barrier_capacity += 1
        elif barrier_capacity > 25 and not is_back:
            barrier_capacity -= 1
        # Create carriers
        if len(carriers) < 40 and voltage_source > voltage_barrier and (not is_back or is_back and voltage_source > voltage_barrier * 5):
            if random.randint(0, 1) > 0:
                carriers.append(Carrier(True, 750 + random.randint(0, 50), random.randint(50, 130), False))
            else:
                carriers.append(Carrier(False, 200 + random.randint(0, 50), random.randint(50, 130), False))
        if is_secondary and len(carriers) < 40 and random.randint(0, 10) > 9 and voltage_source > voltage_barrier and is_back:
            if random.randint(0, 1) > 0:
                carriers.append(Carrier(False, 750 + random.randint(0, 50), random.randint(50, 130), True))
            else:
                carriers.append(Carrier(True, 200 + random.randint(0, 50), random.randint(50, 130), True))
        # Move carriers
        if not is_back:
            for i in carriers:
                if i.is_electron and voltage_source > voltage_barrier:
                    if i.posx < 220:
                        carriers.remove(i)
                    else:
                        i.posx -= (10 + random.randint(0, 10))
                elif voltage_source > voltage_barrier:
                    if i.posx > 780:
                        carriers.remove(i)
                    else:
                        i.posx += (10 + random.randint(0, 10))
        else:
            for i in carriers:
                if i.extra:
                    if i.is_electron:
                        if i.posx > 780:
                            carriers.remove(i)
                        else:
                            i.posx += (10 + random.randint(0, 10))
                    else:
                        if i.posx < 220:
                            carriers.remove(i)
                        else:
                            i.posx -= (10 + random.randint(0, 10))
                elif voltage_barrier * 5 < voltage_source and is_secondary:
                    if i.is_electron:
                        if i.posx < 220:
                            carriers.remove(i)
                        else:
                            i.posx -= (10 + random.randint(0, 10))
                    else:
                        if i.posx > 780:
                            carriers.remove(i)
                        else:
                            i.posx += (10 + random.randint(0, 10))
                else:
                    if not i.is_electron:
                        if i.posx > 780:
                            carriers.remove(i)
                        elif i.posx > 500:
                            i.posx += (10 + random.randint(0, 10))
                        elif i.posx < 220:
                            carriers.remove(i)
                        elif 500 > i.posx > 300:
                            i.posx -= (10 + random.randint(0, 10))
                    elif i.is_electron:
                        if i.posx < 220:
                            carriers.remove(i)
                        elif i.posx < 500:
                            i.posx -= (10 + random.randint(0, 10))
                        elif i.posx > 780:
                            carriers.remove(i)
                        elif 500 < i.posx < 700:
                            i.posx += (10 + random.randint(0, 10))
        for i in carriers:
            i.posx += random.randint(-5, 5)
        # Change current
        if is_alternating and time() - switch_time > 1 / alternating_frequency:
            switch_time = time()
            is_back = not is_back
        # Set log
        if True:  # time() - log_time >= 1:
            log_time = time()
            amp = 0
            volt = voltage_source - voltage_barrier
            for i in range(0, len(amperage) - 1):
                amperage[i] = amperage[i + 1]
            if voltage_source > voltage_barrier:
                if is_back:
                    if is_secondary:
                        if voltage_source > voltage_barrier * 5:
                            amp = volt + random.uniform(-0.1 * volt, 0.1 * volt)
                        else:
                            amp = 0.1 * (volt + random.uniform(-0.1 * volt, 0.1 * volt))
                else:
                    amp = volt + random.uniform(-0.1 * volt, 0.1 * volt)
            amperage[len(amperage) - 1] = amp

    def update_params(self):
        try:
            if float(self.alternating_frequency.value()) >= 0 and float(self.voltage_barrier.value()) > 0 and float(
                    self.voltage_source.value()) >= 0:
                global is_back
                is_back = self.is_back.isChecked()
                global is_alternating
                is_alternating = self.is_alternating.isChecked()
                global is_secondary
                is_secondary = self.is_secondary.isChecked()
                global voltage_source
                voltage_source = float(self.voltage_source.value())
                global voltage_barrier
                voltage_barrier = float(self.voltage_barrier.value()) / 10
                global alternating_frequency
                alternating_frequency = float(self.alternating_frequency.value()) / 10
                self.error_msg.setText('')
                self.label_source.setText('Напряжение на источнике, В: ' + str(voltage_source))
                self.label_barrier.setText('Запирающее напряжение, В: ' + str(voltage_barrier))
                self.label_alternating.setText('Частота переменного тока, Гц: ' + str(alternating_frequency))
            else:
                self.error_msg.setText('<font color="red">Введены некорректные параметры системы</font>')
        except:
            self.error_msg.setText('<font color="red">Введены некорректные параметры системы</font>')
        finally:
            global vahx
            global vahy
            vahx = []
            vahy = []
            for i in range(0, round(voltage_source) * 10):
                if is_back:
                    vahx.append(i / 10 * -1)
                    if is_secondary:
                        if i / 10 < voltage_barrier * 5:
                            vahy.append(i / 100 * -1)
                        else:
                            vahy.append(i / 10 * -1)
                    else:
                        vahy.append(0)
                else:
                    vahx.append(i / 10)
                    if i / 10 < voltage_barrier:
                        vahy.append(0)
                    else:
                        vahy.append(i / 10)
            self.VAHWidget.draw()


def main():
    for i in range(20 * tfps):
        amperage.append(0)
    app = QtWidgets.QApplication(sys.argv)
    window = VisualApp()
    window.show()
    app.exec()


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


if __name__ == '__main__':
    main()
