from PySide6 import QtWidgets
from QlikAPI import  publish_apps, publish_tasks
from alertmessage import error_message, success_message, confirm_dialog
from webintegrations import WebIntegrationScreen

def publish_app_task(self, main_window, tenantid, spaceid, spacename):
    confirm = confirm_dialog(self, "Publish and create tasks?")
    if confirm == QtWidgets.QMessageBox.Yes:
        AppIDOrigin = "05731beb-9f3c-40aa-86fa-1e7aba7f31af"
        AppDesc = AppIDOrigin
        NameApp = f"{spacename}-{tenantid}-{spacename}-Extraction Layer"
        response = publish_apps(AppIDOrigin, NameApp, tenantid, spaceid, spacename, AppDesc)
        json = response.json()
        AppID = json['attributes']['id']
        ByMinute = "00"
        response = publish_tasks(AppID, ByMinute)
        if response and response.status_code == 201:
            success_message(self, f"Extraction Layer-created".replace("-", "\n"))
            AppIDOrigin = "2bf225fd-2e04-434d-b3e1-18bbf97bbe2f"
            AppDesc = "string"
            NameApp = f"{spacename}-{spacename}-Transform"
            response = publish_apps(AppIDOrigin, NameApp, tenantid, spaceid, spacename, AppDesc)
            json = response.json()
            AppID = json['attributes']['id']
            ByMinute = "15"
            response = publish_tasks(AppID, ByMinute)
            if response and response.status_code == 201:
                success_message(self, f"Transform Layer-created".replace("-", "\n"))
                AppIDOrigin = "d72a1d30-e9fa-4338-b4a2-349fd7526e42"
                AppDesc = "string"
                NameApp = f"{spacename}-{spacename}-Analytics"
                response = publish_apps(AppIDOrigin, NameApp, tenantid, spaceid, spacename, AppDesc)
                json = response.json()
                AppID = json['attributes']['id']
                ByMinute = "20"
                response = publish_tasks(AppID, ByMinute)
                if response and response.status_code == 201:
                    success_message(self, f"Analytics Layer-created".replace("-", "\n"))
                    next_screen(self,self.main_window, tenantid, spacename)

            else:
                response_content = response.content
                retorno_dict = json.loads(response_content)
                detail = retorno_dict['detail']
                error_message(self, f"{NameApp}-{detail}".replace("-", "\n"))


def next_screen(self,main_window, tenantid, spacename):
        self.main_window = main_window
        self.hide()
        self.web_screnn = WebIntegrationScreen(main_window, tenantid, spacename)
        self.web_screnn.show()
