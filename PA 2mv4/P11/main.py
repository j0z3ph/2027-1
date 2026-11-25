from PySide6.QtWidgets import QMainWindow 
from PySide6 import QtWidgets
from PySide6.QtGui import QKeyEvent
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
        
        self.btnborraruno.clicked.connect(self.borra_uno)
        self.btnborratodo.clicked.connect(self.borra_todo)
        
    def borra_todo(self):
        self.pantalla.setText("0")
        
    def borra_uno(self):
        valor = self.pantalla.text()
        
        if len(valor) == 1:
            valor = "0"
        else:
            valor = valor[0:len(valor)-1]
        self.pantalla.setText(valor)
        
    def numero(self):
        self.actualiza_pantalla(self.sender().text())
        
    def actualiza_pantalla(self, texto:str):
        valor = self.pantalla.text()
        if valor == "0":
            valor = texto
        else:
            valor += texto
        self.pantalla.setText(valor)
        
        
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() >= 48 and event.key() <= 57:
            self.actualiza_pantalla(str(event.key() - 48))
        elif event.key() == 16777219:
            self.borra_uno()
        elif event.key() == 16777216:
            self.borra_todo()
        return super().keyPressEvent(event)
        
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
