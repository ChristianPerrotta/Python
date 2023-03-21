# -----------------------------------------------------------
# AppBikeRegras.py
# 
# Este arquivo contém as regras de negócio da aplicação, ou 
# seja, as funções que executam as operações escolhidas pelo
# usuário na interface.
# As funções trabalham instanciando classes do BD e acionando
# métodos do SQLAlchemy para manipular dados armazenados.
# -----------------------------------------------------------

# ----------[ Importações ]----------

from appBikeData import Clientes,Seguranca,SessaoBD

# ----------[ Funções ]----------
def login(usu,psw):
    try:
        # criando uma sessão no banco de dados
        sessao = SessaoBD()
        # recuperando o contato do banco de dados
        usuario = sessao.query(Seguranca).filter_by(usuario=usu).first()
        if (usuario.senha == psw):
            return True
        else:
            return False
    except Exception as erro:
        #print('ERRO>>>>>',erro)
        return False

def incluir(cpfInf, nomeInf, emailInf, tipoInf):
    try:
        # instanciando um objeto Contato
        cli = Clientes(cpf=cpfInf, nome=nomeInf, email=emailInf, tipo=tipoInf, numBicicleta=0)
        # criando uma sessão no banco de dados
        sessao = SessaoBD()
        # inserindo novo contato no banco de dados
        sessao.add(cli)
        sessao.commit()
        return True
    except Exception as erro:
        #print('ERRO>>>>>',erro)
        sessao.rollback()
        return False

def alterar(cpfInf, nomeInf, emailInf, tipoInf,numBicInf):
    try:
        # criando uma sessão no banco de dados
        sessao = SessaoBD()
        # recuperando o contato do banco de dados
        cli = sessao.query(Clientes).filter_by(cpf=cpfInf).first()
        # alterando o nome e o e-mail do contato recuperado
        cli.nome = nomeInf
        cli.email = emailInf
        cli.tipo = tipoInf
        cli.numBicicleta = numBicInf
        sessao.commit()
        return True
    except Exception as erro:
        #print('ERRO>>>>>',erro)
        sessao.rollback()
        return False

def excluir(cpfInf):
    try:
        # criando uma sessão no banco de dados
        sessao = SessaoBD()
        # recuperando o contato do banco de dados
        cli = sessao.query(Clientes).filter_by(cpf=cpfInf).first()
        # excluindo o contato recuperado
        sessao.delete(cli)
        sessao.commit()
        return True
    except Exception as erro:
        #print('ERRO>>>>>',erro)
        sessao.rollback()
        return False

def consultar_todos():
    try:
        # criando uma sessão no banco de dados
        sessao = SessaoBD()
        # recuperando todos os contatos do banco de dados em uma lista
        listaCli = sessao.query(Clientes)
        return listaCli
    except Exception as erro:
        #print('ERRO>>>>>',erro)
        return False

def consultar_um(cpfCli):
    try:
        # criando uma sessão no banco de dados
        sessao = SessaoBD()
        # recuperando o contato do banco de dados
        cli = sessao.query(Clientes).filter_by(cpf=cpfCli).first()
        return cli
    except Exception as erro:
        #print('ERRO>>>>>',erro)
        return False

# ----------[ Testando escopo de execução ]----------

if __name__ == '__main__':
    print('Este módulo só pode ser executado dentro da aplicação.')
    exit()