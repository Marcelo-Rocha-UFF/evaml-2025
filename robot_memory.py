# Is equivalent to the $ of the original Eva software
# Is a list of results
var_dolar = []

# "case" flag
reg_case = None

# ops
switch_op = None

# Eva ram (a key/value dictionary)
vars = {}

# Contem a associação entre os nomes dos elementos e seus módulos
# A chave é a tag do elemento e o valor é uma lista com 2 elementos:
# 1) o número de ocorrências do elemento no script
# 2) o objeto que aponta para o módulo importado.
tab_modules = {}

# Essa tabela deve conter todos os elementos com "id", ou seja, aqueles que podem ser chamados por um <goto>
tab_targets = {}


