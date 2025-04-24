from rich import print as rprint

import sys

sys.path.insert(0, "../")

import config  # Module with network device configurations.

broker = config.MQTT_BROKER_ADRESS # Broker address.
port = config.MQTT_PORT # Broker Port.
topic_base = config.SIMULATOR_TOPIC_BASE



def node_processing(node, memory):
    """ Função de tratamento do nó """
    rprint("[bold]State:[/bold] Stopping the script.")

    rprint("[bold green]Fim do script[/]")
    exit(1)
    
    return node # It returns the "target" node 