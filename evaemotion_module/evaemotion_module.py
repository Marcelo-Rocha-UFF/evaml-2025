from paho.mqtt import client as mqtt_client

from rich import print as rprint

import sys

sys.path.insert(0, "../")

import config  # Module with network device configurations.

broker = config.MQTT_BROKER_ADRESS # Broker address.
port = config.MQTT_PORT # Broker Port.
topic_base = config.SIMULATOR_TOPIC_BASE


def node_processing(node, memory):
    """ Função de tratamento do nó """
    rprint("[bold]State:[/bold] Setting the robot display to [bold]" + node.get("emotion") + "[/].")

    message = node.get("emotion")
    
    client = create_mqtt_client()

    client.publish(topic_base + '/' + node.tag, message)

    return node # It returns the same node


# # MQTT
# # The callback for when the client receives a CONNACK response from the server.
# def on_connect(client, userdata, flags, rc):
#     print("Mqtt client connected.")
#     pass
    

# # The callback for when a PUBLISH message is received from the server.
# def on_message(client, userdata, msg):
#     pass

# Run the MQTT client thread.
def create_mqtt_client():
    client = mqtt_client.Client()
    # client.on_connect = on_connect
    # client.on_message = on_message
    try:
        client.connect(broker, port)
    except:
        print ("Unable to connect to Broker.")
        exit(1)
    
    return client