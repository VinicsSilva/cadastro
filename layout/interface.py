from bancoDados.dados import *
import time

def lerOpc():
    a = ['Acessar as pessoas já cadastradas','Cadastrar nova pessoa','Sair do sistema']
    return a

def l(a=40):
    print('-'*a)

def inicio():
    l()
    print('SISTEMA DE CADASTRO'.center(40))
    l()
    opcoes(lerOpc())
    l()

def opcoes(list):
    z = 1
    for x in list:
        print(f'{z} - {x}')
        z+=1
    

def vrf():
    while True:
        try:
            op = int(input('Qual opção você deseja selecionar? '))
        except:
            print('\033[0;31mErro! Valor inválido.\033[m')
        else:
            if op == 1:
                return op
                break
            elif op == 2:
                return op
                break
            elif op == 3:
                return op
                break
            else:
                print('\033[0;31mEsta opção não existe!\033[m')
                continue

def opc(a):
    if a == 1:
        l()
        print('USUÁRIOS CADASTRADOS'.center(40))
        l()
        lerArq()

    elif a == 2:
        novoCadastro()
    elif a == 3:
        l()
        print('Saindo do programa',end='')
        time.sleep(0.5)
        print('.',end='')
        time.sleep(0.5)
        print('.',end='')
        time.sleep(0.5)
        print('.',end='')

def novoCadastro():
    l()
    print('NOVO CADASTRO'.center(40))
    l()
    while True:
        try:
            nome = str(input('Nome: '))
        except:
            print('\033[0;31mErro ao cadastrar o nome, tente novamente.\033[m')
        else:
            break
    while True:
        try:
            idade = int(input('Idade: '))
        except:
            print('\033[0;31mErro ao cadastrar a idade, tente novamente.\033[m')
        else:
            break
