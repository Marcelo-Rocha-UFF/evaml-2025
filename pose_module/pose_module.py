import sys

from rich import print

sys.path.insert(0, "../")

import config  # Module with network device configurations.

topic_base = config.ROBOT_TOPIC_BASE



def node_processing(node, memory, client_mqtt):
    """ Função de tratamento do nó """
    print("[b white]State:[/] Putting the robot in the [b white]pose[/]: [b white reverse] " + node.get("type") + " [/].")

    message = node.get("type")

    # Executa no robô.
    if memory.running_mode == "robot":
        # As cores, no mqtt do esp8266, estão definidas em letras minúsculas.
        client_mqtt.publish(topic_base + '/' + node.tag, message.lower())

    return node # It returns the same node

