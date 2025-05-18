from paho.mqtt import client as mqtt_client

import sys

from rich import print

sys.path.insert(0, "../")

import config  # Module with network device configurations.

topic_base = config.ROBOT_TOPIC_BASE


def node_processing(node, memory, client_mqtt):
    """ Função de tratamento do nó """
    print("[b white]State: Setting [/]the robot [b white]LEDs[/] to the animation/color [bold]" + node.get("animation") + "![/].")

    tab_convertion = { # Tabela de conversão de emoções para as cores.
        "HAPPY"     : "GREEN",
        "SAD"       : "BLUE",
        "ANGRY"     : "RED",
        "SURPRISE"  : "YELLOW",
        "SPEAK"     : "BLUE",
        "LISTEN"    : "GREEN",
        "STOP"      : "BLACK"
    }

    message = node.get("animation")
    
    if message in tab_convertion:
        message = tab_convertion[message]

    # Executa no robô.
    if memory.running_mode == "robot":
        # As cores, no mqtt do esp8266, estão definidas em letras minúsculas.
        topic = "leds" # Esse é o nome do tópico para o FRED
        # Os valores para as cores no FRED são em letras minúsculas.
        client_mqtt.publish(topic_base + '/' + topic, message.lower())

    return node # It returns the same node