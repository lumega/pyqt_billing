# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'G:\misimportaciones\src\ui\importaciones.ui'
#
# Created: Sat Sep 03 21:25:13 2011
#      by: PyQt4 UI code generator 4.7.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(676, 521)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.horizontalLayout_5.addWidget(self.mdiArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.ToolBarArea(QtCore.Qt.TopToolBarArea), self.toolBar)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 676, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuArchivo = QtGui.QMenu(self.menuBar)
        self.menuArchivo.setObjectName(_fromUtf8("menuArchivo"))
        self.menuProductos = QtGui.QMenu(self.menuBar)
        self.menuProductos.setObjectName(_fromUtf8("menuProductos"))
        self.menuVentanas = QtGui.QMenu(self.menuBar)
        self.menuVentanas.setObjectName(_fromUtf8("menuVentanas"))
        self.menuAyuda = QtGui.QMenu(self.menuBar)
        self.menuAyuda.setObjectName(_fromUtf8("menuAyuda"))
        MainWindow.setMenuBar(self.menuBar)
        self.actionAnular = QtGui.QAction(MainWindow)
        self.actionAnular.setEnabled(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/res/edit-delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAnular.setIcon(icon)
        self.actionAnular.setObjectName(_fromUtf8("actionAnular"))
        self.actionRecibo = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/res/okteta.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRecibo.setIcon(icon1)
        self.actionRecibo.setObjectName(_fromUtf8("actionRecibo"))
        self.newAct = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/res/document-new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.newAct.setIcon(icon2)
        self.newAct.setObjectName(_fromUtf8("newAct"))
        self.actionAbrir = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/res/document-edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAbrir.setIcon(icon3)
        self.actionAbrir.setObjectName(_fromUtf8("actionAbrir"))
        self.exitAct = QtGui.QAction(MainWindow)
        self.exitAct.setObjectName(_fromUtf8("exitAct"))
        self.saveAct = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/res/document-save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveAct.setIcon(icon4)
        self.saveAct.setObjectName(_fromUtf8("saveAct"))
        self.actionEditar_Productos = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/res/view-bank-account.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEditar_Productos.setIcon(icon5)
        self.actionEditar_Productos.setObjectName(_fromUtf8("actionEditar_Productos"))
        self.closeAct = QtGui.QAction(MainWindow)
        self.closeAct.setObjectName(_fromUtf8("closeAct"))
        self.closeAllAct = QtGui.QAction(MainWindow)
        self.closeAllAct.setObjectName(_fromUtf8("closeAllAct"))
        self.tileAct = QtGui.QAction(MainWindow)
        self.tileAct.setObjectName(_fromUtf8("tileAct"))
        self.cascadeAct = QtGui.QAction(MainWindow)
        self.cascadeAct.setObjectName(_fromUtf8("cascadeAct"))
        self.nextAct = QtGui.QAction(MainWindow)
        self.nextAct.setObjectName(_fromUtf8("nextAct"))
        self.previousAct = QtGui.QAction(MainWindow)
        self.previousAct.setObjectName(_fromUtf8("previousAct"))
        self.aboutAct = QtGui.QAction(MainWindow)
        self.aboutAct.setObjectName(_fromUtf8("aboutAct"))
        self.printAct = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/res/document-print.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.printAct.setIcon(icon6)
        self.printAct.setObjectName(_fromUtf8("printAct"))
        self.previewAct = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/res/document-preview.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.previewAct.setIcon(icon7)
        self.previewAct.setObjectName(_fromUtf8("previewAct"))
        self.actionInventario = QtGui.QAction(MainWindow)
        self.actionInventario.setObjectName(_fromUtf8("actionInventario"))
        self.fontAct = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/res/font.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.fontAct.setIcon(icon8)
        self.fontAct.setObjectName(_fromUtf8("fontAct"))
        self.toolBar.addAction(self.newAct)
        self.toolBar.addAction(self.actionAbrir)
        self.toolBar.addAction(self.saveAct)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.previewAct)
        self.toolBar.addAction(self.printAct)
        self.menuArchivo.addAction(self.newAct)
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addAction(self.saveAct)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.exitAct)
        self.menuProductos.addAction(self.actionEditar_Productos)
        self.menuProductos.addAction(self.actionInventario)
        self.menuVentanas.addAction(self.closeAct)
        self.menuVentanas.addAction(self.closeAllAct)
        self.menuVentanas.addSeparator()
        self.menuVentanas.addAction(self.tileAct)
        self.menuVentanas.addAction(self.cascadeAct)
        self.menuVentanas.addSeparator()
        self.menuVentanas.addAction(self.nextAct)
        self.menuVentanas.addAction(self.previousAct)
        self.menuAyuda.addAction(self.aboutAct)
        self.menuBar.addAction(self.menuArchivo.menuAction())
        self.menuBar.addAction(self.menuProductos.menuAction())
        self.menuBar.addAction(self.menuVentanas.menuAction())
        self.menuBar.addAction(self.menuAyuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Factura", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.menuArchivo.setTitle(QtGui.QApplication.translate("MainWindow", "Archivo", None, QtGui.QApplication.UnicodeUTF8))
        self.menuProductos.setTitle(QtGui.QApplication.translate("MainWindow", "Productos", None, QtGui.QApplication.UnicodeUTF8))
        self.menuVentanas.setTitle(QtGui.QApplication.translate("MainWindow", "Ventanas", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAyuda.setTitle(QtGui.QApplication.translate("MainWindow", "Ayuda", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAnular.setText(QtGui.QApplication.translate("MainWindow", "anular", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAnular.setToolTip(QtGui.QApplication.translate("MainWindow", "Anular la Factura", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecibo.setText(QtGui.QApplication.translate("MainWindow", "Recibo", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecibo.setToolTip(QtGui.QApplication.translate("MainWindow", "Recibos", None, QtGui.QApplication.UnicodeUTF8))
        self.newAct.setText(QtGui.QApplication.translate("MainWindow", "Nueva Factura", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbrir.setText(QtGui.QApplication.translate("MainWindow", "Abrir", None, QtGui.QApplication.UnicodeUTF8))
        self.exitAct.setText(QtGui.QApplication.translate("MainWindow", "Salir", None, QtGui.QApplication.UnicodeUTF8))
        self.saveAct.setText(QtGui.QApplication.translate("MainWindow", "Guardar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEditar_Productos.setText(QtGui.QApplication.translate("MainWindow", "Editar Productos", None, QtGui.QApplication.UnicodeUTF8))
        self.closeAct.setText(QtGui.QApplication.translate("MainWindow", "Cerrar", None, QtGui.QApplication.UnicodeUTF8))
        self.closeAllAct.setText(QtGui.QApplication.translate("MainWindow", "Cerrar Todo", None, QtGui.QApplication.UnicodeUTF8))
        self.tileAct.setText(QtGui.QApplication.translate("MainWindow", "Titulo", None, QtGui.QApplication.UnicodeUTF8))
        self.cascadeAct.setText(QtGui.QApplication.translate("MainWindow", "Cascada", None, QtGui.QApplication.UnicodeUTF8))
        self.nextAct.setText(QtGui.QApplication.translate("MainWindow", "Siguiente", None, QtGui.QApplication.UnicodeUTF8))
        self.previousAct.setText(QtGui.QApplication.translate("MainWindow", "Anterior", None, QtGui.QApplication.UnicodeUTF8))
        self.aboutAct.setText(QtGui.QApplication.translate("MainWindow", "Acerda de ...", None, QtGui.QApplication.UnicodeUTF8))
        self.printAct.setText(QtGui.QApplication.translate("MainWindow", "Imprimir", None, QtGui.QApplication.UnicodeUTF8))
        self.printAct.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+P", None, QtGui.QApplication.UnicodeUTF8))
        self.previewAct.setText(QtGui.QApplication.translate("MainWindow", "Vista Previa", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInventario.setText(QtGui.QApplication.translate("MainWindow", "Inventario", None, QtGui.QApplication.UnicodeUTF8))
        self.fontAct.setText(QtGui.QApplication.translate("MainWindow", "Tipo de Letra", None, QtGui.QApplication.UnicodeUTF8))

import res_rc