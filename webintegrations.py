import config
from PySide6 import QtWidgets
from PySide6.QtWidgets import QMessageBox
from QlikAPI import  get_webintegrations, create_contentpolicy
from createwidgets import exp_textbox, exp_label,exp_btn_next
from alertmessage import error_message, success_message, confirm_dialog
from user import CreateUserScreen
import  json
from PySide6.QtCore import Qt
class WebIntegrationScreen(QtWidgets.QWidget):
    def __init__(self, main_window, tenantid, spacename):
        super(WebIntegrationScreen, self).__init__()
        self.main_window = main_window
        self.spacename = spacename
        self.tenantid = tenantid

        self.layout = QtWidgets.QVBoxLayout(self)

        self.conn_screen = QtWidgets.QWidget()
        self.setWindowTitle("Connections")
        self.setFixedSize(600, 400)

        self.customer_policy_label = exp_label(self, "Customer Policy")
        self.customer_policy_textbox = exp_textbox(self)
        self.customer_policy_textbox.setText(f"{self.spacename}")

        self.url_policy_label = exp_label(self, "URL Policy")
        self.url_policy_textbox = exp_textbox(self)
        self.url_policy_textbox.setText(f"{self.spacename}.cvortex.com")

        self.btn_createpolicies = exp_btn_next(self, "Create Policies")
        self.btn_createpolicies.clicked.connect(self.callback)

    def callback(self):
        confirm = confirm_dialog(self, "Continue?")
        if confirm == QMessageBox.Yes:
            self.customer_policy_textbox = self.customer_policy_textbox.text()
            self.url_policy_textbox = self.url_policy_textbox.text()
            response = get_webintegrations(self.tenantid, self.url_policy_textbox, self.customer_policy_textbox, self)
            self.check_response(response, 'webintegration')
            response = create_contentpolicy(self.customer_policy_textbox, self.url_policy_textbox, self)
            self.check_response(response, 'create policies')

    def check_response(self, response, method):
        status_description = config.get_status_description(response.status_code)
        if response and response.status_code == 201 or response.status_code == 204:
            success_message(self, f"{method}-{self.customer_policy_textbox}-updated...".replace("-", "\n"))
            self.next_screen()
        else:
            response_json = response.json()
            response_content = response.content
            retorno_dict = json.loads(response_content)
            print(response_content)
            detail = retorno_dict['detail']
            error_message(self, f"{self.customer_policy_textbox}-{detail}".replace("-", "\n"))

    def next_screen(self):
        self.hide()
        self.usr_screen = CreateUserScreen(self.main_window)
        self.usr_screen.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            self.btn_createpolicies.click()
        else:
            super().keyPressEvent(event)