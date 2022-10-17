from layout.interface import *
from bancoDados.dados import *

if vrfArq():
    print('\033[0;32mArquivo encontrado.\033[m')
else:
    criarArq()
while True:
    inicio()
    op = vrf()
    opc(op)
    if op == 3:
        break