import os
from dotenv import load_dotenv
data = any

load_dotenv()

def get_credentials():
    API_KEY = os.getenv('API_KEY')
    UNAME = os.getenv('user_name')
    PWORD = os.getenv('password')
    hostpf = os.getenv('HOST_PF')
    #file_loc = os.getenv('file_location') talvez passar o local para uma .env
    return API_KEY, UNAME, PWORD, hostpf


def alerta(host_name, description, triggerid):

    print(f"---------------------------------------")
    print(f"O host: {host_name} está com um alerta ativo ⚠️")
    print(f"Descrição do Alerta: {description}")
    print(f"Nível de Severidade: Alta, serviço fora do ar")
    print(f"Trigger ID: {triggerid}")


def get_off_hosts():
    hosts= []
    for host in data['result']:
        hosts.append(host)
    for host in hosts:
        if host.get('priority') == '4':
            description = host.get('description')
            host_name = host.get('hosts')[0].get('host') if host.get('hosts') else "Host não encontrado"
            triggerid = host.get('triggerid')        
            alerta(host_name, description, triggerid)

          



