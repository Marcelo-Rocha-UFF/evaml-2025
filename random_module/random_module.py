import random as rnd

from rich.console import Console

console = Console()

import sys

sys.path.insert(0, "../")

import config  # Module with network device configurations.

broker = config.MQTT_BROKER_ADRESS # Broker address.
port = config.MQTT_PORT # Broker Port.
topic_base = config.SIMULATOR_TOPIC_BASE


def node_processing(node, memory):
    """ Função de tratamento do nó """

    min = node.get("min")
    max = node.get("max")
    
    # Check if min <= max
    if (int(min) > int(max)):
        aux = min
        min = max
        max = aux
        console.print('[b blink reverse red] Warning [/]: The value of [b white]min=' + str(min) + '[/] is greater than[b white] max=' + str(max) + '[/]. We [u]fixed[/] it. 👍') 

    if node.get("var") == None: # Maintains compatibility with the use of the $ variable
        memory.var_dolar.append([str(rnd.randint(int(min), int(max))), "<random>"])
    else:
        var_name = node.attrib["var"]
        memory.vars[var_name] = str(rnd.randint(int(min), int(max)))


    return node # It returns the same node
