from config import get_credentials, alerta, get_hosts
from zabbix_alert import api_get_alerts
from whatsapp_sender import wpp_sender


def main():
    # Obtém as credenciais
    ZABBIX_API_URL, UNAME, PWORD, hostpf,url, phone_number, api_key = get_credentials()
    api_get_alerts(ZABBIX_API_URL, UNAME, PWORD, hostpf)
   
    # Obtém as informações dos hosts
    hosts = get_hosts()
    print("Hosts encontrados:", hosts)  # Debug output
    if not hosts:
        message = ("Nenhum host com prioridade '4' encontrado.")
        return
    for hostname, description, triggerid in hosts:
        message = alerta(hostname, description, triggerid)

        # Envia a mensagem para o WhatsApp
        
        wpp_sender(url, phone_number, api_key, message)
        print(f"Mensagem enviada para {hostname}: {message}")

if __name__ == "__main__":
    main()