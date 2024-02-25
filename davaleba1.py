import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QLabel, QMessageBox, QStackedWidget

class LoginWidget(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        layout = QVBoxLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('Username')
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)  
        self.password_input.setPlaceholderText('Password')
        layout.addWidget(self.password_input)

        login_button = QPushButton('Login')
        login_button.clicked.connect(self.check_credentials)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def check_credentials(self):
        correct_username = 'admin'
        correct_password = 'admin123'

        username = self.username_input.text()
        password = self.password_input.text()

        if username == correct_username and password == correct_password:
            self.stacked_widget.setCurrentIndex(1)  
        else:
            QMessageBox.warning(self, 'Error', 'Incorrect username or password')

class WelcomeWidget(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        welcome_label = QLabel('Welcome to the system!')
        layout.addWidget(welcome_label)
        self.setLayout(layout)

class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.login_widget = LoginWidget(self)
        self.addWidget(self.login_widget)

        self.welcome_widget = WelcomeWidget()
        self.addWidget(self.welcome_widget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
