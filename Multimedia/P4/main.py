from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtGui import QPixmap, QImage
from PySide6 import QtWidgets
from ventana_ui import Ui_MainWindow
import cv2 as cv
import numpy as np
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.actionAbrir.triggered.connect(self.abrir)
        self.horizontalSlider.valueChanged.connect(self.cambia_brisho)
        
    def cambia_brisho(self):
        valor = np.array([self.horizontalSlider.value()])
        img_tmp = np.clip(self.img + valor,0,255).astype('uint8')
        self.etiqueta.setPixmap(self.convert_cv_qt(img_tmp))
        
    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv.cvtColor(cv_img, cv.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        converted_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format.Format_RGB888)
        return QPixmap.fromImage(converted_image)
    
    def abrir(self):
        archi = QFileDialog(self)
        
        file, _ = archi.getOpenFileName(self, "Selecciona una imagen", "", "Imagenes *.jpg *.png *.bmp *.jpeg")
        
        if file:
            imagen = QPixmap(file)
            self.etiqueta.setPixmap(imagen)
            self.img = cv.imread(file)
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
