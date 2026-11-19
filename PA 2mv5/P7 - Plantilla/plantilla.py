from PySide6.QtWidgets import QMainWindow 
from PySide6 import QtWidgets
from mi_ventana_ui import Ui_MainWindow
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.saluda)
        
    def saluda(self):
        print("Holi Canoli XD")
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
