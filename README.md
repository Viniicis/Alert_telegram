# 📂 Monitoramento de Arquivos .ENV com Alerta via Telegram  

Este script monitora uma pasta específica e verifica a quantidade de arquivos `.ENV`. Se o número de arquivos ultrapassar um limite definido, ele envia um alerta via Telegram para notificar os responsáveis.  

## 🚀 Funcionalidades  

- 📌 **Monitoramento automático** de arquivos `.ENV` em uma pasta especificada.  
- 🔔 **Envio de alerta para o Telegram** caso a quantidade de arquivos ultrapasse o limite configurado.  
- 🔄 **Verificação periódica** a cada 5 minutos (configurável).

🔧 Configuração
Defina a pasta a ser monitorada:
No código, altere a variável PASTA_MONITORADA para o caminho correto da pasta que deseja monitorar.

Configure o alerta no Telegram:

Substitua "????" pelo TOKEN do seu bot do Telegram na variável TOKEN.
Substitua "-?????" pelo CHAT_ID do grupo ou usuário que receberá as mensagens.
Ajuste o limite de arquivos:

Modifique a variável LIMITE_ARQUIVOS para definir o número máximo de arquivos .ENV antes de disparar o alerta.
![image](https://github.com/user-attachments/assets/fd80869b-bdae-4a87-bec9-f9e3909e0f7b)
