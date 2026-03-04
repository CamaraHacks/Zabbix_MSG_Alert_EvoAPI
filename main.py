import logging
from config import get_credentials, format_alert_message, PRIORITY_THRESHOLD, IGNORED_HOSTS
from zabbix_alert import api_get_alerts
from whatsapp_sender import wpp_sender

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    # Obtém as credenciais
    ZABBIX_API_URL, UNAME, PWORD, _, url, phone_number, api_key = get_credentials()
    
    # Busca alertas diretamente da API
    triggers = api_get_alerts(ZABBIX_API_URL, UNAME, PWORD)
   
    if not triggers:
        logging.info("Nenhum trigger retornado ou erro na conexão.")
        return

    logging.info(f"Analisando {len(triggers)} triggers...")

    alerts_sent = 0
    for trigger in triggers:
        # Verifica prioridade
        try:
            priority = int(trigger.get('priority', 0))
        except ValueError:
            priority = 0
            
        if priority == PRIORITY_THRESHOLD:
            # Extrai nome do host
            hosts = trigger.get('hosts', [])
            host_name = hosts[0].get('host') if hosts else "Host Desconhecido"
            
            # Verifica se host deve ser ignorado
            if host_name in IGNORED_HOSTS:
                continue
                
            description = trigger.get('description')
            triggerid = trigger.get('triggerid')
            
            message = format_alert_message(host_name, description, triggerid)

            # Envia a mensagem para o WhatsApp
            if message:
                wpp_sender(url, phone_number, api_key, message)
                logging.info(f"Mensagem enviada para {host_name}: {message.splitlines()[0]}...")
                alerts_sent += 1
    
    if alerts_sent == 0:
        logging.info("Nenhum alerta de alta prioridade encontrado para envio.")

if __name__ == "__main__":
    main()