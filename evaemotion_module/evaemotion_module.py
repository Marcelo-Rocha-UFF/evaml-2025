from rich import print

import sys

sys.path.insert(0, "../")

import config  # Module with network device configurations.

topic_base = config.ROBOT_TOPIC_BASE




def node_processing(node, memory, client_mqtt):
    """ Função de tratamento do nó """

    if node.get("emotion") == "NEUTRAL":
        emoji = " 😐"
    elif node.get("emotion") == "GREETINGS":
        emoji = " 👋👋"
    elif node.get("emotion") == "BROKEN":
        emoji = " 😵"
    elif node.get("emotion") == "PLEASED":
        emoji = " 🙂"
    elif node.get("emotion") == "ANGRY":
        emoji = " 😡"
    elif node.get("emotion") == "ANGRY2":
        emoji = " 😡😡"
    elif node.get("emotion") == "DISGUST":
        emoji = " 😖"
    elif node.get("emotion") == "AFRAID":
        emoji = " 😧"
    elif node.get("emotion") == "HAPPY":
        emoji = " 😄"
    elif node.get("emotion") == "IN_LOVE":
        emoji = " 🥰"
    elif node.get("emotion") == "SAD":
        emoji = " 😔"
    elif node.get("emotion") == "SURPRISED":
        emoji = " 😲"
    elif node.get("emotion") == "SPEECH_ON_1":
        emoji = " 💬 ⭕"
    elif node.get("emotion") == "SPEECH_OFF_1":
        emoji = " 🔇"
    elif node.get("emotion") == "SPEECH_ON_2":
        emoji = " 💬💬"
    elif node.get("emotion") == "SPEECH_OFF_2":
        emoji = " 🔇🔇"

    print("[b white]State:[/] Setting the robot [b white]expression[/] to [bold]" + node.get("emotion") + emoji + "[/].")

    if memory.running_mode == "robot":
        message = node.get("emotion")
        topic = "expression" # Para o FRED o tópico não é "emotion"
        client_mqtt.publish(topic_base + '/' + topic, message.lower())

    return node # It returns the same node

