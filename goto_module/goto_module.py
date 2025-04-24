from rich import print as rprint

import sys

sys.path.insert(0, "../")

import config  # Module with network device configurations.

broker = config.MQTT_BROKER_ADRESS # Broker address.
port = config.MQTT_PORT # Broker Port.
topic_base = config.SIMULATOR_TOPIC_BASE



def node_processing(node, memory):
    """ Função de tratamento do nó """

    aux_node = node
    # Getting the root element
    while aux_node.getparent() is not None:
        if aux_node.tag ==  "script":
            break
        aux_node = aux_node.getparent()

    root = aux_node  # Root is the root node

    target_value = node.get('target')

    if target_value == None:
        rprint("[red bold]Target ID no found on <goto>.")
        exit(1)
    else:
        node = root.find(".//*[@id=" + "'" + target_value + "'" + "]")
        if node == None:
            rprint("[red bold]It was not possible to find the target: " + target_value)
            exit(1)
    
    rprint("[bold]State:[/bold] Jumping to the element [bold]" + node.tag + "[/] with [bold]id = " + node.get("id") + "[/].")

    return node # It returns the "target" node 