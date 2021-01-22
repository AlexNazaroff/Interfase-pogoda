pyside2-uic "C:\2\Pogoda.ui"  -o "C:\2\test.py"

-x
pyuic5 -x "C:\2\Pogoda.ui" -o "C:\2\test2.py"


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
