from rich import print as rprint

import sys

sys.path.insert(0, "../")

import config  # Module with network device configurations.

broker = config.MQTT_BROKER_ADRESS # Broker address.
port = config.MQTT_PORT # Broker Port.
topic_base = config.SIMULATOR_TOPIC_BASE



def node_processing(node, memory):
    """ Função de tratamento do nó """
    print("The module " + node.tag + " was called.")

    aux_node = node
    # Getting the root element
    while aux_node.getparent() is not None:
        if aux_node.tag ==  "script":
            break
        aux_node = aux_node.getparent()

    root = aux_node  # Root is the root node

    print(node, node.tag)
    target_value = node.get('target')
    if target_value == None:
        rprint("[red bold]Target ID no found.")
        exit(1)
    node = root.find(".//*[@id=" + "'" + target_value + "'" + "]")

    return node