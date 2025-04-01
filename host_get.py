import requests, json
from dotenv import load_dotenv
from config import get_credentials

ZABBIX_API_URL, UNAME, PWORD, hostpf,url, api, phone = get_credentials()

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
    print("\nLogin bem-sucedido!")
else:
    print("\nErro ao logar:", response)
  

# Buscando os triggers
print("\nEfetuando a busca...")
req = requests.post(ZABBIX_API_URL, json={
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": ["name","status", "hostid"],
        "selectAcknowledges": "extend",
        "recent": "true",
        "sortorder": "severity",
    },
    "id": 2,
    "auth": AUTHTOKEN
})

# Salvando os dados retornados em um arquivo JSON
with open('host_list.json', 'w', encoding='utf-8') as f:
    json.dump(req.json(), f, indent=4)

# Logout user
print("\nLogout user")
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
    print("\nLogout bem-sucedido!")
else:
    print("\nErro ao fazer logout:", logout_response)