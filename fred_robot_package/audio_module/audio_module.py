
from play_audio import playsound # Adapter module for the audio library.
# Depending on the OS it matters and defines a function called "playsound".
 
from rich import print

import sys

import os

import time

sys.path.insert(0, "./")

import config  # Module with network device configurations.

topic_base = config.ROBOT_TOPIC_BASE


# Função de bloqueio que é usada para sincronia entre os módulos e o Script Player
def block(state, memory):
    memory.robot_state = state # Altera o estado do robô.
    while memory.robot_state != "free": # Aguarda que o robô fique livre para seguir para o próximo comando.
        time.sleep(0.01)


def node_processing(node, memory, client_mqtt):
    """ Função de tratamento do nó """
    if node.get("block") == "TRUE":
        if memory.running_mode == "robot":
            print('[b white]State:[/][b white] Playing[/] ▶️  the sound [bold][b white]"' + node.get("source") + '"[/] in [b white]BLOCKING[/] mode.')
            message = node.get("source") + "|" + node.get("block")
            client_mqtt.publish(topic_base + '/' + node.tag, message)
            block("Playing a sound", memory)
        else:
            try:
                playsound(os.getcwd() + "/" + config.ROBOT_PACKAGE_FOLDER + "/audio_module/audio_files/" + node.get("source") + ".wav", block = True)
                print('[b white]State:[/][b white] Playing[/] ▶️  the sound [bold][b white]"' + node.get("source") + '"[/] in [b white]BLOCKING[/] mode.')
            except FileNotFoundError as e:
                print('[b white on red blink] FATAL ERROR [/]: [b yellow reverse] There was a problem playing the audio file [/]: [b white]"' + node.get("source") + '"[/]. Check if it [b white u]exists[/] or is in the [b white u]correct format[/] (wav).✋⛔️')
                exit(1) 
    else:
        if memory.running_mode == "robot":
            print('[b white]State:[/][b white] Playing[/] ▶️  the sound [bold][b white]"' + node.get("source") + '"[/] in [b white]NON-BLOCKING[/] mode.')
            message = node.get("source") + "|" + node.get("block")
            client_mqtt.publish(topic_base + '/' + node.tag, message)
        else:
            try:
                playsound(os.getcwd() + "/" + config.ROBOT_PACKAGE_FOLDER + "/audio_module/audio_files/" + node.get("source") + ".wav", block = False)
                print('[b white]State:[/][b white] Playing[/] ▶️  the sound [bold][b white]"' + node.get("source") + '"[/] in [b white]NON-BLOCKING[/] mode.')
            except FileNotFoundError as e:
                print('[b white on red blink] FATAL ERROR [/]: [b yellow reverse] There was a problem playing the audio file [/]: [b white]"' + node.get("source") + '"[/]. Check if it [b u white]exists[/] or is in the [b u white]correct format[/] (wav)[/].✋⛔️')
                exit(1) 
    
    return node # It returns the same node