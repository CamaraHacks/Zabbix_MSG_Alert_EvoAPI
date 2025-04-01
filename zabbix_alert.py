import requests
import json
import time
from datetime import datetime


def api_get_alerts(ZABBIX_API_URL, UNAME, PWORD, hostpf):
    now = int(time.time())
    reload_triggered = int(time.time()) - 600
   
    req = requests.post(ZABBIX_API_URL, json={
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "username": UNAME,
            "password": PWORD,
        },
        "id": 1
    })
    
    # Verificando se o login foi bem-sucedido
    response = req.json()
    if "result" in response:
        AUTHTOKEN = response["result"]
        print("Login bem-sucedido!")
    else:
        print("Erro ao logar:", response)
        return  # Sai da função em caso de erro

    # Buscando os triggers
    print("Efetuando a busca...")
    req = requests.post(ZABBIX_API_URL, json={
        "jsonrpc": "2.0",
        "method": "trigger.get",
        "params": {
            "output": ["status", "hostid", "priority", "description"],
             "hostids": [
                11658, 11664, 12060, 12064, 12065, 12066, 12409, 12410, 12411, 12412, 12413, 
                12414, 12415, 12416, 12420, 12421, 12422, 12423, 12424, 12425, 
                12426, 12427, 12430, 12431, 12432, 12862, 12942, 13248, 13249, 13307, 13308, 
                13309, 13343, 13778, 13779, 13780, 13781, 13782, 13783, 13784, 13785, 13786, 
                13787, 13788, 13789, 13790, 13791, 13792, 13797,13798,13799,13800,13801,13802,13803
            ],
        "filter": {"value": 1}, 
        "type": 1,
        #"lastChangeSince": reload_triggered,
        #"lastChangeTill": now, 
        "selectHosts": ["host"],
        #"selectAcknowledges": ["acknowledgeid", "userid"],  
        "sortfield": "priority",  # Corrige ordenação
        "sortorder": "DESC"  # Ordena da maior para menor severidade
    },
    "id": 2,
    "auth": AUTHTOKEN
})

    # Salvando os dados retornados em um arquivo JSON
    with open('check_files/triggers.json', 'w', encoding='utf-8') as f:
        json.dump(req.json(), f, indent=4)

    # Logout user
    print("Logout user")
    req = requests.post(ZABBIX_API_URL, json={
        "jsonrpc": "2.0",
        "method": "user.logout",
        "params": {},
        "id": 3,  # Alterei o ID aqui para evitar duplicidade com o login
        "auth": AUTHTOKEN
    })

    # Verificando se o logout foi bem-sucedido
    logout_response = req.json()
    if "result" in logout_response:
        print("Logout bem-sucedido!")
        print(datetime.now())
    else:
        print("\nErro ao fazer logout:", logout_response)

