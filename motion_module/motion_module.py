import sys

from rich import print

sys.path.insert(0, "../")

import config  # Module with network device configurations.


topic_base = config.ROBOT_TOPIC_BASE



def node_processing(node, memory, client_mqtt):
    """ Função de tratamento do nó """
    
    print("[b white]State:[/] [b white]Moving[/] the [b white]Robot[/]. [b white]Type: [/][reverse b white on black] " + node.attrib["type"] + " [/].")
    
    # Controla o robô físico.
    if memory.running_mode == "robot":  
        topic = "move" # O tópico para movimentos no FRED é move e não motion.
        message = node.get("type")
        client_mqtt.publish(topic_base + '/' + topic, message.lower())

    return node # It returns the same node
