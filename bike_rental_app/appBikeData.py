# -----------------------------------------------------------
# AppBikeDados.py
# 
# Este arquivo define a engine do banco de dados, conectando 
# a engine a um arquivo/servidor (ou criando, se não existir).
# Aqui também são definidas as classes e suas ligações com as
# tabelas no banco de dados.
# -----------------------------------------------------------

# ----------[ Importações ]----------

# importando a biblioteca SQLAlchemy
import sqlalchemy
# importando sub-bibliotecas
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

# ----------[ Engine e Base de Dados ]----------

# criando engine
engine = sqlalchemy.create_engine('sqlite:///bike.db',echo=False)
# criando a base de dados
Base = declarative_base()
# criando uma sessão no banco de dados
SessaoBD = sessionmaker(bind=engine)

# ----------[ Classes da Aplicação ]----------

# Classe/Tabela: Clientes
# -------------> Define os clientes da aplicação 
#                e controla os empréstimos das bicicletas
class Clientes(Base):
    __tablename__ = 'tb_clientes'
    cpf = Column(Integer, primary_key=True)
    nome = Column(String(20))
    email = Column(String(50))
    tipo = Column(String(1))
    numBicicleta = Column(Integer)

# Classe/Tabela: Seguranca
# -------------> Define usuários e senhas para acesso ao app
class Seguranca(Base):
    __tablename__ = 'tb_seguranca'
    usuario = Column(String(20), primary_key=True)
    senha = Column(String(20))

# ----------[ Criando as Tabelas ]----------

# criando todas as tabelas no banco de dados
Base.metadata.create_all(engine)

# ----------[ Povoando a tabela de segurança ]----------
try:
    usuario1 = Seguranca(usuario='admin', senha='999')
    usuario2 = Seguranca(usuario='funcionario', senha='888')
    # criando uma sessão no banco de dados
    sessao = SessaoBD()
    # inserindo novo contato no banco de dados
    sessao.add_all([usuario1,usuario2])
    sessao.commit()
except Exception as erro:
    sessao.rollback()
sessao.close()
# ----------[ Testando escopo de execução ]----------

if __name__ == '__main__':
    print('Este módulo só pode ser executado dentro da aplicação.')
    exit()