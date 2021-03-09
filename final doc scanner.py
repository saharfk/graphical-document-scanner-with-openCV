import cv2
import numpy as np
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets

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
        cv2.imshow("Original", orig)

    def dgray(self):
        cv2.imshow("Original Gray", gray)

    def dblured(self):
        cv2.imshow("Original Blurred", blurred)

    def dedged(self):
        cv2.imshow("Original Edged", orig_edged)

    def doutliner(self):
        cv2.imshow("Outline", image)

    def doriginalScan(self):
        cv2.imshow("originalscan", imgWarpColored)

    def dwrapGrayScan(self):
        cv2.imshow("doc grayscale", dst)

    def dblackAndWhiteScan(self):
        cv2.imshow("black and white scan", th4)

    def dbinaryScan(self):
        cv2.imshow("binary scan", thresh1)

    def dgrayScan(self):
        cv2.imshow("gray scan", thresh2)

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


def rectify(h):
    h = h.reshape((4, 2))
    hnew = np.zeros((4, 2), dtype=np.float32)

    add = h.sum(1)
    hnew[0] = h[np.argmin(add)]
    hnew[2] = h[np.argmax(add)]

    diff = np.diff(h, axis=1)
    hnew[1] = h[np.argmin(diff)]
    hnew[3] = h[np.argmax(diff)]

    return hnew


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        path = QFileDialog.getOpenFileName(self, 'Open a file', '',
                                           'All Files (*.*)')
        if path != ('', ''):
            global g
            g = path[0]


app = QApplication(sys.argv)
window = MainWindow()
# add image here.
image = cv2.imread(g)

# resize image so it can be processed
# choose optimal dimensions such that important content is not lost
image = cv2.resize(image, (1500, 880))

# *************************

# creating copy of original image
orig = image.copy()

# ***********************

# convert to grayscale and blur to smooth
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# ********************************

# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
blurred = cv2.medianBlur(gray, 5)

# *******************************

# apply Canny Edge Detection
edged = cv2.Canny(blurred, 0, 50)
orig_edged = edged.copy()
# ******************************

# find the contours in the edged image, keeping only the
# largest ones, and initialize the screen contour
(contours, _) = cv2.findContours(edged, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)

# get approximate contour
for c in contours:
    p = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * p, True)

    if len(approx) == 4:
        target = approx
        break

# mapping target points to 800x800 quadrilateral
approx = rectify(target)
pts2 = np.float32([[0, 0], [800, 0], [800, 800], [0, 800]])

M = cv2.getPerspectiveTransform(approx, pts2)
dst = cv2.warpPerspective(orig, M, (800, 800))

imgWarpColored = cv2.warpPerspective(orig, M, (800, 800))
cv2.drawContours(image, [target], -1, (0, 255, 0), 2)
dst = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
# *****************************

# using thresholding on warped image to get scanned effect (If Required)
ret2, th4 = cv2.threshold(dst, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# other thresholding methods

ret, thresh1 = cv2.threshold(dst, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh2 = cv2.threshold(dst, 127, 255, cv2.THRESH_TOZERO)
cv2.waitKey(0)
cv2.destroyAllWindows()

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())



