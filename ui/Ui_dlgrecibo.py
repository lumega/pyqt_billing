# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/windows/C/workspace/EsquipulasPy/esquipulaspy/ui/dlgrecibo.ui'
#
# Created by: PyQt4 UI code generator 4.7.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_dlgRecibo(object):
    def setupUi(self, dlgRecibo):
        dlgRecibo.setObjectName("dlgRecibo")
        dlgRecibo.resize(714, 443)
        self.verticalLayout = QtGui.QVBoxLayout(dlgRecibo)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_4 = QtGui.QGroupBox(dlgRecibo)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 140))
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lblnrec = QtGui.QLabel(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblnrec.sizePolicy().hasHeightForWidth())
        self.lblnrec.setSizePolicy(sizePolicy)
        self.lblnrec.setStyleSheet("border:1px solid #000")
        self.lblnrec.setAlignment(QtCore.Qt.AlignCenter)
        self.lblnrec.setObjectName("lblnrec")
        self.gridLayout.addWidget(self.lblnrec, 0, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_4)
        self.label_7.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 2)
        self.lblnreten = QtGui.QLabel(self.groupBox_4)
        self.lblnreten.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblnreten.sizePolicy().hasHeightForWidth())
        self.lblnreten.setSizePolicy(sizePolicy)
        self.lblnreten.setMaximumSize(QtCore.QSize(16777215, 20))
        self.lblnreten.setStyleSheet("border:1px solid #000")
        self.lblnreten.setAlignment(QtCore.Qt.AlignCenter)
        self.lblnreten.setObjectName("lblnreten")
        self.gridLayout.addWidget(self.lblnreten, 0, 4, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 5, 1, 1)
        self.lblfecha = QtGui.QLabel(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblfecha.sizePolicy().hasHeightForWidth())
        self.lblfecha.setSizePolicy(sizePolicy)
        self.lblfecha.setAlignment(QtCore.Qt.AlignCenter)
        self.lblfecha.setObjectName("lblfecha")
        self.gridLayout.addWidget(self.lblfecha, 0, 6, 1, 1)
        self.label = QtGui.QLabel(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.txtcliente = QtGui.QLineEdit(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtcliente.sizePolicy().hasHeightForWidth())
        self.txtcliente.setSizePolicy(sizePolicy)
        self.txtcliente.setMinimumSize(QtCore.QSize(0, 20))
        self.txtcliente.setReadOnly(True)
        self.txtcliente.setObjectName("txtcliente")
        self.gridLayout.addWidget(self.txtcliente, 1, 1, 1, 6)
        self.label_6 = QtGui.QLabel(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.txtconcepto = QtGui.QLineEdit(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txtconcepto.sizePolicy().hasHeightForWidth())
        self.txtconcepto.setSizePolicy(sizePolicy)
        self.txtconcepto.setMinimumSize(QtCore.QSize(0, 20))
        self.txtconcepto.setStyleSheet("None")
        self.txtconcepto.setAlignment(QtCore.Qt.AlignCenter)
        self.txtconcepto.setDragEnabled(True)
        self.txtconcepto.setReadOnly(True)
        self.txtconcepto.setObjectName("txtconcepto")
        self.gridLayout.addWidget(self.txtconcepto, 2, 1, 1, 4)
        self.swtasaret = QtGui.QStackedWidget(self.groupBox_4)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.swtasaret.sizePolicy().hasHeightForWidth())
        self.swtasaret.setSizePolicy(sizePolicy)
        self.swtasaret.setMinimumSize(QtCore.QSize(0, 30))
        self.swtasaret.setMaximumSize(QtCore.QSize(80, 30))
        self.swtasaret.setObjectName("swtasaret")
        self.page_9 = QtGui.QWidget()
        self.page_9.setObjectName("page_9")
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.page_9)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.cbtasaret = QtGui.QComboBox(self.page_9)
        self.cbtasaret.setMinimumSize(QtCore.QSize(0, 20))
        self.cbtasaret.setEditable(False)
        self.cbtasaret.setObjectName("cbtasaret")
        self.horizontalLayout_9.addWidget(self.cbtasaret)
        self.label_8 = QtGui.QLabel(self.page_9)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.swtasaret.addWidget(self.page_9)
        self.page_10 = QtGui.QWidget()
        self.page_10.setObjectName("page_10")
        self.horizontalLayout_10 = QtGui.QHBoxLayout(self.page_10)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.txttasaret = QtGui.QLineEdit(self.page_10)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txttasaret.sizePolicy().hasHeightForWidth())
        self.txttasaret.setSizePolicy(sizePolicy)
        self.txttasaret.setMinimumSize(QtCore.QSize(0, 20))
        self.txttasaret.setStyleSheet("None")
        self.txttasaret.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txttasaret.setDragEnabled(True)
        self.txttasaret.setReadOnly(True)
        self.txttasaret.setObjectName("txttasaret")
        self.horizontalLayout_10.addWidget(self.txttasaret)
        self.label_9 = QtGui.QLabel(self.page_10)
        self.label_9.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_10.addWidget(self.label_9)
        self.swtasaret.addWidget(self.page_10)
        self.gridLayout.addWidget(self.swtasaret, 2, 6, 1, 1)
        self.ckretener = QtGui.QCheckBox(self.groupBox_4)
        self.ckretener.setEnabled(False)
        self.ckretener.setChecked(True)
        self.ckretener.setObjectName("ckretener")
        self.gridLayout.addWidget(self.ckretener, 2, 5, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.groupBox_3 = QtGui.QGroupBox(dlgRecibo)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.tabledetails = QtGui.QTableView(self.groupBox_3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabledetails.sizePolicy().hasHeightForWidth())
        self.tabledetails.setSizePolicy(sizePolicy)
        self.tabledetails.setMinimumSize(QtCore.QSize(0, 70))
        self.tabledetails.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tabledetails.setObjectName("tabledetails")
        self.horizontalLayout_7.addWidget(self.tabledetails)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.label_20 = QtGui.QLabel(dlgRecibo)
        self.label_20.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setObjectName("label_20")
        self.verticalLayout.addWidget(self.label_20)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.txtobservaciones = QtGui.QPlainTextEdit(dlgRecibo)
        self.txtobservaciones.setEnabled(True)
        self.txtobservaciones.setMaximumSize(QtCore.QSize(16777215, 50))
        self.txtobservaciones.setReadOnly(True)
        self.txtobservaciones.setObjectName("txtobservaciones")
        self.horizontalLayout_2.addWidget(self.txtobservaciones)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtGui.QLabel(dlgRecibo)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.lbltotal = QtGui.QLabel(dlgRecibo)
        self.lbltotal.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbltotal.setObjectName("lbltotal")
        self.gridLayout_2.addWidget(self.lbltotal, 0, 1, 1, 1)
        self.label_19 = QtGui.QLabel(dlgRecibo)
        self.label_19.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_19.sizePolicy().hasHeightForWidth())
        self.label_19.setSizePolicy(sizePolicy)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 1, 0, 1, 1)
        self.lbltotalreten = QtGui.QLabel(dlgRecibo)
        self.lbltotalreten.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbltotalreten.sizePolicy().hasHeightForWidth())
        self.lbltotalreten.setSizePolicy(sizePolicy)
        self.lbltotalreten.setMinimumSize(QtCore.QSize(0, 20))
        self.lbltotalreten.setStyleSheet("None")
        self.lbltotalreten.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbltotalreten.setObjectName("lbltotalreten")
        self.gridLayout_2.addWidget(self.lbltotalreten, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(dlgRecibo)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 0, 2, 1)
        self.lbltotalrecibo = QtGui.QLabel(dlgRecibo)
        self.lbltotalrecibo.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbltotalrecibo.setObjectName("lbltotalrecibo")
        self.gridLayout_2.addWidget(self.lbltotalrecibo, 2, 1, 2, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.buttonBox = QtGui.QDialogButtonBox(dlgRecibo)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_6.setBuddy(self.txtconcepto)

        self.retranslateUi(dlgRecibo)
        self.swtasaret.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), dlgRecibo.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), dlgRecibo.reject)
        QtCore.QMetaObject.connectSlotsByName(dlgRecibo)

    def retranslateUi(self, dlgRecibo):
        dlgRecibo.setWindowTitle(QtGui.QApplication.translate("dlgRecibo", "Recibo", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("dlgRecibo", "Datos del Recibo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("dlgRecibo", "<b>Recibo No.</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblnrec.setText(QtGui.QApplication.translate("dlgRecibo", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("dlgRecibo", "<b>Retención No.</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblnreten.setText(QtGui.QApplication.translate("dlgRecibo", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("dlgRecibo", "<b>Fecha</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.lblfecha.setText(QtGui.QApplication.translate("dlgRecibo", "01/09/2010", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dlgRecibo", "<b>Recibimos de:</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("dlgRecibo", "<b>En concepto de:</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.txtconcepto.setText(QtGui.QApplication.translate("dlgRecibo", "Cancelacion de Factura", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("dlgRecibo", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.txttasaret.setText(QtGui.QApplication.translate("dlgRecibo", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("dlgRecibo", "%", None, QtGui.QApplication.UnicodeUTF8))
        self.ckretener.setText(QtGui.QApplication.translate("dlgRecibo", "Retener", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("dlgRecibo", "Especifique los tipos de pagos", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("dlgRecibo", "<b>Observaciones </b>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("dlgRecibo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Total a pagar</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lbltotal.setText(QtGui.QApplication.translate("dlgRecibo", "0.0000", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("dlgRecibo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">-Retención</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lbltotalreten.setText(QtGui.QApplication.translate("dlgRecibo", "0.0000", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("dlgRecibo", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt; font-weight:600;\">Total Recibido</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.lbltotalrecibo.setText(QtGui.QApplication.translate("dlgRecibo", "0.0000", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    dlgRecibo = QtGui.QDialog()
    ui = Ui_dlgRecibo()
    ui.setupUi(dlgRecibo)
    dlgRecibo.show()
    sys.exit(app.exec_())
