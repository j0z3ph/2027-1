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
    QDialogButtonBox, QLabel, QLineEdit, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(391, 173)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 120, 341, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 10, 58, 16))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 40, 141, 16))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 80, 58, 16))
        self.txtid = QLineEdit(Dialog)
        self.txtid.setObjectName(u"txtid")
        self.txtid.setGeometry(QRect(140, 10, 201, 21))
        self.txtusuario = QLineEdit(Dialog)
        self.txtusuario.setObjectName(u"txtusuario")
        self.txtusuario.setGeometry(QRect(140, 40, 201, 21))
        self.combotipo = QComboBox(Dialog)
        self.combotipo.setObjectName(u"combotipo")
        self.combotipo.setGeometry(QRect(140, 70, 201, 32))

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Nuevo Usuario", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Nombre de Usuario", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Tipo", None))
    # retranslateUi

