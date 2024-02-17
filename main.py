from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout
from functions import resource_path
import sys
import space
import user
import webintegrations

def handlePaletteChanged():
    if isDarkTheme():
        color_theme = "#313131"
        color_contrast = "#F7F8FA"
    else:
        color_theme = "#F7F8FA"
        color_contrast = "#313131"
    stylesheet = f"""
    QWidget {{
        background-color: {color_theme};
    }}
    QPushButton {{
        background-color: {color_contrast};
        color: {color_theme};
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
    }}
    QPushButton:hover {{
        background-color: #FF8C00;
        color: #ffffff
    }}
    QPushButton:pressed {{
        background-color: #FF8C00;
    }}
    QLabel {{
        color: {color_contrast};
    }}
    QLineEdit {{
        background-color: {color_theme};
        color: {color_contrast};
        border: 2px solid {color_contrast};
        border-radius: 5px;
        padding: 5px;
    }}   
    QComboBox {{
        background-color: {color_theme};
        color: {color_contrast};
        border: 2px solid {color_contrast};
        border-radius: 5px;
        padding: 5px;
        padding-right: 20px;            
    }} 
    QComboBox QAbstractItemView {{
        background-color: {color_theme};
        color: {color_contrast};
    }}
    QComboBox QAbstractItemView::item:hover {{
        background-color: {color_contrast};
        color: {color_theme};
    }}
    QCheckBox {{
        font-size: 12px;
        color: {color_contrast};
    }}
    """
    QApplication.instance().setStyleSheet(stylesheet)


def isDarkTheme():
    current_palette = QApplication.instance().palette()
    background_color = current_palette.color(QPalette.Window)
    return background_color.lightness() < 128


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
        image_path = resource_path("assets/QCloud_128.png")  # Caminho absoluto da imagem
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

        button_fluxo.setProperty("class", "mac-button")
        button_usuarios.setProperty("class", "mac-button")

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
    app.paletteChanged.connect(handlePaletteChanged)
    main_window = TelaPrincipal()
    main_window.setWindowTitle("QCloud")
    main_window.setFixedSize(300, 250)
    main_window.show()
    app.setApplicationName("QCloud")
    app.setWindowIcon(QIcon("assets/QCloud.ico"))
    handlePaletteChanged()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
