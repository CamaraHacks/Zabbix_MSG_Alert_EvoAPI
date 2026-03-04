import os
from dotenv import load_dotenv

load_dotenv()

def get_credentials():
    ZABBIX_API_URL = os.getenv('ZABBIX_API_URL')
    UNAME = os.getenv('UNAME')
    PWORD = os.getenv('PWORD')
    hostpf = os.getenv('hostpf')
    url = os.getenv('url') 
    api_key = os.getenv('api') 
    phone_number = os.getenv('phone')

    return ZABBIX_API_URL, UNAME, PWORD, hostpf, url, phone_number, api_key 

# Configuration Constants
HOST_IDS = [
    11658, 11664, 12060, 12064, 12065, 12066, 12409, 12410, 12411, 12412, 12413, 
    12414, 12415, 12416, 12420, 12421, 12422, 12423, 12424, 12425, 
    12426, 12427, 12430, 12431, 12432, 12862, 12942, 13248, 13249, 13307, 13308, 
    13309, 13343, 13778, 13779, 13780, 13781, 13782, 13783, 13784, 13785, 13786, 
    13787, 13788, 13789, 13790, 13791, 13792, 13797, 13798, 13799, 13800, 13801, 13802, 13803
]

IGNORED_HOSTS = ['rumoall-gja-hafw-1', 'rumoall-stsp-hafw-1', 'CS_RUPOR_ACP_01']

PRIORITY_THRESHOLD = 4

def format_alert_message(host_name, description, triggerid):
    if host_name and description and triggerid:
        return f"O host: {host_name} está com um alerta ativo ⚠️\nDescrição do Alerta: {description}\nNível de Severidade: Alta, serviço fora do ar\nTrigger ID: {triggerid}"
    else:
        return "Erro: Dados do alerta não estão completos."
    