from PySide6.QtGui import QIcon
import config
from PySide6 import QtWidgets, QtGui
from functions import create_connection, resource_path
from createwidgets import exp_textbox, exp_label,  exp_btn_next
from alertmessage import error_message, success_message, confirm_dialog
from publish import publish_app_task
import json
from PySide6.QtCore import Qt



class ConnectionScreen(QtWidgets.QWidget):
    def __init__(self, main_window, spacename, spacetype, spaceid, tenantid):
        super(ConnectionScreen, self).__init__()
        self.main_window = main_window
        self.spacename = spacename
        self.spaceid = spaceid
        self.tenantid = tenantid
        self.spacetype = spacetype
        self.layout = QtWidgets.QVBoxLayout(self)
        self.connscrn = self.layout
        self.conn_screen = QtWidgets.QWidget()
        self.setWindowTitle("Connections")
        self.setFixedSize(600, 400)
        image_path = resource_path("assets/QCloud.ico")
        icon = QtGui.QIcon(image_path)
        self.setWindowIcon(QIcon(icon))

        self.connection_label = exp_label(self, "Connection Name")
        self.connection_textbox = exp_textbox(self)
        self.connection_textbox.setText(f"PostgreSQL_{self.spacename}")

        self.dbusr_label = exp_label(self, "User")
        self.dbusr_textbox = exp_textbox(self)
        self.dbusr_textbox.setText(f"usr_{self.tenantid}")

        self.dbpw_label = exp_label(self, "Password")
        self.dbpw_textbox = exp_textbox(self)
        self.dbpw_textbox.setEchoMode(QtWidgets.QLineEdit.Password)

        self.serverip_label = exp_label(self, "Server")
        self.serverip_textbox = exp_textbox(self)
        self.serverip_textbox.setText(f"{config.ip_default}")

        self.serverport_label = exp_label(self, "Port")
        self.serverport_textbox = exp_textbox(self)
        self.serverport_textbox.setText(f"{config.port_default}")

        self.btn_createconnection = exp_btn_next(self, "Create Connection")
        self.btn_createconnection.clicked.connect(self.callback)

    def callback(self):
            confirm = confirm_dialog(self, "Continue?")
            if confirm == QtWidgets.QMessageBox.Yes:
                response = create_connection(self.tenantid, self.connection_textbox.text(), self.dbusr_textbox.text(),
                                             self.dbpw_textbox.text(),
                                             self.serverip_textbox.text(), self.serverport_textbox.text(), self.spaceid,
                                             self.spacename)
                self.connection_check_response(response)

    def connection_check_response(self, response):
            if response and response.status_code == 201:
                success_message(self, f"Connections-{self.connection_textbox.text()}-created".replace("-", "\n"))
                publish_app_task(self, self.main_window, self.tenantid, self.spaceid, self.spacename)
            else:
                response_content = response.content
                retorno_dict = json.loads(response_content)
                detail = retorno_dict['detail']
                error_message(self, f"{self.connection_textbox.text()}-{detail}".replace("-", "\n"))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.btn_createconnection.click()
        else:
            super().keyPressEvent(event)