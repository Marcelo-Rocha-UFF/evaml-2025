from rich import print
from rich.console import Console

console = Console()

import sys

sys.path.insert(0, "../")

import config  # Module with network device configurations.

topic_base = config.SIMULATOR_TOPIC_BASE



def node_processing(node, memory, client_mqtt):
    """ Função de tratamento do nó """

    if node.get("language") == None: # Maintains compatibility with the use of <listen> in old scripts
        # It will be used the default value defined in config.py file
        language_for_listen = config.LANG_DEFAULT_GOOGLE_TRANSLATING
    else:
        language_for_listen =  node.get("language")
    
    print('[b white]State:[/] The Robot is [b green]listening[/] in [b white]' + language_for_listen + '[/]. ', end="")

    user_answer = console.input("[b white on green blink] > [/] ")
    
    if node.get("var") == None: # Maintains compatibility with the use of the $ variable
        memory.var_dolar.append([user_answer, "<listen>"])
    else:
        var_name = node.get("var")
        memory.vars[var_name] = user_answer

    

    # client = create_mqtt_client()
    # client.publish(topic_base + '/' + node.tag, message)

    return node # It returns the same node

