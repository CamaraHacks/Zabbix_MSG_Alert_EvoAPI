import requests
import logging

def wpp_sender(url, phone_number, api_key, message):
    """
    Sends a message via WhatsApp API (EvoAPI).
    """
    if not message:
        logging.warning("No message provided for sending.")
        return False

    postData = {
        "number": phone_number,
        "text": message
    }

    headers = {
        "Content-Type": "application/json",
        "apikey": api_key
    }

    try:
        response = requests.post(url, json=postData, headers=headers, timeout=10) # Added timeout
        
        if response.status_code in (200, 201):
            logging.info(f"Message sent successfully to {phone_number}!")
            return True
        else:
            logging.error(f"Error sending message: {response.status_code}")
            logging.error(f"API Response: {response.text}")
            return False
            
    except requests.exceptions.RequestException as e:
        logging.error(f"Connection error sending message: {e}")
        return False
