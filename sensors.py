print("--- SIMULADOR DE PRESSÃO INICIADO ---")
print("*(Para fechar o simulador, digite 0)*\n")

while True:
    sensor_pressao = float(input("Digite o valor atual da pressão (ou 0 para sair): ").replace(",", "."))
    
    if sensor_pressao == 0:
        print("Simulador encerrado pelo operador.")
        break
        
    if sensor_pressao > 4.0:
        print("⚠️ ALERTA: Pressão acima do limite! Parar linha de produção.\n")
    else:
        print("✅ STATUS: Pressão normal. Linha operando.\n")
