### ------------ Default Configs --------------
BASE_URL = "https://zv37sxsjfgn7hyt.us.qlikcloud.com/api/v1"
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJFUzM4NCIsImtpZCI6Ijk4MWI1MGZkLWFjZjgtNDU2ZS04MTE2LWQwOWJiY2ViN2VjZiIsInR5cCI6IkpXVCJ9.eyJzdWJUeXBlIjoidXNlciIsInRlbmFudElkIjoiN3Zqbk02UHQydXRmUlhsR2hnUVM4WFBWTTlKb2VlY3kiLCJqdGkiOiI5ODFiNTBmZC1hY2Y4LTQ1NmUtODExNi1kMDliYmNlYjdlY2YiLCJhdWQiOiJxbGlrLmFwaSIsImlzcyI6InFsaWsuYXBpL2FwaS1rZXlzIiwic3ViIjoiNjNjODQ1NDIwOGY2OThiMGE3NDE0YWVhIn0.dzFgNoL7pnF_TkkGWswr_53ZSituRqpmc1cVnzA0Exgr8_nUSTT8l8dIf_SNs1SRXkCbnpHhaEuFlfSD_XfMxiAkEsxgC_v6rgDDdJhWWP2wbxScC2FxxS_zw1aMPt9h'
}
### ------------ Connection Configs --------------
ip_default =  "34.95.163.64"
port_default = "5432"
db_default = "6230f2f5bd3a69548491bc37"

### ------------ Publish Apps Configs --------------
ExtractApp = "05731beb-9f3c-40aa-86fa-1e7aba7f31af"
TransformApp = "2bf225fd-2e04-434d-b3e1-18bbf97bbe2f"
AnalyticsApp = "d72a1d30-e9fa-4338-b4a2-349fd7526e42"

### ------------ Publish Tasks Configs --------------
freq = "HOURLY"
interval = 1
ExtractByMinute = "00"
TransformByMinute = "15"
AnalyticsByMinute = "20"

### ------------ Users Configs --------------
gs_mail = [
    "rodrigo.borges@cvortex.io",
    "gustavo.henrique@cvortex.io",
    "linique.santos@cvortex.io",
    "gilmar.oliveira@cvortex.io"
    ]

### ------------ Users Configs --------------
### - ThemeLight
color_themelight = "#F7F8FA"
color_onhover = "#FF8C00"
color_onhoverlight = "#FF8C00"
color_themedark = "#313131"
color_onhoverdark = "#FF8C00"