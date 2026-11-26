from PySide6.QtWidgets import QMainWindow, QMessageBox, QDialog, QTableWidgetItem
from PySide6 import QtWidgets
from ventana_ui import Ui_MainWindow
from nuevo_ui import Ui_Dialog
import sys

class Producto:
    def __init__(self, nombre, marca, cantidad, precio, tipo):
        self.__nombre = nombre
        self.__marca = marca
        self.__tipo = tipo
        self.__cantidad = cantidad
        self.__precio = precio
    
    @property
    def nombre(self):
        return self.__nombre
    @property
    def marca(self):
        return self.__marca
    @property
    def tipo(self):
        return self.__tipo
    @property
    def precio(self):
        return self.__precio
    @property
    def cantidad(self):
        return self.__cantidad
        

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        
        self.__lista = []
        
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(["Nombre", "Marca", "Precio Unitario", "Cantidad", "Tipo"])
        
        self.actionSalir.triggered.connect(self.close)
        self.actionAcerca_de.triggered.connect(self.muestra_ayuda)
        self.actionNuevo.triggered.connect(self.nuevo_producto)
    
    def muestra_lista(self):
        self.tabla.clearContents()
        self.tabla.setRowCount(len(self.__lista))
        row = 0
        for producto in self.__lista:
            self.tabla.setItem(row, 0, QTableWidgetItem(producto.nombre))
            self.tabla.setItem(row, 1, QTableWidgetItem(producto.marca))
            self.tabla.setItem(row, 2, QTableWidgetItem(str(producto.precio)))
            self.tabla.setItem(row, 3, QTableWidgetItem(str(producto.cantidad)))
            self.tabla.setItem(row, 4, QTableWidgetItem(producto.tipo))
            row += 1
                        
    def nuevo_producto(self):
        dialogo = NuevoProductoDialog(self)
        if dialogo.exec() == 1:
            # Agrego el nuevo producto
            nombre = dialogo.nombre.text()
            marca = dialogo.marca.text()
            cantidad = dialogo.cantidad.value()
            precio = dialogo.precio.value()
            tipo = dialogo.tipo.currentText()
            producto = Producto(nombre, marca, cantidad, precio, tipo)
            self.__lista.append(producto)
            
            self.muestra_lista()
    
    
    def muestra_ayuda(self):
        QMessageBox.information(self, "Acerca de", "Creado por MI XD")
        
class NuevoProductoDialog(QDialog, Ui_Dialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        
        self.tipo.addItems(["Lacteos", "Frutas", "Verduras", "Bebidas Sin Alcohol", "Bebidad Con Alcohol", "Congelados", "Carnes", "Pastas", "Free Tangas"])

    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
