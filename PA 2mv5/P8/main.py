from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QKeyEvent
from PySide6 import QtWidgets
from calculadora_ui import Ui_MainWindow
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
        self.btn0.clicked.connect(self.numero)
        self.btn1.clicked.connect(self.numero)
        self.btn2.clicked.connect(self.numero)
        self.btn3.clicked.connect(self.numero)
        self.btn4.clicked.connect(self.numero)
        self.btn5.clicked.connect(self.numero)
        self.btn6.clicked.connect(self.numero)
        self.btn7.clicked.connect(self.numero)
        self.btn8.clicked.connect(self.numero)
        self.btn9.clicked.connect(self.numero)
        self.btnac.clicked.connect(self.borra_todo)
        self.btnborraruno.clicked.connect(self.borra_uno)

    def borra_uno(self):
        original = self.pantalla.text()
        if len(original) == 1:
            original = '0'
        else:
            original = original[0:len(original) - 1]
        
        self.pantalla.setText(original)
        
    def borra_todo(self):
        self.pantalla.setText("0")
        
    def numero(self):
        self.actualiza_pantalla(self.sender().text())
        
    def actualiza_pantalla(self, text: str):
        original = self.pantalla.text()
        if original == "0" :
            original = text
        else:
            original += text
        self.pantalla.setText(original)
        
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() >= 48 and event.key() <= 57:
            self.actualiza_pantalla(str(event.key() - 48))
        return super().keyPressEvent(event)
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
