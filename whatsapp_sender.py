import json
import requests



def wpp_sender (mensagem):
    url = "http://localhost:8080/message/SendText/teste" # URL da Evolution API
    api_key = "8ecaf9e45f43-4721b34d3f74fa0bbc22"   # API Key da Evolution
    phone_number = "5513997936361"  # Número de telefone de destino
    mensagem = "Tr7!c4tch!3nt3r"


    postData = {
        "number": phone_number,
        "text": mensagem
    }

    headers = {
        "Content-Type": "application/json",
        "apikey": api_key
    }

    response = requests.post(url, json=postData, headers=headers)

    if response.status_code == 200:
        print("Mensagem enviada com sucesso!")
    else:
        print(f"Erro ao enviar mensagem: {response.status_code}")
        print("Resposta da API:", response.text)