import os
import time
import requests

# Configurações
PASTA_MONITORADA = r"\\192.168.1.5\pedidos\Atria_volta"
LIMITE_ARQUIVOS = 100
TOKEN = "7726313493:AAGClqu1-CfU_1LyFTe97yR7154YZHsy5rI"  # Substitua pelo seu token
CHAT_ID = "-1002305832512"  # Substitua pelo seu chat_id

def enviar_telegram(mensagem):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    dados = {"chat_id": CHAT_ID, "text": mensagem}
    requests.post(url, data=dados)

while True:
    # Filtrando apenas arquivos com extensão .env
    arquivos_env = [f for f in os.listdir(PASTA_MONITORADA) if f.endswith(".ENV")]
    qtd_arquivos_env = len(arquivos_env)  # Contando apenas os arquivos .env
    print(f"Arquivos .env na pasta: {qtd_arquivos_env}")

    if qtd_arquivos_env >= LIMITE_ARQUIVOS:
        ##enviar_telegram(f"⚠️ Alerta: A pasta excedeu o limite de arquivos .env! \n Total de {qtd_arquivos_env} arquivos .env na pasta!")
        mensagem_aleatoria = f"""
⚠️  Robô Alerta!

🚨 A pasta monitorada esta com acúmulo de arquivos !! 🚨
-------------------------------------------------------------
📁 Arquivos acumulados = {qtd_arquivos_env} ❗
-------------------------------------------------------------

🤖 Ação recomendada: Verifique o funcionamento do robô de integração!
"""
        enviar_telegram(mensagem_aleatoria)


    time.sleep(300)  # Verifica a cada 5 segundos
