import configparser
import os
import sys

### ------------ Default Configs --------------
BASE_URL = "https://zv37sxsjfgn7hyt.us.qlikcloud.com/api/v1"
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJFUzM4NCIsImtpZCI6Ijk4MWI1MGZkLWFjZjgtNDU2ZS04MTE2LWQwOWJiY2ViN2VjZiIsInR5cCI6IkpXVCJ9.eyJzdWJUeXBlIjoidXNlciIsInRlbmFudElkIjoiN3Zqbk02UHQydXRmUlhsR2hnUVM4WFBWTTlKb2VlY3kiLCJqdGkiOiI5ODFiNTBmZC1hY2Y4LTQ1NmUtODExNi1kMDliYmNlYjdlY2YiLCJhdWQiOiJxbGlrLmFwaSIsImlzcyI6InFsaWsuYXBpL2FwaS1rZXlzIiwic3ViIjoiNjNjODQ1NDIwOGY2OThiMGE3NDE0YWVhIn0.dzFgNoL7pnF_TkkGWswr_53ZSituRqpmc1cVnzA0Exgr8_nUSTT8l8dIf_SNs1SRXkCbnpHhaEuFlfSD_XfMxiAkEsxgC_v6rgDDdJhWWP2wbxScC2FxxS_zw1aMPt9h'
}


def resource_path(relative_path):
   try:
       base_path = sys._MEIPASS
   except Exception:
       base_path = os.path.abspath(".")

   return os.path.join(base_path, relative_path)


ini_file = resource_path("config.ini")
config = configparser.ConfigParser()
config.read(ini_file)

### ------------ Database Configs --------------
port_default = config['Database']['port_default']
ip_default = config['Database']['ip_default']
db_default = config['Database']['db_default']

### ------------ Publish Apps Configs --------------
ExtractApp = config['Publish']['ExtractApp']
TransformApp = config['Publish']['TransformApp']
AnalyticsApp = config['Publish']['AnalyticsApp']

### ------------ Publish Tasks Configs --------------
freq = config['Task']['freq']
interval = config['Task']['interval']
ExtractByMinute = config['Task']['ExtractByMinute']
TransformByMinute = config['Task']['ExtractByMinute']
AnalyticsByMinute = config['Task']['ExtractByMinute']

### ------------ Users Configs --------------
gs_mail = config['User']['gs_mail'].split(',')

### ------------ Users Configs --------------
### - ThemeLight
color_themelight = config['Theme']['color_themelight']
color_onhover = config['Theme']['color_onhover']
color_themedark = config['Theme']['color_themedark']
color_onhoverdark = config['Theme']['color_onhoverdark']
