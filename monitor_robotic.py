from typing import Dict, List, Optional
import logging


def evaluate_temperature(temperatura_motor: float) -> Dict[str, object]:
    """Avalia a temperatura do motor e retorna um dicionário com o nível e mensagens.

    Args:
        temperatura_motor: temperatura atual do motor em °C.

    Retorna:
        dict: {
            'level': 'ideal' | 'warning' | 'critical',
            'messages': [str, ...]
        }
    """
    messages: List[str] = []
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


def print_report(temperatura_motor: float, logger: Optional[logging.Logger] = None) -> None:
    """Imprime o relatório de monitoramento no stdout ou registra via logger.

    Args:
        temperatura_motor: temperatura atual do motor em °C.
        logger: se fornecido, as mensagens serão enviadas para esse logger em vez de stdout.
    """
    result = evaluate_temperature(temperatura_motor)
    header = "--------------------------------------------------"

    if logger is None:
        print(header)
        for m in result["messages"]:
            print(m)
        print(header)
    else:
        logger.info(header)
        for m in result["messages"]:
            logger.info(m)
        logger.info(header)


def get_default_logger() -> logging.Logger:
    """Configura e retorna um logger simples para uso em integrações/produção."""
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
    return logging.getLogger("monitor_robotic")


if __name__ == "__main__":
    # Exemplo de uso: ao executar diretamente, usa um valor de exemplo.
    temperatura_motor = 75
    # Ao executar como script, usamos o logger por padrão para demonstrar integração com sistemas de logs.
    logger = get_default_logger()
    print_report(temperatura_motor, logger)
