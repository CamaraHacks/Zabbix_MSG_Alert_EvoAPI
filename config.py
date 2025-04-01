import json
from dotenv import load_dotenv
import os

load_dotenv()
def get_credentials():
    ZABBIX_API_URL= os.getenv('ZABBIX_API_URL')
    UNAME= os.getenv('UNAME')
    PWORD= os.getenv('PWORD')
    hostpf = os.getenv('hostpf')
    url= os.getenv('url') 
    api_key= os.getenv('api') 
    phone_number= os.getenv('phone')

    return ZABBIX_API_URL, UNAME, PWORD, hostpf, url, phone_number, api_key 


def alerta(host_name, description, triggerid):
    if host_name and description and triggerid:
        return f"O host: {host_name} está com um alerta ativo ⚠️\nDescrição do Alerta: {description}\nNível de Severidade: Alta, serviço fora do ar\nTrigger ID: {triggerid}"
    else:
        return "Erro: Dados do alerta não estão completos."

def get_hosts():
    
    with open('/home/user0/Documentos/Zabbix_Trigger_Alert/NOC_FIPS_engine/check_files/triggers.json', 'r') as f:
        data = json.load(f)
    ignored_items = ['rumoall-gja-hafw-1', 'rumoall-stsp-hafw-1', 'CS_RUPOR_ACP_01']  
    hosts = []  # Lista para armazenar hosts com prioridade '4'
    for host in data['result']:
        if host.get('priority') == 4:
            host_name = host.get('hosts')[0] if host.get('hosts') else "Host não encontrado"
            if host_name not in ignored_items:
                description = host.get('description')
                triggerid = host.get('triggerid')
                hosts.append((host_name, description, triggerid))
            
            
    return hosts





""" usar uma função que receba esses parametros filtrados e emita somente o necessário
print(f"---------------------------------------")
print(f"O host:{hosts[1].get('hosts')[0].get('host')} está com um alerta ativo ⚠️")
print(f"Descrição do Alerta: {hosts[1].get('description')}")
print(f"Nível de Severidade: {hosts[1].get('priority')}")
print(f"Status: {hosts[1].get('status')}")
print(f"Trigger ID: {hosts[1].get('triggerid')}") """
    