# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(742, 381)
        Dialog.setStyleSheet("background-color: rgba(179, 218, 255, 255);\n"
                             "")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.originalPhoto = QtWidgets.QPushButton(Dialog)
        self.originalPhoto.setGeometry(QtCore.QRect(90, 70, 151, 41))
        self.originalPhoto.setAutoFillBackground(False)
        self.originalPhoto.setStyleSheet("background-color: rgba(51, 156, 255,170);\n"
                                         "")
        self.originalPhoto.setCheckable(False)
        self.originalPhoto.setObjectName("originalPhoto")
        self.gray = QtWidgets.QPushButton(Dialog)
        self.gray.setGeometry(QtCore.QRect(90, 130, 151, 41))
        self.gray.setAutoFillBackground(False)
        self.gray.setStyleSheet("background-color: rgba(51, 156, 255,170);\n"
                                "\n"
                                "")
        self.gray.setCheckable(False)
        self.gray.setObjectName("gray")
        self.blured = QtWidgets.QPushButton(Dialog)
        self.blured.setGeometry(QtCore.QRect(90, 190, 151, 41))
        self.blured.setAutoFillBackground(False)
        self.blured.setStyleSheet("background-color: rgba(51, 156, 255,170);\n"
                                  "")
        self.blured.setCheckable(False)
        self.blured.setObjectName("blured")
        self.edged = QtWidgets.QPushButton(Dialog)
        self.edged.setGeometry(QtCore.QRect(90, 250, 151, 41))
        self.edged.setAutoFillBackground(False)
        self.edged.setStyleSheet("background-color: rgba(51, 156, 255,170);\n"
                                 "")
        self.edged.setCheckable(False)
        self.edged.setObjectName("edged")
        self.outliner = QtWidgets.QPushButton(Dialog)
        self.outliner.setGeometry(QtCore.QRect(90, 310, 151, 41))
        self.outliner.setAutoFillBackground(False)
        self.outliner.setStyleSheet("background-color: rgba(51, 156, 255,170);\n"
                                    "")
        self.outliner.setCheckable(False)
        self.outliner.setObjectName("outliner")
        self.originalScan = QtWidgets.QPushButton(Dialog)
        self.originalScan.setGeometry(QtCore.QRect(280, 70, 151, 41))
        self.originalScan.setAutoFillBackground(False)
        self.originalScan.setStyleSheet("background-color: rgba(51, 156, 255,170);\n"
                                        "")
        self.originalScan.setCheckable(False)
        self.originalScan.setObjectName("originalScan")
        self.wrapGrayScan = QtWidgets.QPushButton(Dialog)
        self.wrapGrayScan.setGeometry(QtCore.QRect(280, 130, 151, 41))
        self.wrapGrayScan.setAutoFillBackground(False)
        self.wrapGrayScan.setStyleSheet("background-color: rgba(51, 156, 255,170);\n"
                                        "")
        self.wrapGrayScan.setCheckable(False)
        self.wrapGrayScan.setObjectName("wrapGrayScan")
        self.blackAndWhiteScan = QtWidgets.QPushButton(Dialog)
        self.blackAndWhiteScan.setGeometry(QtCore.QRect(280, 190, 151, 41))
        self.blackAndWhiteScan.setAutoFillBackground(False)
        self.blackAndWhiteScan.setStyleSheet("background-color: rgba(51, 156, 255,170);\n"
                                             "")
        self.blackAndWhiteScan.setCheckable(False)
        self.blackAndWhiteScan.setObjectName("blackAndWhiteScan")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setStyleSheet(
            "background-color:qconicalgradient(cx:0, cy:1, angle:0, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0))")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(530, 10, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(False)
        self.label_2.setStyleSheet(
            "background-color:qconicalgradient(cx:0, cy:1, angle:0, stop:0 rgba(255, 255, 255, 0), stop:1 rgba(255, 255, 255, 0))")
        self.label_2.setObjectName("label_2")
        self.binaryScan = QtWidgets.QPushButton(Dialog)
        self.binaryScan.setGeometry(QtCore.QRect(280, 250, 151, 41))
        self.binaryScan.setAutoFillBackground(False)
        self.binaryScan.setStyleSheet("background-color: rgba(51, 156, 255,170);\n"
                                      "")
        self.binaryScan.setCheckable(False)
        self.binaryScan.setObjectName("binaryScan")
        self.grayScan = QtWidgets.QPushButton(Dialog)
        self.grayScan.setGeometry(QtCore.QRect(280, 310, 151, 41))
        self.grayScan.setAutoFillBackground(False)
        self.grayScan.setStyleSheet("background-color: rgba(51, 156, 255,170);\n"
                                    "")
        self.grayScan.setCheckable(False)
        self.grayScan.setObjectName("grayScan")
        self.blackAndWhitePDF = QtWidgets.QPushButton(Dialog)
        self.blackAndWhitePDF.setGeometry(QtCore.QRect(510, 190, 151, 41))
        self.blackAndWhitePDF.setAutoFillBackground(False)
        self.blackAndWhitePDF.setStyleSheet("background-color: rgba(51, 156, 255,170);\n"
                                            "")
        self.blackAndWhitePDF.setCheckable(False)
        self.blackAndWhitePDF.setObjectName("blackAndWhitePDF")
        self.grayPDF = QtWidgets.QPushButton(Dialog)
        self.grayPDF.setGeometry(QtCore.QRect(510, 310, 151, 41))
        self.grayPDF.setAutoFillBackground(False)
        self.grayPDF.setStyleSheet("background-color: rgba(51, 156, 255,170);\n"
                                   "")
        self.grayPDF.setCheckable(False)
        self.grayPDF.setObjectName("grayPDF")
        self.binaryPDF = QtWidgets.QPushButton(Dialog)
        self.binaryPDF.setGeometry(QtCore.QRect(510, 250, 151, 41))
        self.binaryPDF.setAutoFillBackground(False)
        self.binaryPDF.setStyleSheet("background-color: rgba(51, 156, 255,170);\n"
                                     "")
        self.binaryPDF.setCheckable(False)
        self.binaryPDF.setObjectName("binaryPDF")
        self.originalScanPDF = QtWidgets.QPushButton(Dialog)
        self.originalScanPDF.setGeometry(QtCore.QRect(510, 70, 151, 41))
        self.originalScanPDF.setAutoFillBackground(False)
        self.originalScanPDF.setStyleSheet("background-color: rgba(51, 156, 255,170);\n"
                                           "")
        self.originalScanPDF.setCheckable(False)
        self.originalScanPDF.setObjectName("originalScanPDF")
        self.wrapGrayPDF = QtWidgets.QPushButton(Dialog)
        self.wrapGrayPDF.setGeometry(QtCore.QRect(510, 130, 151, 41))
        self.wrapGrayPDF.setAutoFillBackground(False)
        self.wrapGrayPDF.setStyleSheet("background-color: rgba(51, 156, 255,170);\n"
                                       "")
        self.wrapGrayPDF.setCheckable(False)
        self.wrapGrayPDF.setObjectName("wrapGrayPDF")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(460, 20, 20, 341))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(Dialog)
        self.binaryPDF.clicked.connect(self.dbinaryPDF)
        self.binaryScan.clicked.connect(self.dbinaryScan)
        self.blackAndWhitePDF.clicked.connect(self.dblackAndWhitePDF)
        self.blackAndWhiteScan.clicked.connect(self.dblackAndWhiteScan)
        self.blured.clicked.connect(self.dblured)
        self.edged.clicked.connect(self.dedged)
        self.gray.clicked.connect(self.dgray)
        self.grayPDF.clicked.connect(self.dgrayPDF)
        self.grayScan.clicked.connect(self.dgrayScan)
        self.originalPhoto.clicked.connect(self.doriginalPhoto)
        self.originalScan.clicked.connect(self.doriginalScan)
        self.originalScanPDF.clicked.connect(self.doriginalScanPDF)
        self.outliner.clicked.connect(self.doutliner)
        self.wrapGrayPDF.clicked.connect(self.dwrapGrayPDF)
        self.wrapGrayScan.clicked.connect(self.dwrapGrayScan)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.originalPhoto.setText(_translate("Dialog", "Original photo"))
        self.gray.setText(_translate("Dialog", "Gray"))
        self.blured.setText(_translate("Dialog", "Blurred"))
        self.edged.setText(_translate("Dialog", "Edged"))
        self.outliner.setText(_translate("Dialog", "outliner"))
        self.originalScan.setText(_translate("Dialog", "original scan"))
        self.wrapGrayScan.setText(_translate("Dialog", "Warp Gray scan"))
        self.blackAndWhiteScan.setText(_translate("Dialog", "black and white scan"))
        self.label.setText(_translate("Dialog", "select an option :"))
        self.label_2.setText(_translate("Dialog", "PDF options :"))
        self.binaryScan.setText(_translate("Dialog", "binary scan"))
        self.grayScan.setText(_translate("Dialog", "gray scan"))
        self.blackAndWhitePDF.setText(_translate("Dialog", "black and white scan"))
        self.grayPDF.setText(_translate("Dialog", "gray scan"))
        self.binaryPDF.setText(_translate("Dialog", "binary scan"))
        self.originalScanPDF.setText(_translate("Dialog", "original scan"))
        self.wrapGrayPDF.setText(_translate("Dialog", "Warp Gray scan"))

    def doriginalPhoto(self):
        pass

    def dgray(self):
        pass

    def dblured(self):
        pass

    def dedged(self):
        pass

    def doutliner(self):
        pass

    def doriginalScan(self):
        pass

    def dwrapGrayScan(self):
        pass

    def dblackAndWhiteScan(self):
        pass

    def dbinaryScan(self):
        pass

    def dgrayScan(self):
        pass

    def dblackAndWhitePDF(self):
        pass

    def dgrayPDF(self):
        pass

    def dbinaryPDF(self):
        pass

    def doriginalScanPDF(self):
        pass

    def dwrapGrayPDF(self):
        pass


app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())
