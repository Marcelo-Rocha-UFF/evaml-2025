from paho.mqtt import client as mqtt_client

import sys

from rich import print

sys.path.insert(0, "../")

import config  # Module with network device configurations.

broker = config.MQTT_BROKER_ADRESS # Broker address.
port = config.MQTT_PORT # Broker Port.
topic_base = config.SIMULATOR_TOPIC_BASE



def node_processing(node, memory):
    """ Função de tratamento do nó """
    print("[bold]State:[/bold] Setting the robot [b white]LED[/] to the animation [bold]" + node.get("animation") + "![/].")

    message = node.get("animation")

    client = create_mqtt_client()
    client.publish(topic_base + '/' + node.tag, message)

    return node # It returns the same node


def create_mqtt_client():
    client = mqtt_client.Client()
    try:
        client.connect(broker, port)
    except:
        print ("Unable to connect to Broker.")
        exit(1)
    
    return client