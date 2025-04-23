import time

import sys

sys.path.insert(0, "../")

import config  # Module with network device configurations.

broker = config.MQTT_BROKER_ADRESS # Broker address.
port = config.MQTT_PORT # Broker Port.
topic_base = config.SIMULATOR_TOPIC_BASE


def node_processing(node, memory):
    """ Função de tratamento do nó """
    # print("The module " + node.tag + " was called.")

    duration = node.attrib["duration"]
    # gui.terminal.insert(INSERT, "\nSTATE: Pausing. Duration = " + duration + " ms")
    # gui.terminal.see(tkinter.END)
    seconds = int(duration)/1000
    print("Wait duration:", seconds, "seconds.")
    if seconds > 1:
        for t in range(int(seconds)):
            print("Counting:", t)
            time.sleep(1) # Convert to seconds
    else:
        time.sleep(seconds) # Convert to seconds