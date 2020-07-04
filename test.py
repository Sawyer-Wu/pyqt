import sys
import test1

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    ui = test1.Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.show()

    sys.exit(app.exec())