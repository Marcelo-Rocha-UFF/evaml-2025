import random as rnd
import sys

sys.path.insert(0, "../")

import config  # Module with network device configurations.

broker = config.MQTT_BROKER_ADRESS # Broker address.
port = config.MQTT_PORT # Broker Port.
topic_base = config.SIMULATOR_TOPIC_BASE


def node_processing(node, memory):
    """ Função de tratamento do nó """
    # print("The module " + node.tag + " was called.")

    min = node.attrib["min"]
    max = node.attrib["max"]
    # Check if min <= max
    if (int(min) > int(max)):
        # gui.terminal.insert(INSERT, "\nError -> The 'min' attribute of the random command must be less than or equal to the 'max' attribute. Please, check your code.", "error")
        # gui.terminal.see(tkinter.END)
        exit(1)

    if node.get("var") == None: # Maintains compatibility with the use of the $ variable
        memory.var_dolar.append([str(rnd.randint(int(min), int(max))), "<random>"])
        # gui.terminal.insert(INSERT, "\nSTATE: Generating a random number (using the variable $): " + memory.var_dolar[-1][0])
        # tab_load_mem_dollar()
        # gui.terminal.see(tkinter.END)
        print("random command, min = " + min + ", max = " + max + ", valor = " + memory.var_dolar[-1][0])
    else:
        var_name = node.attrib["var"]
        memory.vars[var_name] = str(rnd.randint(int(min), int(max)))
        print("Eva ram => ", memory.vars)
        # gui.terminal.insert(INSERT, "\nSTATE: Generating a random number (using the user variable '" + var_name + "'): " + str(memory.vars[var_name]))
        # tab_load_mem_vars() # Enter data from variable memory into the var table
        #gui.terminal.see(tkinter.END)
        print("random command USING VAR, min = " + min + ", max = " + max + ", valor = " + memory.vars[var_name])

