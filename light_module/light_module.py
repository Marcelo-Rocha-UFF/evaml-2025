from paho.mqtt import client as mqtt_client

from rich import print

import sys

sys.path.insert(0, "../")

import config  # Module with network device configurations.

broker = config.MQTT_BROKER_ADRESS # Broker address.
port = config.MQTT_PORT # Broker Port.
topic_base = config.SIMULATOR_TOPIC_BASE


def node_processing(node, memory):
    """ Função de tratamento do nó """
    # É preciso tratar os casos em que o node vem sem o "color" definido
    if node.get('state') == "OFF":
        light_color = 'BLACK'
        message = light_color + "|" + 'OFF'
    else:
        if node.get('color') == None:
            light_color = 'WHITE'
        else:
            light_color = node.get('color')
        message = light_color + "|" + node.attrib["state"]

    tab_colors = {"BLACK": "[b white on grey19] OFF [/]",
                  "BLUE": "[b white on blue ] ON [/]",
                  "GREEN": "[b white on green ] ON [/]",
                  "PINK": "[b white on magenta ] ON [/]",
                  "RED": "[b white on red ] ON [/]",
                  "YELLOW": "[b white on yellow ] ON [/]",
                  "WHITE": "[b black on white ] ON [/]"
                  }
    print("[bold]State:[/bold] Setting the [b white]Light[/]. 💡 " + tab_colors[light_color])
    

    client = create_mqtt_client()
    client.publish(topic_base + '/' + node.tag, message)

    return node # It returns the same node


# Run the MQTT client thread.
def create_mqtt_client():
    client = mqtt_client.Client()

    try:
        client.connect(broker, port)
    except:
        print ("Unable to connect to Broker.")
        exit(1)
    
    return client