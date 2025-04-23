import sys

sys.path.insert(0, "../")

import config  # Module with network device configurations.

broker = config.MQTT_BROKER_ADRESS # Broker address.
port = config.MQTT_PORT # Broker Port.
topic_base = config.SIMULATOR_TOPIC_BASE


def node_processing(node, memory):
    """ Função de tratamento do nó """
    # print("The module " + node.tag + " was called.")
    memory.switch_op = node.attrib["var"]
    memory.reg_case == False
    print("Valor de switch_op:", memory.switch_op)

