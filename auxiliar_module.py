# Este módulo define duas funções.
# Uma função para a identificação dos elementos usados no script.
# Uma função para a importação dos módulos associados a cada um desses elementos.
# A função de importação retorna uma tabela que associa os nomes (tags) dos elementos com os objetos dos módulos importados.

import sys
import importlib

from rich import print as rprint
from rich.console import Console
from rich.table import Table

console = Console()

def identify_targets(xml_root, verbose_mode=False):
    tab_targets = {}
    for element in xml_root.iter():
        if element.get("id") and element.tag != "macro": # Cria a tabela com os elementos que possuem o atributo "id" excluindo as macros.
            tab_targets[element.get("id")] = [element.tag, element]
    return tab_targets


def identify_elements(xml_root, verbose_mode=False):
    """Percorre toda a seção de script identificando os elementos utilizados."""
    if verbose_mode:
        # Rich tem um método para limpar a tela
        console.clear()
        rprint("[bold underline green]Identificando os elementos do script.[/]")
    tab_modules = {}
    for element in xml_root.iter():
        if element.tag in tab_modules:
            tab_modules[element.tag][0] = tab_modules[element.tag][0] + 1
        else:
            if element.tag != "script":
                tab_modules[element.tag] = [1]
    if verbose_mode:
        rprint("[white]O script utuliza [bold]" + str(sum(1 for _ in xml_root.iter()) - 1) + " elemento(s).")
    return tab_modules
    """ Retorna uma tabela com os elmentos utilizados no script"""


def import_modules(xml_root, verbose_mode=False):
    """Importa os módulos associados a cada um dos elementos do script."""
    import_error = False
    tab_modules = identify_elements(xml_root, verbose_mode)
    for element_tag in tab_modules:
        module_name = element_tag.lower() + "_module" # nome padrão para pastas dos módulos
        sys.path.insert(0, module_name + "/") # coloca o diretório do módulo no path
        try:
            mod = importlib.import_module(module_name) # importa o módulo
            tab_modules[element_tag].append(module_name + ".py")
            tab_modules[element_tag].append(mod)
        except:
            import_error = True
            tab_modules[element_tag].append("Not imported")
            tab_modules[element_tag].append(None)
            # rprint("[bold red]Sorry! It was not possible to import the module " + "[red italic]" + module_name + "[/]")
    
    if verbose_mode:
        print("")
        table = Table(title="[bold]XML Elements and Modules")
        table.add_column("XML Element")
        table.add_column("Ocurrence")
        table.add_column("Associated Module")
        for key, value in tab_modules.items():
            if value[2]: # not None
                table.add_row("[bold yellow]" + key, "[bold cyan ]" + str(value[0]).center(9), "[bold green]" + value[1])
                #rprint("[bold yellow]" + key.ljust(20) + "[/][bold cyan ]" + str(value[0]).ljust(13) + "[bold green]" + value[1].ljust(30) + "[/]")
            else:
                table.add_row("[bold yellow]" + key, "[bold cyan ]" + str(value[0]).center(9), "[bold red]" + value[1])
                #rprint("[bold yellow]" + key.ljust(20) + "[/][bold cyan ]" + str(value[0]).ljust(13) + "[bold red]" + value[1].ljust(30) + "[/]")
        console.print(table)
    
    # if import_error:
    #     return tab_modules
    #     print("")
    #     rprint("[bold red underline]*** The execution was aborted ***")
    #     print("\n")
    #     exit(1)
    # else:
    return tab_modules


    
