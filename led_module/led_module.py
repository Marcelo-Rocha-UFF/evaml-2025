# print('Módulo led sendo importado.')

def node_processing(node, memory):
    """ Função de tratamento do nó """
    print("led-module was called...", node.tag, memory)
    print("The led is: ", node.attrib["animation"])