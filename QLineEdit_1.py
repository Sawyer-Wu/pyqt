from PyQt5.QtWidgets import *
import sys


class QLineEditEchoMode(QWidget):
    def __init__(self):
        super(QLineEditEchoMode, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('回显')

        formLayout = QFormLayout()

        normalLineEdit = QLineEdit()  # 普通回显
        noEcholLineEdit = QLineEdit()  # 不回显
        passwordLineEdit = QLineEdit()  # 密码
        passwordEchoOnLineEdit = QLineEdit()  # 密码可视

        formLayout.addRow("Normal", normalLineEdit)
        formLayout.addRow("NoEcho", noEcholLineEdit)
        formLayout.addRow("Password", passwordLineEdit)
        formLayout.addRow("PasswordEchoOn", passwordEchoOnLineEdit)

        # placeholdertext

        normalLineEdit.setPlaceholderText("Normal")
        noEcholLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordEchoOnLineEdit.setPlaceholderText("PasswordEchoOn")

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEcholLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QLineEditEchoMode()
    mainwindow.show()

    sys.exit(app.exec())

