import pytest
from monitor_robotic import evaluate_temperature


@pytest.mark.parametrize(
    "temp, expected_level, expected_substr",
    [
        (0, "ideal", "STATUS: Temperatura ideal"),
        (69.9, "ideal", "STATUS: Temperatura ideal"),
        (70, "warning", "ATENÇÃO: Motor aquecido"),
        (75, "warning", "ATENÇÃO: Motor aquecido"),
        (90, "warning", "ATENÇÃO: Motor aquecido"),
        (90.1, "critical", "ALERTA CRÍTICO"),
        (120, "critical", "ALERTA CRÍTICO"),
    ],
)
def test_evaluate_temperature_levels_and_messages(temp, expected_level, expected_substr):
    result = evaluate_temperature(temp)
    assert isinstance(result, dict)
    assert "level" in result and "messages" in result
    assert result["level"] == expected_level
    # Verifica se alguma das mensagens contém o trecho esperado
    assert any(expected_substr in m for m in result["messages"])
