from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6 import QtWidgets
from ventana_ui import Ui_MainWindow
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
        self.boton.clicked.connect(self.cliqueado)
    
    def cliqueado(self):
        #print("Te dije que no tocaras 🤬")
        QMessageBox.information(self, "😡", "Te dije que no tocaras 🤬")
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
