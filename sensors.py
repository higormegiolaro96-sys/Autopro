print("--- SISTEMA DE MONITORAMENTO INDUSTRIAL INICIADO ---")
print("*(Para fechar o simulador, digite 0 em qualquer valor)*\n")

while True:
    # 1. Leitura do Sensor de Pressão
    entrada_pressao = input("Digite a Pressão atual (ou 0 para sair): ").replace(",", ".")
    if entrada_pressao == "0":
        print("Simulador encerrado pelo operador.")
        break
    sensor_pressao = float(entrada_pressao)
    
    # 2. Leitura do Sensor de Temperatura
    entrada_temp = input("Digite a Temperatura atual em °C (ou 0 para sair): ").replace(",", ".")
    if entrada_temp == "0":
        print("Simulador encerrado pelo operador.")
        break
    sensor_temperatura = float(entrada_temp)
    
    print("\n--- ANÁLISE DO SISTEMA ---")
    
    # Validação da Pressão (Limite: 4.0)
    if sensor_pressao > 4.0:
        print("⚠️ ALERTA DE PRESSÃO: Acima do limite (4.0)! Parar linha de produção.")
    else:
        print("✅ PRESSÃO: Normal.")
        
    # Validação da Temperatura (Limite: 70.0)
    if sensor_temperatura > 70.0:
        print("🔥 ALERTA DE TEMPERATURA: Superaquecimento (Acima de 70°C)!")
    else:
        print("✅ TEMPERATURA: Estável.")
        
    print("---------------------------\n")



