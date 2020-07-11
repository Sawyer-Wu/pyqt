import sys
import hbgx_2

from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QMainWindow()
    ui = hbgx_2.Ui_MainWindow()
    ui.setupUi(mainwindow)
    mainwindow.show()

    sys.exit(app.exec())