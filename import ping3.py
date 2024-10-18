import ping3
import random
from ping3 import ping

# Definir os dispositivos e seus IPs
dispositivos = [
    {"nome": "Dispositivo A", "ip": "10.1.1.100"},
    {"nome": "Dispositivo B", "ip": "10.1.1.200"},
    {"nome": "Switch", "ip": "10.1.1.75"},
    {"nome": "Roteador", "ip": "10.1.0.75"},
    {"nome": "Servidor", "ip": "10.1.0.2"},
    {"nome": "Gateway", "ip": "10.1.0.1"}
]

# Escolher aleatoriamente um dispositivo que "não responderá"
dispositivo_inacessivel = random.choice(dispositivos)["ip"]

# Função para verificar a conectividade com um dispositivo
def verificar_conectividade(nome, ip):
    # Se for o dispositivo escolhido, simular que ele não está respondendo
    if ip == dispositivo_inacessivel:
        print(f"{nome} ({ip}) não está respondendo! (Simulado)")
        return

    # Testar a conectividade real
    resultado = ping(ip, timeout=2)
    if resultado:
        print(f"{nome} ({ip}) está respondendo.")
    else:
        print(f"{nome} ({ip}) não está respondendo!")

# Testar conectividade de todos os dispositivos
def testar_rede(dispositivos):
    print("Iniciando verificação da rede...")
    for dispositivo in dispositivos:
        nome = dispositivo["nome"]
        ip = dispositivo["ip"]
        verificar_conectividade(nome, ip)

# Executar a verificação da rede
if __name__ == "__main__":
    testar_rede(dispositivos)
