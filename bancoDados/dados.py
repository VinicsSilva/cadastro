from layout.interface import *

def vrfArq():
    try:
        a = open(nomeArq(),'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criarArq():
    try:
        a = open(nomeArq(), 'wt+')
        a.close()
    except:
        print('\033[0;31mHouve um erro na criação do arquivo.\033[m')
    else:
        print('\033[0;32mArquivo criado com sucesso!\033[m')

def lerArq():
    try:
        b = open(nomeArq(), 'rt')
    except:
        print('\033[0;31mErro ao ler o arquivo.\033[m')
    else:
        for linha in b:
            c = linha.split(';')
            c[1] = c[1].replace('\n', '')
            print(f'{c[0]:<30}{c[1]:>5} anos')
    finally:
        b.close()

def nomeArq():
    return 'dadosCadastrados.txt'

def cadastrar(nome='desconhecido',idade=0):
    try:
        a = open(nomeArq(), 'at')
    except:
        print('\033[0;31mErro ao abrir arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[0;31mFalha ao escrever os dados.\033[m')
        else:
            print('\033[0;32mUsuário cadastrado com sucesso!\033[m')
    finally:
        a.close()