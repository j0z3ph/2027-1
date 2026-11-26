# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ventana.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(356, 331)
        self.actionNuevo = QAction(MainWindow)
        self.actionNuevo.setObjectName(u"actionNuevo")
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionAcerca_de = QAction(MainWindow)
        self.actionAcerca_de.setObjectName(u"actionAcerca_de")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.tabla = QTableWidget(self.centralwidget)
        self.tabla.setObjectName(u"tabla")

        self.gridLayout.addWidget(self.tabla, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 356, 30))
        self.menuArchivo = QMenu(self.menuBar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuAyuda = QMenu(self.menuBar)
        self.menuAyuda.setObjectName(u"menuAyuda")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuArchivo.menuAction())
        self.menuBar.addAction(self.menuAyuda.menuAction())
        self.menuArchivo.addAction(self.actionNuevo)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menuAyuda.addAction(self.actionAcerca_de)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ventana Principal", None))
        self.actionNuevo.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
#if QT_CONFIG(shortcut)
        self.actionNuevo.setShortcut(QCoreApplication.translate("MainWindow", u"Meta+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
#if QT_CONFIG(shortcut)
        self.actionSalir.setShortcut(QCoreApplication.translate("MainWindow", u"Meta+X", None))
#endif // QT_CONFIG(shortcut)
        self.actionAcerca_de.setText(QCoreApplication.translate("MainWindow", u"Acerca de ...", None))
#if QT_CONFIG(shortcut)
        self.actionAcerca_de.setShortcut(QCoreApplication.translate("MainWindow", u"Meta+Y", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Productos Registrados", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("MainWindow", u"Archivo", None))
        self.menuAyuda.setTitle(QCoreApplication.translate("MainWindow", u"Ayuda", None))
    # retranslateUi

