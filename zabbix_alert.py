import requests
import json
import logging
from config import HOST_IDS

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def api_get_alerts(zabbix_api_url, username, password):
    """
    Authenticates with Zabbix API, fetches triggers, and returns the result.
    """
    session = requests.Session()
    headers = {'Content-Type': 'application/json-rpc'}
    
    # 1. Login
    login_payload = {
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
            "username": username,
            "password": password,
        },
        "id": 1
    }
    
    try:
        response = session.post(zabbix_api_url, json=login_payload, headers=headers)
        response.raise_for_status()
        login_data = response.json()
    except requests.RequestException as e:
        logging.error(f"Error connecting to Zabbix API: {e}")
        return []

    if "result" not in login_data:
        logging.error(f"Login failed: {login_data.get('error')}")
        return []
    
    auth_token = login_data["result"]
    logging.info("Login successful!")

    # 2. Get Triggers
    logging.info("Fetching triggers...")
    trigger_payload = {
        "jsonrpc": "2.0",
        "method": "trigger.get",
        "params": {
            "output": ["status", "hostid", "priority", "description", "triggerid"],
            "hostids": HOST_IDS,
            "filter": {"value": 1}, 
            "type": 1,
            "selectHosts": ["host"],
            "sortfield": "priority",
            "sortorder": "DESC"
        },
        "id": 2,
        "auth": auth_token
    }

    triggers = []
    try:
        response = session.post(zabbix_api_url, json=trigger_payload, headers=headers)
        response.raise_for_status()
        trigger_data = response.json()
        
        if "result" in trigger_data:
            triggers = trigger_data["result"]
        else:
            logging.error(f"Error fetching triggers: {trigger_data.get('error')}")

    except requests.RequestException as e:
        logging.error(f"Error fetching triggers: {e}")

    # 3. Logout
    logout_payload = {
        "jsonrpc": "2.0",
        "method": "user.logout",
        "params": {},
        "id": 3,
        "auth": auth_token
    }
    
    try:
        response = session.post(zabbix_api_url, json=logout_payload, headers=headers)
        logout_data = response.json()
        if "result" in logout_data:
            logging.info("Logout successful!")
        else:
            logging.warning(f"Logout failed: {logout_data}")
    except requests.RequestException as e:
        logging.warning(f"Error during logout: {e}")

    return triggers
