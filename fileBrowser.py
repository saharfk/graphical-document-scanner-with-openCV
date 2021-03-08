import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


# you can copy and run this code

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        path = QFileDialog.getOpenFileName(self, 'Open a file', '',
                                           'All Files (*.*)')
        if path != ('', ''):
            print("File path : " + path[0])


app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
print('hiuh')
