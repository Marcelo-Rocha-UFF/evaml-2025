import time

from rich import print
from rich.console import Console

from lxml import etree as ET

from auxiliar_module import identify_targets, identify_elements, import_modules

import robot_memory as memory

console = Console()

# file_name = "teste.xml"
file_name = "tabuada_nova.xml"

tree = ET.parse(file_name)  # XML code file
root = tree.getroot() # script root node
script_node = root.find("script")

# # Versão recursiva
# def run_script(xml_root):
#     # print("Rodando o script.")
#     # if len(list(xml_root)) > 0: 
#     #     node = xml_root[0]
#     # else:
#     node = xml_root
#     while node != None: # Diferente de None (None significa que não tem irmão adiante).
#         # Tratando elementos que têm filhos (<switch>, <case>).
#         if len(node) > 0:
#             # Alguns casos especiais
#             if node.tag == "switch":
#                 mod = memory.tab_modules[node.tag][2]
#                 node = eval('mod.node_processing')(node, memory) # Executa o elemento <switch> que coloca o operador (do switch) na memória.
#                 run_script(node[0]) # Executa o primeiro nó do elemento composto <switch>.
#                 node = node.getnext() # Chama o próximo irmão do no corrente.
            
#             elif node.tag == "case":
#                 # Um case só executa se houver um operador do switch na memória.
#                 if memory.op_switch != None: # Deve haver um operador do switch na memória. None indica que um case verdadeiro já ocorreu neste switch
#                     mod = memory.tab_modules[node.tag][2]
#                     node = eval('mod.node_processing')(node, memory) # Executa o elemento <case> comparando com o operador (do switch) na memória. O result. da comparação fica em memory.flag_case.
#                     if memory.flag_case == True:
#                         memory.flag_case = False
#                         memory.op_switch = None
#                         run_script(node[0]) # Executa o primeiro nó do elemento composto <case> (True).
#                         node = node.getnext() # Chama o próximo irmão do no corrente.
#                     else:
#                         node = node.getnext() # Chama o próximo irmão do no corrente.
#                 else:
#                     break # Quebra a recursão dos cases.
        
#         # Tratando elementos que não têm filhos (<led>, <light> etc)).
#         else:
#             # Alguns casos de nós especiais.
#             if node.tag == "goto":
#                 mod = memory.tab_modules[node.tag][2]
#                 node = eval('mod.node_processing')(node, memory) # Executa o <goto> que retorna o nó destino.
#                 mod = memory.tab_modules[node.tag][2]
#                 node = eval('mod.node_processing')(node, memory) # Executa o nó de destino.
#                 node = node.getnext() # Chama o próximo irmão do no corrente.

#             elif node.tag == "useMacro":
#                 aux_node = node # Será preciso restaurar o nó useMacro no fim desta função.
#                 mod = memory.tab_modules[node.tag][2]
#                 node = eval('mod.node_processing')(node, memory) # Executa o <useMacro> que retorna o nó <macro> referente ao "id".
#                 run_script(node[0]) # Executa o primeiro elemento da macro.
#                 node = aux_node # Restaura o nó useMacro para que seu próximo irmão seja chamado.
#                 node = node.getnext() # Chama o próximo irmão do no corrente.

#             else: # Execução de nós comuns.
#                 mod = memory.tab_modules[node.tag][2]
#                 node = eval('mod.node_processing')(node, memory)
#                 node = node.getnext() # Chama o próximo irmão do no corrente.
        
# Versão iterativa
def run_script(xml_root):
    node = xml_root[0]

    while True: # Roda até ser interrompido por um break.

        if node == None: # None significa o fim de um um nível, onde não existe mais um nó irmão.
            if len(memory.node_stack) != 0: # Se tem elemento na pilha.
                node = memory.node_stack.pop()
            else:
                break

        # Processa os nós que têm filhos.
        elif len(node) > 0:
            if node.tag == "switch":
                if node.getnext() != None: # O nó "switch" tem um irmão adiante.
                    memory.node_stack.append(node.getnext()) # Nó que será executado após o retorno do <switch>.
                mod = memory.tab_modules[node.tag][2]
                node = eval('mod.node_processing')(node, memory) # Executa o <switch> colocando seu operador na memória.
                node = node[0] # Primeiro <case> do <switch>

            elif node.tag == "case":
                if node.getnext() != None: # O nó "case" tem um irmão adiante (o "case" seguinte").
                    memory.node_stack.append(node.getnext()) # Nó "case" que será executado caso o resultado do <case> seja falso.
                
                # Um case só executa se houver um operador do switch na memória.
                if memory.op_switch != None: # Deve haver um operador do switch na memória. None indica que um case verdadeiro já ocorreu neste switch
                    mod = memory.tab_modules[node.tag][2]
                    node = eval('mod.node_processing')(node, memory) # Executa o elemento <case> comparando com o operador (do switch) na memória. O result. da comparação fica em memory.flag_case.
                    if memory.flag_case == True:
                        memory.flag_case = False
                        memory.op_switch = None
                        node = node[0] # Executa o primeiro nó do elemento composto <case> (True).
                    else:
                        node = memory.node_stack.pop() # node = node.getnext() # Chama o próximo irmão do no corrente.
                else:
                    node = memory.node_stack.pop() # 

            elif node.tag == "default" and memory.op_switch != None: # Se chegou aqui...
                mod = memory.tab_modules[node.tag][2]
                node = eval('mod.node_processing')(node, memory)
                node = node[0] # Primeiro nó do <Default>
            
            else:
                node = node.getnext()

        else: # Execução de nós comuns.
            # Alguns casos de nós especiais.
            if node.tag == "goto":
                mod = memory.tab_modules[node.tag][2]
                node = eval('mod.node_processing')(node, memory) # Executa o <goto> que retorna o nó destino.
                # Com a execução sendo direcionada para o nó "target" do <goto>
                # os nós na pilha de endereços de retorno perdem o significado.
                # É preciso zerar a pilha e inserir novos nó que são os pais do nó "target".
                node_parent = node.getparent()
                memory.node_stack = []

                while node_parent.tag != "script" and node_parent.tag != "macro":
                    node_parent = node.getparent()
                    if node_parent.tag == "switch" and node_parent.getnext() != None:
                        memory.node_stack.append(node_parent.getnext())
                    else:
                        node_parent = node_parent.getparent()
                
                memory.node_stack.reverse()

            elif node.tag == "useMacro": # Tratando elemento <useMacro>
                if node.getnext() != None: # O nó "useMacro" tem um irmão adiante.
                    memory.node_stack.append(node.getnext()) # Nó que será executado após o retorno do <useMacro>.
                
                mod = memory.tab_modules[node.tag][2]
                node = eval('mod.node_processing')(node, memory) # Executa o <useMacro> que retorna o nó "macro".
                node = node[0] # Primeiro nó  dentro da "macro"

            else:
                if node.tag != "wait":
                    time.sleep(1)
                mod = memory.tab_modules[node.tag][2]
                node = eval('mod.node_processing')(node, memory)
                node = node.getnext() # Chama o próximo irmão do no corrente.




# Robot memory initializing
memory.tab_modules = import_modules(root, verbose_mode=True)
memory.tab_ids = identify_targets(root, verbose_mode=True)


# Running the script
console.rule("🤖 [red reverse b]  Executing the script: " + file_name + "  [/]")
print()
run_script(script_node)


# def run_script(xml_root):
#     # print("Rodando o script.")
#     if len(list(xml_root)) > 0: 
#         node = xml_root[0]
#     else:
#         node = xml_root
#     while node != None: # Diferente de None (None significa que não tem irmão adiante)
        
#         if node.tag == "goto": # Tratando elemento <goto>
#             mod = memory.tab_modules[node.tag][2]
#             node = eval('mod.node_processing')(node, memory)

#         elif node.tag == "useMacro": # Tratando elemento <useMacro>
#             aux_node = node
#             mod = memory.tab_modules[node.tag][2]
#             node = eval('mod.node_processing')(node, memory)
#             run_script(node)
#             node = aux_node.getnext()
#             run_script(node)
#         else:
#             if node.tag != "wait":
#                 time.sleep(0) # somente pra facilitar a visualização.

#         mod = memory.tab_modules[node.tag][2]
#         node = eval('mod.node_processing')(node, memory)

#         if len(node) > 0: # Tratanto elementos que têm filhos (<switch>, <case>)
#             run_script(node)
#             node = node.getnext()
#         else:
#             node = node.getnext() # Elemento sem filhos

