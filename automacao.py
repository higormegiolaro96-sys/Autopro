import os
import psutil
import time
import shutil
from plyer import notification

def enviar_notificacao(titulo, mensagem):
    """Envia um pop-up nativo no canto inferior direito do Windows."""
    try:
        notification.notify(
            title=titulo,
            message=mensagem,
            app_name="Acelerador de Sistema",
            timeout=5  # O pop-up some após 5 segundos
        )
    except Exception:
        pass  # Evita que erros de notificação travem o script


def limpar_arquivos_temporarios():
    """Deleta arquivos inúteis da pasta %TEMP% para destravar o SSD."""
    pasta_temp = os.environ.get('TEMP')
    if not pasta_temp or not os.path.exists(pasta_temp):
        return

    arquivos_deletados = 0
    for item in os.listdir(pasta_temp):
        caminho_item = os.path.join(pasta_temp, item)
        try:
            if os.path.isfile(caminho_item) or os.path.islink(caminho_item):
                os.unlink(caminho_item)
                arquivos_deletados += 1
            elif os.path.isdir(caminho_item):
                shutil.rmtree(caminho_item)
                arquivos_deletados += 1
        except Exception:
            continue
            
    print(f"🧹 Faxina Concluída! {arquivos_deletados} arquivos temporários limpos.")
    enviar_notificacao("🧹 Limpeza de Disco", f"Faxina concluída! {arquivos_deletados} arquivos inúteis foram removidos.")


def ativar_energia_alta_performance():
    """Força o processador e a placa de vídeo ao limite de velocidade (Ótimo para TIA Portal e Jogos)."""
    try:
        os.system("powercfg /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c")
        print("⚡ Modo Desempenho Máximo ativado no hardware.")
        enviar_notificacao("⚡ Hardware Otimizado", "Notebook configurado para Alta Performance!")
    except Exception:
        print("⚠️ Não foi possível alterar o plano de energia automaticamente.")


def gerenciar_processos_tempo_real():
    """Varre o sistema para proteger a memória RAM e acelerar os apps de automação industrial."""
    # O Google Chrome está LIBERADO. Bloqueia apenas navegadores secundários abertos de fundo por engano.
    navegadores_proibidos = ["msedge.exe", "opera.exe", "firefox.exe"]
    
    # Executáveis da Siemens para priorizar na CPU
    processos_siemens = ["tia.exe", "s7tgtopx.exe", "s7onlinx.exe"]

    for processo in psutil.process_iter(['name', 'pid']):
        try:
            nome_processo = processo.info['name'].lower()
            pid_processo = processo.info['pid']
            
            # 1. Fecha navegadores que pesam na RAM à toa
            if nome_processo in navegadores_proibidos:
                processo.terminate()
                print(f"❌ [BLOQUEADO] {nome_processo} encerrado.")
                
            # 2. Gatilho de Prioridade para o TIA Portal / STEP 7
            elif nome_processo in processos_siemens:
                p = psutil.Process(pid_processo)
                if p.nice() != psutil.HIGH_PRIORITY_CLASS:
                    p.nice(psutil.HIGH_PRIORITY_CLASS)
                    print(f"🚀 [IMPULSIONADO] Prioridade ALTA em {nome_processo} (PID: {pid_processo})")
                    enviar_notificacao("⚙️ TIA Portal / STEP 7", f"Foco total ativado para {nome_processo}! Processador focado aqui.")
                
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue


if __name__ == "__main__":
    print("====================================================")
    print("        GERENCIADOR DE PERFORMANCE AUTOMÁTICO       ")
    print("====================================================\n")
    
    # Notifica o usuário e faz as otimizações pesadas de inicialização
    enviar_notificacao("🤖 Sistema Ativo", "Seu assistente Python começou a monitorar o notebook.")
    
    limpar_arquivos_temporarios()
    time.sleep(1)
    ativar_energia_alta_performance()
    time.sleep(1)
    
    print("\n====================================================")
    print("  ENTRANDO EM MODO SENTINELA (VERIFICAÇÃO A CADA 10S)")
    print("  Pressione 'Ctrl + C' no terminal para fechar.     ")
    print("====================================================")
    
    try:
        while True:
            gerenciar_processos_tempo_real()
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n🛑 Monitoramento encerrado. O notebook voltou ao estado normal.")
