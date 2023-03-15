aula3_RE.py contem o código da aula que utilizou uma expressão regular para separar os termos das
descrições. Contudo, este não tratava dos problemas que surgem com as diferentes posições dos \f
ao longo do documento. Os \f foram todos substituídos por "".

aula3_markers faz a remoção dos \f consoante a posição em que aparecem no documento. Existem 3 locais possíveis:
-> antes do termo
-> logo a seguir ao termo
-> a meio da descrição
Ao fazer a remoção manteve-se a estrutura base pretendida: \n\n termo \n descrição ...
Em seguida adicionaram-se marcadores ao texto: @ no início de cada linha de um termo e # no início de
cada linha da descrição.
O HTML foi gerado como uma tabela para maior acomodamento dos dados.