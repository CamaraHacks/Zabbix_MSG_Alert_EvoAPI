import requests
import json
import time

reload_triggered = int(time.time()) - 300

def api_get_alerts(API_KEY, UNAME, PWORD, hostpf):
    req = requests.post(API_KEY, json={
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "username": UNAME,
            "password": PWORD,
        },
        "id": 1
        
    })
    AUTHTOKEN = req.json()["result"] 

    if "result" in req.json():
            print("\nLogin bem-sucedido!")
    else:
            print("\nErro ao logar:", req.json())





    
#Envia um post para a API verificando os triggers
    print("\nEfetuando a busca...")
    req = requests.post(API_KEY, json={
        "jsonrpc": "2.0",
        "method": "trigger.get",
        "params": {
            "withUnacknowledgedEvents": False,
            "lastChangeSince" : 'reload_triggered',
            "output": ["status", "hostid", "priority", "description"],
            "hostids": [hostpf],
            "filter": {"value": 1, "priority": [3, 4, 5]},
            "selectHosts": ["host", "hostsid"],
            "selectAcknowledges": "extend",
            "recent": "true",
            "sortorder": "severity",
        },
        "id": 2,
        "auth": AUTHTOKEN
    })

    with open('triggers.json', 'w', encoding='utf-8') as f:
        json.dump(req.json(), f, indent=4, ensure_ascii=False, sort_keys=True)

    # Logout user
    print("\nLogout user")
    req = requests.post(API_KEY, json={
        "jsonrpc": "2.0",
        "method": "user.logout",
        "params": {},
        "id": 2,
        "auth": AUTHTOKEN
    })


