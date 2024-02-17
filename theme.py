import platform
from PySide6.QtCore import QTimer
from PySide6.QtGui import QPalette
from PySide6.QtWidgets import QApplication
import config

def set_theme(self, app):
    op = get_operating_system()
    if op == "Darwin":
        macOS_theme()
        app.paletteChanged.connect(macOS_theme)
    elif op == "Windows":
        win_dark()
        self.dark_theme_timer = QTimer(self)
        self.dark_theme_timer.timeout.connect(win_dark)
        self.dark_theme_timer.start(1000)  # Check every 1 second
    else:
        a = None

def win_dark():
    try:
        from winreg import ConnectRegistry, OpenKey, HKEY_CURRENT_USER, QueryValueEx
        registry = ConnectRegistry(None, HKEY_CURRENT_USER)
        key = OpenKey(registry, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize")
        value, _ = QueryValueEx(key, "AppsUseLightTheme")
        if value:
            applytheme(0)
        else:
            applytheme(1)
    except Exception as e:
        print(f"Error checking Windows dark mode: {e}")
        return False

def macOS_theme():
    darktheme = macOS_dark()
    applytheme(darktheme)

def macOS_dark():
    current_palette = QApplication.instance().palette()
    background_color = current_palette.color(QPalette.Window)
    return background_color.lightness() < 128
def get_operating_system():
    return platform.system()

def applytheme(isdarktheme):
    if  isdarktheme:
        color_theme = config.color_themedark
        color_contrast = config.color_themelight
        color_onhover = config.color_onhover
    else:
        color_theme = config.color_themelight
        color_contrast = config.color_themedark
        color_onhover = config.color_onhover

    stylesheet = f"""
    QWidget {{
        background-color: {color_theme};
    }}
    QLineEdit {{
        color: {color_contrast};
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
        background-color: {color_onhover};
        color:white;
    }}
    QPushButton:pressed {{
        background-color: {color_onhover};
    }}
    QLabel {{
        color: {color_contrast};
    }}
    QComboBox {{
        color: {color_contrast};
        border: 2px solid #666666;
        border-radius: 5px;
        padding: 5px;
        padding-right: 20px;
    }}
    QComboBox QAbstractItemView {{
        color: {color_contrast}; 
    }}    
    QCheckBox {{
        color: {color_contrast};
    }}                
    """
    QApplication.instance().setStyleSheet(stylesheet)



