import time

from rich.progress import Progress, TextColumn, BarColumn, TimeElapsedColumn

import sys

sys.path.insert(0, "../")

import config  # Module with network device configurations.

broker = config.MQTT_BROKER_ADRESS # Broker address.
port = config.MQTT_PORT # Broker Port.
topic_base = config.SIMULATOR_TOPIC_BASE


def node_processing(node, memory):
    """ Função de tratamento do nó """
    # print("The module " + node.tag + " was called.")

    duration = node.attrib["duration"]
    # gui.terminal.insert(INSERT, "\nSTATE: Pausing. Duration = " + duration + " ms")
    # gui.terminal.see(tkinter.END)
    
    seconds = int(duration)/1000

    # Tempo em segundos
    tempo_total = int(seconds)

    # Barra de progresso personalizada
    with Progress(
        TextColumn("[bold]State:[/bold] Waiting [bold]" + str(seconds) + " [/] seconds. [bold blue]Time left:"),
        BarColumn(bar_width=20),
        TextColumn("[bold cyan]{task.fields[tempo]}")
    ) as progress:
        
        # Adicionar tarefa
        task = progress.add_task("", total=tempo_total, tempo="--:--")
        
        # Contagem regressiva
        for segundos_restantes in range(tempo_total, -1, -1):
            # Formatar o tempo restante
            minutos = segundos_restantes // 60
            segundos = segundos_restantes % 60
            tempo_str = f"{minutos:02d}:{segundos:02d}"
            
            # Atualizar a barra e o campo de tempo
            progresso_atual = tempo_total - segundos_restantes
            progress.update(task, completed=progresso_atual, tempo=tempo_str)
            
            # Aguardar 1 segundo, mas apenas se não for o último valor
            if segundos_restantes > 0:
                time.sleep(1)

    return node # It returns the same node