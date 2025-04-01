import requests

def wpp_sender(url, phone_number, api_key, message):
    if not message:
        print("Nenhuma mensagem fornecida para envio.")
        return

    postData = {
        "number": phone_number,
        "text": message
    }

    headers = {
        "Content-Type": "application/json",
        "apikey": api_key
    }

    try:
        response = requests.post(url, json=postData, headers=headers)
        
        if response.status_code in (200, 201):  # Aceita 200 e 201 como sucesso
            print(f"Mensagem enviada com sucesso!")
        else:
            print(f"Erro ao enviar mensagem: {response.status_code}")
            print("Resposta da API:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão ao enviar mensagem: {e}")