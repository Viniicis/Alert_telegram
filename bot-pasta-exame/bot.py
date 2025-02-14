import os
import shutil
import time

# Configurações
diretorio_monitorado = r"\\192.168.1.5\pedidos\Atria_volta"
diretorio_secundario = r"\\192.168.1.5\pedidos\Atria Volta_Hem"
limite_arquivos = 110
intervalo_verificacao = 10

def monitorar_pasta():
    while True:
        resultados = [f for f in os.listdir(diretorio_monitorado) if f.endswith(".ENV")]
        
        if len(resultados) > limite_arquivos:
            quantidade_mover = len(resultados) // 2
            arquivos_para_mover = resultados[:quantidade_mover]
            
            for arquivo in arquivos_para_mover:
                origem = os.path.join(diretorio_monitorado, arquivo)
                destino = os.path.join(diretorio_secundario, arquivo)
                shutil.move(origem, destino)
                print(f"Movido: {arquivo} para {diretorio_secundario}")
        
        time.sleep(intervalo_verificacao)

if __name__ == "__main__":
    if not os.path.exists(diretorio_secundario):
        os.makedirs(diretorio_secundario)
    print("Monitorando pasta... Pressione Ctrl+C para interromper.")
    monitorar_pasta()
