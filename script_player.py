import time

import xml.etree.ElementTree as ET

from auxiliar_module import import_modules


# VM global variables
root = {}
script_node = {}
links_node = {}
fila_links =  [] # Link queue (commands)
thread_pop_pause = False
play = False # Play status of the script. This variable has an influence on the function. link_process
script_file = "" # Variable that stores the pointer to the xml script file on disk.


tree = ET.parse('eva_demo.xml')  # XML code file
root = tree.getroot() # script root node
script_node = root.find("script")
links_node = root.find("links")


# modulo = script_node[0].tag + '-module'

# sys.path.insert(0, "light-module/") 
# sys.path.insert(0, "display-module/")
# sys.path.insert(0, "evaemotion-module/")


# mod = importlib.import_module('light-module')
# mod2 = importlib.import_module('evaemotion-module')

# for child in script_node:
#     print(f"Elemento filho: {child.tag}, Atributos: {child.attrib}")
    

# eval('mod.node_processing')(script_node[0], 3)
# eval('mod2.node_processing')(script_node[1], 3)

# eval('mod.node_processing')(script_node[0], 3)

# client.publish(topic_base + "/talk", root.find("settings")[0].attrib["tone"] + "|" + texto[ind_random])

# if node.get("tone") == None: # Usuario não selecionou a voz no talk. A opção global será utilizada
#     tone_voice = root.find("settings")[0].attrib["tone"]

# def reloadFile(self):
#     global root, script_node, links_node, script_file
#     script_file.seek(0) # Places the file object pointer at the beginning
#     tree = ET.parse(script_file) # # XML code file
#     root = tree.getroot() # EvaML root node
#     script_node = root.find("script")
#     links_node = root.find("links")
#     evaEmotion("NEUTRAL")
#     only_file_name = str(script_file).split("/")[-1].split("'")[0]
#     gui.terminal.insert(INSERT, '\nSTATE: Script => ' + only_file_name + ' was RELOADED.')
#     gui.terminal.see(tkinter.END)


tab_modules = import_modules(script_node, verbose_mode=True)

def run_script(xml_root): # percorre toda a seção de script identificando os elementos utilizados.
    print("Rodando o script.")
    for element in xml_root.iter():
        time.sleep(1)
        if element.tag != "script":
            mod = tab_modules[element.tag][2]
            eval('mod.node_processing')(element, 3)
        
# tab_modules = import_modules(script_node, verbose_mode=True)
# identify_elements(script_node)
# import_modules(tab_modules)
run_script(script_node)

# list_nodes = list(script_node)
# print(list_nodes)