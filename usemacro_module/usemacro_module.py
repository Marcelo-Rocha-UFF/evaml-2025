from paho.mqtt import client as mqtt_client

import sys

from rich import print as rprint

sys.path.insert(0, "../")

import config  # Module with network device configurations.


def node_processing(node, memory):
    """ Função de tratamento do nó """

    # Verifica se a <macro> tem o atributo "id" definido
    macro_id = node.get('macro')
    if macro_id == None:
        rprint("[red bold]Macro ID was not found on <useMacro>.")
        exit(1)

    # Procura pelo id em tab_ids
    for key, value in memory.tab_ids.items():
        if key == node.get("macro"):
            rprint("[bold]State:[/bold] Using macro [bold]" + key + "[/].")
            return value[1] # Retorna a macro associada ao "id" encontrado.
    
    # Não encontrou o "id"
    rprint("[red bold]It was not possible to find the macro: " + key)
    exit(1)

    
