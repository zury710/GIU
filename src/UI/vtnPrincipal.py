# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtnPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_vtnPrincipal(object):
    def setupUi(self, vtnPrincipal):
        if not vtnPrincipal.objectName():
            vtnPrincipal.setObjectName(u"vtnPrincipal")
        vtnPrincipal.resize(800, 600)
        self.centralwidget = QWidget(vtnPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lbNombre = QLabel(self.centralwidget)
        self.lbNombre.setObjectName(u"lbNombre")
        self.lbNombre.setGeometry(QRect(120, 30, 91, 20))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lbNombre.setFont(font)
        self.lbCedula = QLabel(self.centralwidget)
        self.lbCedula.setObjectName(u"lbCedula")
        self.lbCedula.setGeometry(QRect(120, 150, 81, 20))
        self.lbCedula.setFont(font)
        self.lbApelido = QLabel(self.centralwidget)
        self.lbApelido.setObjectName(u"lbApelido")
        self.lbApelido.setGeometry(QRect(120, 90, 91, 20))
        self.lbApelido.setFont(font)
        self.txtNombre = QLineEdit(self.centralwidget)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(210, 30, 301, 20))
        self.txtNombre.setMaxLength(50)
        self.txtApellido = QLineEdit(self.centralwidget)
        self.txtApellido.setObjectName(u"txtApellido")
        self.txtApellido.setGeometry(QRect(210, 90, 301, 20))
        self.txtApellido.setMaxLength(50)
        self.txtCedula = QLineEdit(self.centralwidget)
        self.txtCedula.setObjectName(u"txtCedula")
        self.txtCedula.setGeometry(QRect(210, 150, 301, 20))
        self.txtCedula.setMaxLength(10)
        self.btnGuardar = QPushButton(self.centralwidget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(230, 340, 75, 23))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.btnGuardar.setFont(font1)
        self.btnBorrar = QPushButton(self.centralwidget)
        self.btnBorrar.setObjectName(u"btnBorrar")
        self.btnBorrar.setGeometry(QRect(420, 340, 75, 23))
        self.btnBorrar.setFont(font1)
        self.lbCedula_3 = QLabel(self.centralwidget)
        self.lbCedula_3.setObjectName(u"lbCedula_3")
        self.lbCedula_3.setGeometry(QRect(120, 230, 81, 20))
        self.lbCedula_3.setFont(font)
        self.cbSexo = QLineEdit(self.centralwidget)
        self.cbSexo.setObjectName(u"cbSexo")
        self.cbSexo.setGeometry(QRect(210, 230, 301, 20))
        self.cbSexo.setMaxLength(100)
        self.cbSexo_2 = QComboBox(self.centralwidget)
        self.cbSexo_2.addItem("")
        self.cbSexo_2.addItem("")
        self.cbSexo_2.setObjectName(u"cbSexo_2")
        self.cbSexo_2.setGeometry(QRect(210, 190, 221, 24))
        self.lbCedula_2 = QLabel(self.centralwidget)
        self.lbCedula_2.setObjectName(u"lbCedula_2")
        self.lbCedula_2.setGeometry(QRect(120, 190, 81, 20))
        self.lbCedula_2.setFont(font)
        vtnPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtnPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        vtnPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtnPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        vtnPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(vtnPrincipal)

        QMetaObject.connectSlotsByName(vtnPrincipal)
    # setupUi

    def retranslateUi(self, vtnPrincipal):
        vtnPrincipal.setWindowTitle(QCoreApplication.translate("vtnPrincipal", u"Sistema de Gestion de Persona", None))
        self.lbNombre.setText(QCoreApplication.translate("vtnPrincipal", u"Nombre:", None))
        self.lbCedula.setText(QCoreApplication.translate("vtnPrincipal", u"C\u00e9dula:", None))
        self.lbApelido.setText(QCoreApplication.translate("vtnPrincipal", u"Apellido:", None))
        self.txtCedula.setText("")
        self.btnGuardar.setText(QCoreApplication.translate("vtnPrincipal", u"Guardar", None))
        self.btnBorrar.setText(QCoreApplication.translate("vtnPrincipal", u"Borrar", None))
        self.lbCedula_3.setText(QCoreApplication.translate("vtnPrincipal", u"Email", None))
        self.cbSexo.setText("")
        self.cbSexo_2.setItemText(0, QCoreApplication.translate("vtnPrincipal", u"Mujer", None))
        self.cbSexo_2.setItemText(1, QCoreApplication.translate("vtnPrincipal", u"Hombre", None))

        self.lbCedula_2.setText(QCoreApplication.translate("vtnPrincipal", u"Sexo", None))
    # retranslateUi

