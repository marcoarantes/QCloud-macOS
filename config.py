import psycopg2
import configparser
import os
import sys

### ------------ Default Configs --------------
BASE_URL = "https://zv37sxsjfgn7hyt.us.qlikcloud.com/api/v1"
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJFUzM4NCIsImtpZCI6Ijk4MWI1MGZkLWFjZjgtNDU2ZS04MTE2LWQwOWJiY2ViN2VjZiIsInR5cCI6IkpXVCJ9.eyJzdWJUeXBlIjoidXNlciIsInRlbmFudElkIjoiN3Zqbk02UHQydXRmUlhsR2hnUVM4WFBWTTlKb2VlY3kiLCJqdGkiOiI5ODFiNTBmZC1hY2Y4LTQ1NmUtODExNi1kMDliYmNlYjdlY2YiLCJhdWQiOiJxbGlrLmFwaSIsImlzcyI6InFsaWsuYXBpL2FwaS1rZXlzIiwic3ViIjoiNjNjODQ1NDIwOGY2OThiMGE3NDE0YWVhIn0.dzFgNoL7pnF_TkkGWswr_53ZSituRqpmc1cVnzA0Exgr8_nUSTT8l8dIf_SNs1SRXkCbnpHhaEuFlfSD_XfMxiAkEsxgC_v6rgDDdJhWWP2wbxScC2FxxS_zw1aMPt9h'
}
try:
    # Conectar ao banco de dados
    conn = psycopg2.connect(
        dbname="productanalytics",
        user="usr_qlik",
        password="p_egO$U#9A93aTl",
        host="34.95.231.8"
    )

    cursor = conn.cursor()

    # Executar a consulta SQL
    cursor.execute("SELECT id, \"type\", value FROM public.tb_paramns_config")

    # Criar um dicionário para armazenar os parâmetros
    parametros = {}

    # Preencher o dicionário com os parâmetros da consulta
    for row in cursor.fetchall():
        parametro = row[1]
        valor = row[2]
        parametros[parametro] = valor

    # Exibir os parâmetros salvos no dicionário
    print("Parâmetros disponíveis:")
    for parametro, valor in parametros.items():
        print(f"{parametro}: {valor}")

    # Agora você pode acessar os parâmetros como variáveis no dicionário 'parametros'
    ExtractApp = parametros['ExtractApp']
    TransformApp = parametros['TransformApp']
    AnalyticsApp = parametros['AnalyticsApp']
    freq = parametros['freq']
    interval = parametros['interval']
    ExtractByMinute = parametros['ExtractByMinute']
    TransformByMinute = parametros['TransformByMinute']
    AnalyticsByMinute = parametros['AnalyticsByMinute']
    color_themelight = parametros['color_themelight']
    color_onhover = parametros['color_onhover']
    color_onhoverlight = parametros['color_onhoverlight']
    color_themedark = parametros['color_themedark']
    color_onhoverdark = parametros['color_onhoverdark']
    ip_default = parametros['ip_default']
    port_default = parametros['port_default']
    db_default = parametros['db_default']
    print("Status da conexão: Conexão bem-sucedida")

    cursor.execute("SELECT email FROM tb_service_manager")
    gs_mail = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    print(gs_mail)
except (Exception, psycopg2.Error) as error:
    print("Status da conexão: Falha ao conectar ao banco de dados")
    print(error)
