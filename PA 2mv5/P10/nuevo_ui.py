# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nuevo.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QDoubleSpinBox, QLabel, QLineEdit,
    QSizePolicy, QSpinBox, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(397, 243)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 190, 341, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 58, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 50, 58, 16))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 80, 58, 16))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 110, 58, 16))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 150, 58, 16))
        self.nombre = QLineEdit(Dialog)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setGeometry(QRect(100, 20, 271, 21))
        self.marca = QLineEdit(Dialog)
        self.marca.setObjectName(u"marca")
        self.marca.setGeometry(QRect(100, 50, 271, 21))
        self.precio = QDoubleSpinBox(Dialog)
        self.precio.setObjectName(u"precio")
        self.precio.setGeometry(QRect(100, 80, 121, 22))
        self.cantidad = QSpinBox(Dialog)
        self.cantidad.setObjectName(u"cantidad")
        self.cantidad.setGeometry(QRect(100, 110, 121, 22))
        self.tipo = QComboBox(Dialog)
        self.tipo.setObjectName(u"tipo")
        self.tipo.setGeometry(QRect(100, 140, 221, 32))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Nuevo Producto", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Marca", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Precio", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Cantidad", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Tipo", None))
    # retranslateUi

