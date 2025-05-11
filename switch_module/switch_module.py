from rich import print

import sys

sys.path.insert(0, "../")

import config  # Module with network device configurations.

broker = config.MQTT_BROKER_ADRESS # Broker address.
port = config.MQTT_PORT # Broker Port.
topic_base = config.SIMULATOR_TOPIC_BASE


def node_processing(node, memory):
    """ Função de tratamento do nó """
    # Por definição, o switch pode conter referências aos "$" e às variáveis.
    # As variaveis são referenciadas pelo nome, sem o usr do "#" no início.
    if node.get("var")[0] != "$": # É uma variável definida pelo usuário.
        try:
            memory.op_switch = str(memory.vars[node.get('var')]).lower()
        except:
            print("[b white on red blink] FATAL ERROR [/]:  The variable [b white]" + node.get("var") + "[/] used in[b white] <switch>[/] element,[b yellow reverse] has not been declared [/]. Please, check your code.✋⛔️")
            exit(1)
    else: # É um tipo "$", "$n" ou "$-n"
        # Checks if var_dollar memory has any value
        if (len(memory.var_dolar)) == 0:
            print('[b white on red blink] FATAL ERROR [/]: There are [b yellow reverse] no values [/] for the [b white]' + node.get("var") + "[/] used in[b white] <switch>[/]. Please, check your code.✋⛔️")
            exit(1)

        elif len(node.get("var")) == 1: # Is the dollar ($)
            memory.op_switch = memory.var_dolar[-1][0]
    
        else: # May be of type $n or $-n.
            try:
                if "-" in node.get("var"): # $-n type
                    indice = int(node.get("var")[2:]) # Var dollar is of type $-n. then just take n and convert it to int
                    memory.op_switch = memory.var_dolar[-(indice + 1)][0]
                else: # tipo $n
                    indice = int(node.get("var")[1:]) # Var dollar is of type $n. then just take n and convert it to int
                    memory.op_switch =  memory.var_dolar[(indice - 1)][0]
            except IndexError:
                print("[b white on red blink] FATAL ERROR [/]: It looks like [b yellow reverse] there is an error with the index [/] used with the [b white]$[/] variable. Please, check your code.✋⛔️")
                exit(1)

    memory.flag_case = False
    print('[b white]State:[/] Processing a [b white]Switch[/]. [b white]Var "' + node.get("var") + '"[/], with [b white]value = ' + memory.op_switch + ".")
    
    return node # It returns the same node