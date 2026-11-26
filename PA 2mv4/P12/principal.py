from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QDialog
from PySide6 import QtWidgets
from ventana_ui import Ui_MainWindow
from nuevo_ui import Ui_Dialog
import sys

class Usuario:
    def __init__(self, id, nombre, tipo):
        self.__id = id
        self.__nombre = nombre
        self.__tipo = tipo
    
    @property
    def id(self):
        return self.__id
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def tipo(self):
        return self.__tipo

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.__lista = []
        
        self.actionSalir.triggered.connect(self.close)
        self.actionAcerca_de.triggered.connect(self.muestra_ayuda)
        self.actionNuevo.triggered.connect(self.muestra_dialogo_nuevo_usuario)
        
        self.tabla.setColumnCount(3)
        self.tabla.setHorizontalHeaderLabels(["ID", "Usuario", "Tipo"])
     
    def muestra_dialogo_nuevo_usuario(self):
        dialogo = DialogoNuevoUsuario(self)
        if dialogo.exec() == 1:
            nombre = dialogo.txtusuario.text()
            id = dialogo.txtid.text()
            tipo = dialogo.combotipo.currentText()
            usuario = Usuario(id, nombre, tipo)
            self.__lista.append(usuario)
            self.actualiza_tabla()
            
    def actualiza_tabla(self):
        self.tabla.clearContents()
        self.tabla.setRowCount(len(self.__lista))
        row = 0
        for usuario in self.__lista:
            self.tabla.setItem(row, 0, QTableWidgetItem(usuario.id))
            self.tabla.setItem(row, 1, QTableWidgetItem(usuario.nombre))
            self.tabla.setItem(row, 2, QTableWidgetItem(usuario.tipo))
            row += 1
        
    def muestra_ayuda(self):
        QMessageBox.information(self, "Acerca de", "Creador por YO XD")

class DialogoNuevoUsuario(QDialog, Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.combotipo.addItems(["Admin", "General", "Invitado"])

    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
