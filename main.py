from PySide6.QtCore import QEvent, QTimer, Qt
from PySide6 import QtWidgets, QtGui
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from functions import resource_path
import sys
import space
import user
import theme

class TelaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QCloud")
        self.initUI()


    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignCenter)

        label_texto = QLabel("QCloud Integration with cVortex", self)
        image_label = QLabel(self)
        image_label.setAlignment(Qt.AlignHCenter)
        image_path = resource_path("assets/QCloud_128.png")
        image_label.setPixmap(QPixmap(image_path))
        vbox.addWidget(label_texto)
        vbox.addWidget(image_label)
        vbox.addSpacing(10)

        layout.addLayout(vbox)
        layout.setAlignment(Qt.AlignCenter)

        button_fluxo = QPushButton("Flow", self)
        button_usuarios = QPushButton("Users", self)

        button_layout = QHBoxLayout()
        button_layout.addWidget(button_fluxo)
        button_layout.addWidget(button_usuarios)

        layout.addLayout(button_layout)

        button_fluxo.clicked.connect(self.abrir_interface_fluxo)
        button_usuarios.clicked.connect(self.abrir_interface_usuarios)

    def abrir_interface_fluxo(self):
        self.hide()
        self.screenspace = space.SpaceScreen(self)
        self.screenspace.show()

    def abrir_interface_usuarios(self):
        self.hide()
        self.screenuser = user.CreateUserScreen(self)
        self.screenuser.show()

def main():
    app = QApplication(sys.argv)
    main_window = TelaPrincipal()
    theme.set_theme(main_window, app)
    main_window.setWindowTitle("QCloud")
    main_window.setFixedSize(300, 250)
    main_window.show()
    app.setApplicationName("QCloud")
    image_path = resource_path("assets/QCloud.ico")
    icon = QtGui.QIcon(image_path)
    main_window.setWindowIcon(QIcon(icon))
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
