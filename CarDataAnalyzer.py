import obd
from PyQt5 import QtCore, QtGui, QtWidgets
# from qwt_plot import QwtPlot

usb_ports = obd.scan_serial()

connection = obd.OBD(
    usb_ports[0],
    baudrate=9600,
    fast=False,
    timeout=None,
)

speed_response = connection.query(obd.commands.SPEED)
rpm_response = connection.query(obd.commands.RPM)
fuel_response = connection.query(obd.commands.FUEL_LEVEL)


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 500)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        '''
        self.hp_graph = QwtPlot(self.centralwidget)
        self.hp_graph.setGeometry(QtCore.QRect(0, 0, 500, 200))
        self.hp_graph.setFrameShape(QtWidgets.QFrame.Box)
        self.hp_graph.setObjectName("hp_graph")
        '''

        self.speed_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.speed_lcd.setGeometry(QtCore.QRect(125, 240, 64, 23))
        self.speed_lcd.setObjectName("speed_lcd")

        self.rpm_lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.rpm_lcd.setGeometry(QtCore.QRect(375, 240, 64, 23))
        self.rpm_lcd.setObjectName("rpm_lcd")

        self.speed_label = QtWidgets.QLabel(self.centralwidget)
        self.speed_label.setGeometry(QtCore.QRect(125, 210, 67, 17))
        self.speed_label.setFrameShape(QtWidgets.QFrame.Box)
        self.speed_label.setAlignment(QtCore.Qt.AlignCenter)
        self.speed_label.setObjectName("speed_label")

        self.rpm_label = QtWidgets.QLabel(self.centralwidget)
        self.rpm_label.setGeometry(QtCore.QRect(375, 210, 67, 17))
        self.rpm_label.setFrameShape(QtWidgets.QFrame.Box)
        self.rpm_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rpm_label.setObjectName("rpm_label")

        self.fuel_progress_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.fuel_progress_bar.setGeometry(QtCore.QRect(20, 370, 100, 25))
        self.fuel_progress_bar.setProperty("value", fuel_response)
        self.fuel_progress_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.fuel_progress_bar.setObjectName("fuel_progress_bar")

        self.fuel_label = QtWidgets.QLabel(self.centralwidget)
        self.fuel_label.setGeometry(QtCore.QRect(20, 340, 100, 25))
        self.fuel_label.setAlignment(QtCore.Qt.AlignCenter)
        self.fuel_label.setObjectName("fuel_label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.speed_label.setText(_translate("MainWindow", "Speed"))
        self.rpm_label.setText(_translate("MainWindow", "RPM"))
        self.fuel_label.setText(_translate("MainWindow", "Fuel Level"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

