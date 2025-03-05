import requests

TOKEN = "????"  # Substitua pelo seu token
CHAT_ID = "????"  # Substitua pelo seu chat_id

def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    dados = {"chat_id": CHAT_ID, "text": mensagem}
    response = requests.post(url, data=dados)

    if response.status_code == 200:
        print("✅ Mensagem enviada com sucesso!")
    else:
        print(f"❌ Erro ao enviar mensagem: {response.text}")

# Testando envio
enviar_telegram("Olá! Seu bot está funcionando! 🚀")
