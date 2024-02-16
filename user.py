import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout,  QPushButton, QHBoxLayout, QCheckBox, QMessageBox
from PySide6.QtCore import Qt
from QlikAPI import get_spaces_managed, get_user, get_space, update_spaceuser , create_user
from createwidgets import exp_textbox, exp_label, exp_combobox
from alertmessage import error_message, success_message, confirm_dialog
import json


class CreateUserScreen(QWidget):
    def __init__(self, main_window):
        super(CreateUserScreen, self).__init__()
        self.setWindowTitle("Create User")
        self.main_window = main_window
        self.setFixedSize(400, 440)

        self.layout = QVBoxLayout()
        self.user_dropdown_layout = QHBoxLayout()
        self.space_label = exp_label(self, "Space")
        self.user_dropdown_layout.addWidget(self.space_label)

        self.space_dropdown = exp_combobox(self, "[1,2]")
        self.space_dropdown.setEditable(True)
        self.space_dropdown.lineEdit().setFocus()
        self.user_dropdown_layout.addWidget(self.space_dropdown)

        self.checkbox_layout = QHBoxLayout()
        self.include_gs_checkbox = QCheckBox("Include GS")

        self.checkbox_layout.addWidget(self.include_gs_checkbox)
        self.layout.addLayout(self.checkbox_layout)
        self.layout.addLayout(self.user_dropdown_layout)

        self.uniqueid_label = exp_label(self,"Unique User ID")
        self.layout.addWidget(self.uniqueid_label)

        self.uniqueid_textbox = exp_textbox(self)
        self.uniqueid_textbox.setPlaceholderText("Unique ID")
        self.layout.addWidget(self.uniqueid_textbox)

        self.username_label = exp_label(self,"Name")
        self.layout.addWidget(self.username_label)

        self.username_textbox = exp_textbox(self)
        self.username_textbox.setPlaceholderText("Name user without spaces")
        self.layout.addWidget(self.username_textbox)

        self.button_layout = QHBoxLayout()
        self.create_button = QPushButton("Create User")
        self.create_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: #E0E0E0;
                border: 2px solid #4CAF50;
                border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            """)
        self.create_button.clicked.connect(self.callback)
        self.button_layout.addWidget(self.create_button)


        self.back_button = QPushButton("Back")
        self.back_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: #E0E0E0;
                border: 2px solid #2196F3;
                border-radius: 5px;
                padding: 5px 10px;
            }
            QPushButton:hover {
                background-color: #0b7dda;
            }
            """)
        self.back_button.clicked.connect(self.back_mainwindow)
        self.button_layout.addWidget(self.back_button)
        self.layout.addLayout(self.button_layout)
        self.space_dropdown.clear()
        self.setLayout(self.layout)
        self.populate_user_dropdown()

    def populate_user_dropdown(self):
        self.space_dropdown.addItem("Nenhum")
        spaces_response = get_spaces_managed()
        if spaces_response.status_code == 200:
            spaces_json = spaces_response.json()
            spaces = [space['name'] for space in spaces_json['data']]
            self.space_dropdown.addItems(spaces)

    def callback(self):
        confirm = confirm_dialog(self, "Continue?")
        if confirm == QMessageBox.Yes:
            space = self.space_dropdown.currentText()
            unique_id = self.uniqueid_textbox.text()
            username = self.username_textbox.text()
            include_gs = self.include_gs_checkbox.isChecked()
            spaceid = get_space(space)

            if username and unique_id:
                response = create_user(unique_id,username)
                self.check_response(response, unique_id, "created")
                user_id = get_user(unique_id)
                response = update_spaceuser(user_id,spaceid)
                self.check_response(response, unique_id, "updated")

            if include_gs:
                user_emails = ["rodrigo.borges@cvortex.io", "gustavo.henrique@cvortex.io", "linique.santos@cvortex.io", "gilmar.oliveira@cvortex.io"]
                for email in user_emails:
                    user_id = get_user(email)
                    response = update_spaceuser(user_id, spaceid)
                    self.check_response(response, email, "updated")
            self.uniqueid_textbox.clear()
            self.username_textbox.clear()

            if not include_gs and not username and not unique_id:
                error_message(self, 'Input a user or check include GS')


    def check_response(self, response, email, msgtext):
        if response is not None:
            if response.status_code == 201:
                success_message(self, f"{email}-{msgtext}".replace("-", "\n"))
            else:
                response_content = response.content
                retorno_dict = json.loads(response_content)
                detail = retorno_dict['detail']
                error_message(self, f"{email}-{detail}".replace("-", "\n"))

    def back_mainwindow(self):
        self.hide()
        self.main_window.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.create_button.click()
        else:
            super().keyPressEvent(event)
