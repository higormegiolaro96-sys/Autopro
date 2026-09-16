def evaluate_temperature(temperatura_motor):
    """Avalia a temperatura do motor e retorna um dicionário com o nível e mensagens.

    Retorna:
        dict: {
            'level': 'ideal' | 'warning' | 'critical',
            'messages': [str, ...]
        }
    """
    messages = []
    messages.append(f"⚙️ MONITORAMENTO ATIVO: Temperatura atual do motor: {temperatura_motor}°C.")

    if temperatura_motor < 70:
        level = "ideal"
        messages.append("🟢 STATUS: Temperatura ideal. Robô operando em ciclo automático.")
    elif 70 <= temperatura_motor <= 90:
        level = "warning"
        messages.append("🟡 ATENÇÃO: Motor aquecido! Gerando ordem preventiva no SAP.")
        messages.append("👉 Recomendação: Verificar nível de graxa/óleo na próxima parada.")
    else:
        level = "critical"
        messages.append("🔴 ALERTA CRÍTICO: SUPER-AQUECIMENTO!")
        messages.append("🔒 INTERTRAVAMENTO ATIVADO: Parando o robô imediatamente para proteger o motor.")
        messages.append("🚨 Enviando alarme para o painel do supervisor da linha.")

    return {"level": level, "messages": messages}


def print_report(temperatura_motor):
    """Imprime o relatório de monitoramento no stdout."""
    result = evaluate_temperature(temperatura_motor)
    print("--------------------------------------------------")
    for m in result["messages"]:
        print(m)
    print("--------------------------------------------------")


if __name__ == "__main__":
    # Exemplo de uso: ao executar diretamente, usa um valor de exemplo.
    temperatura_motor = 75
    print_report(temperatura_motor)
