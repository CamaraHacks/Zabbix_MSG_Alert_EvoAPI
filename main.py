
from config import get_credentials, alerta, get_off_hosts
from zabbix_alert import api_get_alerts
import json
from whatsapp_sender import wpp_sender


API_KEY, UNAME, PWORD, hostpf = get_credentials()

api_get_alerts(API_KEY, UNAME, PWORD, hostpf)

with open(r'local\triggers.json', 'r') as f:
    data = json.load(f)

get_off_hosts()
wpp_sender(alerta()) 





def __init__(main):
    main()