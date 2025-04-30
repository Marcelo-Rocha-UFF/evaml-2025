from rich import print

import sys

sys.path.insert(0, "../")

import config  # Module with network device configurations.

broker = config.MQTT_BROKER_ADRESS # Broker address.
port = config.MQTT_PORT # Broker Port.
topic_base = config.SIMULATOR_TOPIC_BASE


def node_processing(node, memory):
    """ Função de tratamento do nó """

    var_name = node.get("var")
    var_value = int(node.get("value"))
    op = node.get("op")

    # Checks if the operation is different from assignment and checks if var ... DOES NOT exist in memory
    if op != "=":
        if (var_name not in memory.vars):
            error_string = "\nError -> The variable " + var_name + " [b yellow reverse]has not been declared[/]. Please, check your code."
            print("[b white on red blink] FATAL ERROR [/]: The variable [b white]#" + var_name + "[/] [b yellow reverse]has not been declared[/]. Please, check your code.✋⛔️")
            exit(1)

    if op == "=": # Perform the assignment
        memory.vars[var_name] = var_value

    if op == "+": # Perform the addition
        memory.vars[var_name] += var_value

    if op == "*": # Perform the product
        memory.vars[var_name] *= var_value

    if op == "/": # Performs the division (it was /=) but I changed it to //= (integer division)
        memory.vars[var_name] //= var_value

    if op == "%": # Calculate the module
        memory.vars[var_name] %= var_value



    return node # It returns the same node