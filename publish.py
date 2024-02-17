from PySide6 import QtWidgets
from functions import  publish_apps, publish_tasks
from alertmessage import error_message, success_message, confirm_dialog
from webintegrations import WebIntegrationScreen
import config
def publish_app_task(self, main_window, tenantid, spaceid, spacename):
    AppIDOrigin = config.ExtractApp
    AppDesc = AppIDOrigin
    NameApp = f"{spacename}-{tenantid}-{spacename}-Extraction Layer"
    response = publish_apps(AppIDOrigin, NameApp, tenantid, spaceid, spacename, AppDesc)
    json = response.json()
    AppID = json['attributes']['id']
    ByMinute = config.ExtractByMinute
    response = publish_tasks(AppID, ByMinute)
    if response and response.status_code == 201:
        success_message(self, f"Extraction Layer-created".replace("-", "\n"))
        AppIDOrigin = config.TransformApp
        AppDesc = "string"
        NameApp = f"{spacename}-{spacename}-Transform"
        response = publish_apps(AppIDOrigin, NameApp, tenantid, spaceid, spacename, AppDesc)
        json = response.json()
        AppID = json['attributes']['id']
        ByMinute = config.TransformByMinute
        response = publish_tasks(AppID, ByMinute)
        if response and response.status_code == 201:
            success_message(self, f"Transform Layer-created".replace("-", "\n"))
            AppIDOrigin = config.AnalyticsApp
            AppDesc = "string"
            NameApp = f"{spacename}-{spacename}-Analytics"
            response = publish_apps(AppIDOrigin, NameApp, tenantid, spaceid, spacename, AppDesc)
            json = response.json()
            AppID = json['attributes']['id']
            ByMinute = config.AnalyticsByMinute
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
