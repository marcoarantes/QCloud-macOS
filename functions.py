import requests
import config
import sys
import os.path
import http.client

def create_space(costumer, spacetype, tenantid):
    url = config.BASE_URL + "/spaces"
    headers = config.HEADERS
    data = {
        "name": costumer,
        "type": spacetype,
        "description": tenantid
    }
    response = requests.post(url, headers=headers, json=data)
    response_code = response.status_code
    response_desc = get_status_description(response_code)
    print("Create Space... ", response, '-', response_desc)
    return response


def get_connectionDefault(hostname, port, tenantID):
    url = config.BASE_URL + "/data-connections/f1970e97-cee5-48b6-8fce-ed66278875cd"
    headers = config.HEADERS
    response = requests.get(url, headers=headers)
    response_code = response.status_code
    response_desc = get_status_description(response_code)
    print("Get connection template... - ", response, '-', response_desc)
    response = response.json()
    qConnectTemp = response['qConnectStatement']
    hostname_default = config.ip_default
    port_default = config.port_default
    db_default = config.db_default
    response = qConnectTemp.replace(hostname_default, hostname).replace(port_default, port).replace(db_default,
                                                                                                    tenantID)
    return response


def create_connection(tenantID, connection, username, password, hostname, port, spaceID, customer):
    url = config.BASE_URL + "/data-connections"
    headers = config.HEADERS
    qConnectStatement = get_connectionDefault(hostname, port, tenantID)

    data = {
        "qName": f"{connection}",
        "qType": "QvOdbcConnectorPackage.exe",
        "space": spaceID,  # Usar o space_id fornecido
        "qLogOn": "1",
        "qPassword": f"{password}",
        "qUsername": f"usr_{tenantID}",
        "datasourceID": "postgres",
        "qArchitecture": 0,
        "qConnectStatement": qConnectStatement.replace("!", "\\"),
        "qSeparateCredentials": True,
        "qCredentialsName": f"usr_postgre_{customer}_{tenantID}"

    }
    response = requests.post(url, headers=headers, json=data)
    response_code = response.status_code
    response_json = response.json()
    response_desc = get_status_description(response_code)
    print("Create connection... - ", response, '-', response_desc)
    return response


def publish_apps(AppIDOrigin, NameApp, tenantID, spaceID, costumer, description):
    # ======================= Publish App ===============================
    url = config.BASE_URL + f"/apps/{AppIDOrigin}/publish"
    headers = config.HEADERS

    data = {
        "data": "target",
        "moveApp": False,
        "spaceId": f"{spaceID}",
        "attributes": {
            "name": f"{NameApp}",
            "description": f"{AppIDOrigin}"
        },
        "originAppId": f"{AppIDOrigin}"
    }
    response = requests.post(url, headers=headers, json=data)
    response_code = response.status_code
    response_desc = get_status_description(response_code)
    print("Publish apps...", response, '-', response_desc)
    return response


def publish_tasks(AppID, ByMinute):
    # ======================= Publish App ===============================
    url = config.BASE_URL + "/reload-tasks"
    headers = config.HEADERS

    data = {
        "appId": f"{AppID}",
        "partial": False,
        "timeZone": "America/Sao_Paulo",
        "autoReload": False,
        "recurrence": [
            f"RRULE:FREQ={config.freq};INTERVAL={config.interval};BYMINUTE={ByMinute};BYSECOND=0"
        ],
        "startDateTime": "2022-09-19T11:18:00",
        "autoReloadPartial": False
    }
    response = requests.post(url, headers=headers, json=data)
    response_code = response.status_code
    response_desc = get_status_description(response_code)
    print("Publish tasks...", response, '-', response_desc)
    return response


def get_webintegrations(tenantID, urlPolicy, customer, self):
    # ======================= Publish App ===============================
    url = config.BASE_URL + "/web-integrations/obUmJejDExihU1RjCxjo9rHwP0O3sJbT"
    headers = config.HEADERS
    urlPolicyHttps = "https://" + urlPolicy
    try:
        response = requests.get(url, headers=headers)
        response_code = response.status_code
        response_desc = get_status_description(response_code)
        print("Get list webs...", response, '-', response_desc)
        response_json = response.json()
        response_data = response_json['validOrigins']
        response_Webname = response_json['name']
        response_data.append(f"{urlPolicyHttps}")
        response_lista = response_data
        response = pacth_webintegrations(tenantID, response_Webname, response_lista, urlPolicy, customer, self)
        print(response)
        return response
    except requests.exceptions.JSONDecodeError as e:
        print("JSONDecodeError:", e)
        print("Response content:", response.content)
        return []


def pacth_webintegrations(tenantID, response_Webname, response_lista, urlPolicy, customer, self):
    # ======================= Publish App ===============================
    WebIntegrationID = "obUmJejDExihU1RjCxjo9rHwP0O3sJbT"
    url = config.BASE_URL + f"/web-integrations/{WebIntegrationID}"
    print(response_lista)
    headers = config.HEADERS
    data = [
        {
            "op": "replace",
            "path": "/validOrigins",
            "value": response_lista
        }
    ]

    response = requests.patch(url, headers=headers, json=data)
    response_code = response.status_code
    response_desc = get_status_description(response_code)
    print("Updated list of webs...", response, '-', response_desc)
    return response


def create_contentpolicy(customer, urlPolicy, self):
    # ======================= Publish App ===============================
    url = config.BASE_URL + "/csp-origins"
    headers = config.HEADERS
    false = 'false'
    true = 'true'
    data = {
        "name": f"{customer}",
        "imgSrc": False,
        "origin": f"{urlPolicy}",
        "fontSrc": False,
        "childSrc": False,
        "frameSrc": False,
        "mediaSrc": False,
        "styleSrc": False,
        "objectSrc": False,
        "scriptSrc": False,
        "workerSrc": False,
        "connectSrc": False,
        "formAction": False,
        "connectSrcWSS": False,
        "frameAncestors": True
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response_code = response.status_code
        response_desc = get_status_description(response_code)
        print("Create url policies...", response, '-', response_desc)
        return response
    except requests.exceptions.JSONDecodeError as e:
        print("JSONDecodeError:", e)
        print("Response content:", response.content)
        return []


def create_user(login, username):
    # ======================= Publish App ==============================
    user_exists = get_user(login)
    if user_exists == 0:
        url = config.BASE_URL + "/users"
        headers = config.HEADERS
        username_space = username.replace(' ', '')
        data = {
            "name": f"{username_space}",
            "email": f"{login}",
            "status": "active",
            "subject": f"{login}"
        }
        try:
            response = requests.post(url, headers=headers, json=data)
            response_code = response.status_code
            response_desc = get_status_description(response_code)
            print("Create user...", response, '-', response_desc)
            return response
        except requests.exceptions.JSONDecodeError as e:
            print("JSONDecodeError:", e)
            print("Response content:", response.content)
            return response


def update_spaceuser(response_user, spaceID):
    # ======================= Publish App ===============================
    url = config.BASE_URL + f"/spaces/{spaceID}/assignments"
    headers = config.HEADERS
    data = {
        "type": "user",
        "roles": [
            "consumer",
            "dataconsumer",
        ],
        "assigneeId": f"{response_user}"
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response_code = response.status_code
        response_desc = get_status_description(response_code)
        print("Update user access into space...", response, '-', response_desc)
        return response
    except requests.exceptions.JSONDecodeError as e:
        print("JSONDecodeError:", e)
        print("Response content:", response.content)
        return response

def get_user(login):
    # ======================= Publish App ===============================
    url = config.BASE_URL + "/users/actions/filter"
    headers = config.HEADERS

    # Crie o corpo da solicitação com o filtro desejado
    data = {
        "filter": f"(email eq \"{login}\")"
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response_code = response.status_code
        response_desc = get_status_description(response_code)
        response_json = response.json()
        if 'data' in response_json:
            users_list = response_json['data']
            if users_list:
                user_id = users_list[0]['id']
                return user_id
        return 0
    except requests.exceptions.JSONDecodeError as e:
        print("JSONDecodeError:", e)
        print("Response content:", response.content)
        return 0

def get_space(spacename):
    url = config.BASE_URL + f"/spaces?name={spacename}&limit=100"
    headers = config.HEADERS
    try:
        response = requests.get(url, headers=headers)
        response_code = response.status_code
        response_desc = get_status_description(response_code)
        response_json = response.json()
        if 'data' in response_json:
            space_list = response_json['data']
            if space_list:
                space_id = space_list[0]['id']
                return space_id
        return 0
    except requests.exceptions.JSONDecodeError as e:
        print("JSONDecodeError:", e)
        print("Response content:", response.content)
        return 0

def get_spaces_managed():
    url = config.BASE_URL + "/spaces?type=managed&limit=100"
    headers = config.HEADERS
    try:
        response = requests.get(url, headers=headers)
        response_json = response.json()
        response_code = response.status_code

        spaces = [space['name'] for space in response_json['data']]
        return response
    except requests.exceptions.JSONDecodeError as e:
        print("JSONDecodeError:", e)
        print("Response content:", response.content)
        return []

def resource_path(relative_path):
   try:
       base_path = sys._MEIPASS
   except Exception:
       base_path = os.path.abspath(".")

   return os.path.join(base_path, relative_path)
def get_status_description(status_code):
    return http.client.responses.get(status_code, 'Unknown')