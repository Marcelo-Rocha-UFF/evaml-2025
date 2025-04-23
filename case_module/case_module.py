import sys

sys.path.insert(0, "../")

import config  # Module with network device configurations.

broker = config.MQTT_BROKER_ADRESS # Broker address.
port = config.MQTT_PORT # Broker Port.
topic_base = config.SIMULATOR_TOPIC_BASE


def node_processing(node, memory):
    """ Função de tratamento do nó """
    # print("The module " + node.tag + " was called.")
    # print("Comparando: ", memory.switch_op, "com", node.attrib["value"])
    if memory.switch_op != None:
        if memory.switch_op == node.attrib["value"]:
            memory.reg_case = True
            memory.switch_op = None
        else:
            memory.reg_case = False
    print("Resultado da comparação:", memory.reg_case)

