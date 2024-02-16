import config
from PySide6 import QtWidgets, QtCore, QtGui
from QlikAPI import create_space
from createwidgets import exp_textbox, exp_label, exp_combobox, exp_btn_back, exp_btn_next
from alertmessage import error_message, success_message, confirm_dialog
from connection import ConnectionScreen
import json
from PySide6.QtCore import Qt
import string
import re

class SpaceScreen(QtWidgets.QWidget):
    def __init__(self, main_window):
        super(SpaceScreen, self).__init__()
        self.main_window = main_window
        self.spaceID = None
        self.space = None
        self.layout = QtWidgets.QVBoxLayout(self)
        self.space_screen = QtWidgets.QWidget()
        self.setWindowTitle("Spaces")
        self.setFixedSize(400, 300)

        self.space_label = exp_label(self, "Space")
        self.space_textbox = exp_textbox(self)
        self.space_textbox.setValidator(NoSpecialCharactersValidator())
        self.spacetype_label = exp_label(self, "Space Type")
        self.spacetype_options = exp_combobox(self, ["managed", "shared"])
        self.tenantid_label = exp_label(self, "Tenant ID")
        self.tenantid_textbox = exp_textbox(self)
        self.tenantid_textbox.setValidator(NoSpecialCharactersValidator())
        self.btn_createspace = exp_btn_next(self, "Create Space")

        self.btn_createspace.clicked.connect(self.callback)
        self.btn_menu = exp_btn_back(self, "Back")
        self.btn_menu.setAutoDefault(True)
        self.btn_menu.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btn_menu.clicked.connect(self.back_mainwindow)

    def callback(self):
        confirm = confirm_dialog(self, "Continue?")
        if confirm == QtWidgets.QMessageBox.Yes:
            customer = self.space_textbox.text()
            self.space = self.space_textbox.text()  # Defina o valor do atributo space
            self.spacetype = self.spacetype_options.currentText()
            self.tenantID = self.tenantid_textbox.text()
            response = create_space(self.space, self.spacetype, self.tenantID)
            self.check_response(response)

    def check_response(self, response):
        status_description = config.get_status_description(response.status_code)
        if response and response.status_code == 201 or response.status_code == 204:
            response_json = response.json()
            self.spaceID = response_json.get("id")
            success_message(self, f"{self.space}-created".replace("-", "\n"))
            self.next_screen()
        else:
            response_content = response.content
            retorno_dict = json.loads(response_content)
            detail = retorno_dict['detail']
            error_message(self, f"{self.space}-{detail}".replace("-", "\n"))

    def next_screen(self):
        self.hide()
        self.conn_screen = ConnectionScreen(self.main_window, self.space, self.spacetype, self.spaceID, self.tenantID)
        self.conn_screen.show()

    def back_mainwindow(self):
        self.hide()
        self.main_window.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.btn_createspace.click()
        else:
            super().keyPressEvent(event)

class NoSpecialCharactersValidator(QtGui.QValidator):
    def validate(self, text, pos):
        # Verificar se há caracteres especiais no texto inserido
        for char in text:
            if char in string.punctuation or char.isspace():
                return (QtGui.QValidator.Invalid, text, pos)
        return (QtGui.QValidator.Acceptable, text, pos)

    def fixup(self, text):
        # Remover qualquer caractere especial do texto inserido
        cleaned_text = ''.join(char for char in text if char not in string.punctuation)
        return cleaned_text