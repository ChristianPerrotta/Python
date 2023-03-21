# -----------------------------------------------------------
# AppBikeIntefTexto.py
# 
# Este arquivo contém a interface do aplicativo (inicialmente
# em texto, mas futuramente pode ser substituída por uma nova
# interface gráfica). 
# A interface vai chamar o módulo "contatos.py", que contém a
# estratégia (regras de negócio) da aplicação.
# -----------------------------------------------------------

# ----------[ Importações ]----------

from appBikeRules import *
from appBikeData import Clientes

# ----------[ Aplicação ]----------
def incCliente():
    # --------------------- INCLUSÂO
    print('''
    ===================
    Inclusão de Cliente
    ===================''')
    cpf   = int(input("            CPF   : "))
    nome  =     input("            Nome  : ")
    email =     input("            E-mail: ")
    tipo  =     input("            Tipo (A/M): ")
    resp = incluir(cpf, nome, email, tipo)
    if resp:
        print(f'Cliente Nome: {nome} incluído com sucesso\n')
    else:
        print(f'ERRO na inclusão do cliente {nome}\n')

def altCliente():
    # --------------------- ALTERAÇÃO
    print('''
    ====================
    Alteração de Cliente
    ====================''')
    cpf   = int(input("            CPF   : "))
    cli = consultar_um(cpf)
    if (cli):
        print(f'Nome: {cli.nome}  E-mail:{cli.email}  Tipo: {cli.tipo}\n')
        nome  =     input("            Nome  : ")
        email =     input("            E-mail: ")
        tipo  =     input("            Tipo (A/M): ")
        resp = alterar(cpf, nome, email, tipo, cli.numBicicleta)
        if resp:
            print(f'Cliente Nome: {nome} alterado com sucesso\n')
        else:
            print(f'ERRO na alteração do cliente {cpf}\n')
    else:
        print(f'CPF {cpf} não encontrado')

def excCliente():
    # --------------------- EXCLUSÃO
    print('''
    ===================
    Exclusão de Cliente
    ===================''')
    cpf   = int(input("            CPF   : "))
    cli = consultar_um(cpf)
    if (cli):
        print(f'Nome: {cli.nome}  E-mail:{cli.email}  Tipo: {cli.tipo}\n')
        conf = input("            Confirma exclusãoNome  : ")
        if conf:
            resp = excluir(cpf)
            if resp:
                print(f'Cliente: {cpf} excluido com sucesso\n')
            else:
                print(f'ERRO na alteração do cliente {cpf}\n')
    else:
        print(f'CPF {cpf} não encontrado')

def retBike():
    # --------------------- RETIRAR BICICLETA
    print('''
    =================
    Retirar Bicicleta
    =================''')
    cpf     = int(input("            CPF       : "))
    cli = consultar_um(cpf)
    if (cli):
        numBike = int(input("            Bicicleta : "))
        resp = alterar(cli.cpf, cli.nome, cli.email, cli.tipo, numBike)
        if resp:
            print(f'Cliente {cpf} retirou a bicicleta {numBike}\n')
        else:
            print(f'ERRO na retirada de bicicleta {cpf}/{numBike}\n')
    else:
        print(f'CPF {cpf} não encontrado')

def devBike():
    # --------------------- DEVOLVER BICICLETA
    print('''
    =================
    Devolver Bicicleta
    =================''')
    cpf     = int(input("            CPF       : "))
    cli = consultar_um(cpf)
    if (cli):
        bike = cli.numBicicleta
        resp = alterar(cli.cpf, cli.nome, cli.email, cli.tipo, 0)
        if resp:
            print(f'Cliente {cpf} devolveu bicicleta número {bike}\n')
        else:
            print(f'ERRO na devolução de bicicleta do cliente {cpf}\n')
    else:
        print(f'CPF {cpf} não encontrado')

def acompanhamento():
    # --------------------- ACOMPANHAMENTO
    print('''
    ==============
    Acompanhamento
    ==============''')
    listaClientes = consultar_todos()
    if (listaClientes):
        print('-'*50)
        for cli in listaClientes:
            print(cli.cpf, cli.nome, cli.email, cli.tipo, cli.numBicicleta)
        print('-'*50)
    else:
        print(f'ERRO no acompanhamento\n')

def app():
    while True:
        print('''
          
        ======================================
            Agenda de Contatos
        ======================================
        1. Incluir cliente
        2. Alterar cliente
        3. Excluir cliente
        4. Retirar bicicleta
        5. Devolver bicicleta
        6. Acompanhamento
        7. Sair da aplicação
        ======================================''')

        # entrada da operação
        op = int(input('        Escolha uma operação: '))

        # chamando a operação escolhida
        if op == 1:
            incCliente()
        elif op == 2:
            altCliente()
        elif op == 3:
            excCliente()
        elif op == 4:
            retBike()
        elif op == 5:
            devBike()
        elif op == 6:
            acompanhamento()
        elif op == 7:
            print("VOCÊ ESCOLHEU SAIR DA APLICAÇÃO")
            break
        else:
            print("ERRO: OPÇÃO INVÁLIDA")

    print("Fim do programa.")

# ----------[ Testando escopo de execução ]----------

if __name__ == '__main__':
    app()
else:
    print('Este módulo só pode ser executado como programa principal.')
    exit()
