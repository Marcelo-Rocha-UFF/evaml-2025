from rich import print

import sys

sys.path.insert(0, "../")

import config  # Module with network device configurations.

broker = config.MQTT_BROKER_ADRESS # Broker address.
port = config.MQTT_PORT # Broker Port.
topic_base = config.SIMULATOR_TOPIC_BASE


def node_processing(node, memory):
    """ Função de tratamento do nó """
    # print("The module " + node.tag + " was called.")
    memory.op_switch = node.attrib["var"]
    memory.flag_case = False
    print("[bold]State:[/bold] Processing a [b white]Switch[/]. Var=" + memory.op_switch + ".")
    
    return node # It returns the same node