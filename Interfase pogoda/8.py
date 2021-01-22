
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
	owm=pyowm.OWM('62c2980e8419f3fad2f1c8f805589918')

	city=ui.lineEdit.text()
	mgr = owm.weather_manager()
	observation	= mgr.weather_at_place( city )
	#w = observation.get_weather()
	w = observation.weather
	temperature = w.temperature( 'celsius' )[ 'temp' ]
	ui.label.setText(f'Температура: {temperature}')

ui.pushButton.clicked.connect (get_weather_city)
sys.exit(app.exec_())
