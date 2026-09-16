print("--------------------------------------------------")
print(f"⚙️ MONITORAMENTO ATIVO: Temperatura atual do motor: {temperatura_motor}°C.")
print("--------------------------------------------------")

if temperatura_motor < 70:
    print("🟢 STATUS: Temperatura ideal. Robô operando em ciclo automático.")
    
elif temperatura_motor >= 70 and temperatura_motor <= 90:
    print("🟡 ATENÇÃO: Motor aquecido! Gerando ordem de preventiva no SAP.")
    print("👉 Recomendação: Verificar nível de graxa/óleo na próxima parada.")
    
else:
    print("🔴 ALERTA CRÍTICO: SUPER-AQUECIMENTO!")
    print("🔒 INTERTRAVAMENTO ATIVADO: Parando o robô imediatamente para proteger o motor.")
    print("🚨 Enviando alarme para o painel do supervisor da linha.")
