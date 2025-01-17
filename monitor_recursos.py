import psutil
import time

def monitorando_recursos():
    horario = time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())
    cpu = psutil.cpu_percent(interval=1)
    memoria_RAM = psutil.virtual_memory().percent
    memoria_disco = psutil.disk_usage('/').percent
    quantidade_processos_ativos = len(psutil.pids())

    recursos_usados = f"\n{horario} \n| CPU - {cpu}% \n| RAM - {memoria_RAM}% \n| Uso do Disco - {memoria_disco}% \n| Processos ativos - {quantidade_processos_ativos}"
    print(recursos_usados)

while True:
    monitorando_recursos()

    sair = input("\nDigite 1 para realizar uma nova leitura ou "
                 "qualquer outra tecla para sair.\n")
    
    if sair != '1':
        print("Encerrando programa.")
        break