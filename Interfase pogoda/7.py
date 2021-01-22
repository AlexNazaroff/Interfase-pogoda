
#if __name__ == "__main__":
import sys, pyowm

from PyQt5 import QtCore, QtGui, QtWidgets
from test2 import Ui_Dialog
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
#mgr

def get_weather_city():
    owm=pyom.OWM("62c2980e8419f3fad2f1c8f805589918")

    city=ui.lineEdit.text()
    observation = mgr.weather_at_place( London )
    w = observation.get_weather
    temperature=w.get_temperature('celsius')['temp']
    ui.label.setText(f'Температура: {temperature}')

ui.pushButton.clicked.connect (get_weather_city)
sys.exit(app.exec_())
