# Zabbix MSG Alert EvoAPI 🚀

Este projeto integra o sistema de monitoramento **Zabbix** com a **EvoAPI** (WhatsApp) para o envio automatizado de alertas críticos de infraestrutura.

## 🛠️ Funcionalidades

- **Monitoramento em Tempo Real:** Busca triggers ativos diretamente via JSON-RPC API do Zabbix.
- **Filtragem Inteligente:** Filtra alertas por prioridade (ex: Alta/Desastre) e permite ignorar hosts específicos (whitelist/blacklist).
- **Notificação Instantânea:** Envia mensagens formatadas via WhatsApp utilizando a EvoAPI.
- **Robustez:** Implementação com tratamento de erros, timeouts de conexão e logs detalhados.

## 📋 Pré-requisitos

- Python 3.8+
- Acesso à API do Zabbix (URL, usuário e senha).
- Instância da EvoAPI configurada com uma API Key válida.
- Bibliotecas Python necessárias (instaláveis via `pip`).

## ⚙️ Configuração

1.  **Instale as dependências:**
    ```bash
    pip install requests python-dotenv
    ```

2.  **Configure as variáveis de ambiente:**
    Copie o arquivo de exemplo e preencha com suas credenciais:
    ```bash
    cp .env.example .env
    ```

3.  **Ajuste os Hosts e IDs:**
    No arquivo `config.py`, você pode personalizar:
    - `HOST_IDS`: Lista de IDs de hosts que deseja monitorar.
    - `IGNORED_HOSTS`: Lista de nomes de hosts que não devem disparar alertas.
    - `PRIORITY_THRESHOLD`: Nível de severidade mínima para o alerta (padrão: 4 - Alta).

## 🚀 Como Executar

Para iniciar o monitoramento e envio de alertas, execute o script principal:

```bash
python main.py
```

## 📂 Estrutura do Projeto

- `main.py`: Orquestrador principal do fluxo de execução.
- `zabbix_alert.py`: Módulo de comunicação com a API do Zabbix.
- `whatsapp_sender.py`: Módulo de integração com a EvoAPI.
- `config.py`: Centralização de constantes, filtros e formatação de mensagens.
- `.env`: Armazenamento seguro de credenciais sensíveis (não versionado).

## 📝 Licença

Este projeto é destinado a uso interno e monitoramento de NOC. Sinta-se à vontade para adaptar conforme sua infraestrutura.
