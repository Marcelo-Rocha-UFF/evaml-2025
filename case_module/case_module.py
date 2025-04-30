from rich import print

import sys

sys.path.insert(0, "../")

import config  # Module with network device configurations.

broker = config.MQTT_BROKER_ADRESS # Broker address.
port = config.MQTT_PORT # Broker Port.
topic_base = config.SIMULATOR_TOPIC_BASE


def node_processing(node, memory):
    """ Função de tratamento do nó """

    if memory.op_switch == node.get("value"):
        memory.flag_case = True
    else:
        memory.flag_case = False
    print("[bold]State:[/bold] Executing a [b white]Case[/]. Comparing [b white] " + memory.op_switch + "[/] with [b white]" + node.get("value") + "[/]. Result [b reverse]" + str(memory.flag_case) + "[/].")


    return node # It returns the same node

