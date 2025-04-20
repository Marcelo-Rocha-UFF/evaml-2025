# print('Módulo light sendo importado.')

def node_processing(node, memory):
    print("light-module was called...", node.tag, memory)
    print("The light is: ", node.attrib["state"])