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
    if node.get("leftArm") != None: # Move the left arm
        print("[bold]State:[/bold] [b white]Moving[/] the [b white]LEFT ARM[/]. [b white]Type: [/][reverse b white on black] " + node.attrib["leftArm"] + " [/].")
    if node.get("rightArm") != None: # Move the right arm
        print("[bold]State:[/bold] [b white]Moving[/] the [b white]RIGHT ARM[/]. [b white]Type: [/][reverse b white on black] " + node.attrib["rightArm"] + " [/].")
    if node.get("head") != None: # Move head with the new format (<head> element)
        print("[bold]State:[/bold] [b white]Moving[/] the [b white]HEAD[/]. [b white]Type: [/][reverse b white on black] " + node.attrib["head"] + " [/].")
    else: # Check if the old version was used
        if node.get("type") != None: # Maintaining compatibility with the old version of the motion element
            print("[bold]State:[/bold] [b white]Moving[/] the [b white]HEAD[/]. [b white]Type: [/][reverse b white on black] " + node.attrib["type"] + " [/].")

    # client = create_mqtt_client()
    # client.publish(topic_base + '/' + node.tag, message)

    return node # It returns the same node



#         if RUNNING_MODE == "EVA_ROBOT":
#             if node.get("leftArm") != None: # Move the left arm
#                 client.publish(topic_base + "/motion/arm/left", node.attrib["leftArm"]); # comando para o robô físico
#             if node.get("rightArm") != None:  # Move the right arm
#                 client.publish(topic_base + "/motion/arm/right", node.attrib["rightArm"]); # comando para o robô físico
#             if node.get("head") != None: # Move head with the new format (<head> element)
#                     client.publish(topic_base + "/motion/head", node.attrib["head"]); # Command for the physical robot
#                     time.sleep(0.2) # This pause is necessary for arm commands to be received via the serial port
#             else: # Check if the old version was used
#                 if node.get("type") != None: # Maintaining compatibility with the old version of the motion element    
#                     client.publish(topic_base + "/motion/head", node.attrib["type"]); # Command for the physical robot
#                     time.sleep(0.2) # This pause is necessary for arm commands to be received via the serial port
#         else:
#             time.sleep(0.1) # A symbolic time. In the robot, the movement does not block the script and takes different times