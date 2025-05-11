# Adapter module for the audio library
# Depending on the OS it matters and defines a function called "playsound"
from play_audio import playsound

from paho.mqtt import client as mqtt_client
 
from rich import print

import sys

sys.path.insert(0, "./")

import config  # Module with network device configurations.

broker = config.MQTT_BROKER_ADRESS # Broker address.
port = config.MQTT_PORT # Broker Port.
topic_base = config.SIMULATOR_TOPIC_BASE


def node_processing(node, memory):
    """ Função de tratamento do nó """
    if node.get("block") == "TRUE":
        print('[b white]State:[/][b white] Playing[/] ▶️  the sound [bold][b white]"' + node.get("source") + '"[/] in [b white]BLOCKING[/] mode.')
        try:
            playsound("audio_module/audio_files/" + node.get("source") + ".wav", block = True)
        except FileNotFoundError as e:
            print('[b white on red blink] FATAL ERROR [/]: [b yellow reverse] There was a problem playing the audio file [/]: [b white]"' + node.get("source") + '"[/]. Check if it [b white u]exists[/] or is in the [b white u]correct format[/] (wav).✋⛔️')
            exit(1) 
    else:
        try:
            print('[b white]State:[/][b white] Playing[/] ▶️  the sound [bold][b white]"' + node.get("source") + '"[/] in [b white]NON-BLOCKING[/] mode.')
            playsound("audio_module/audio_files/" + node.get("source") + ".wav", block = False)
        except FileNotFoundError as e:
            print('[b white on red blink] FATAL ERROR [/]: [b yellow reverse] There was a problem playing the audio file [/]: [b white]"' + node.get("source") + '"[/]. Check if it [b u white]exists[/] or is in the [b u white]correct format[/] (wav)[/].✋⛔️')
            exit(1) 

    # message = node.get("source") + "|" + node.get("block")
    # client = create_mqtt_client()
    # client.publish(topic_base + '/' + node.tag, message)

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