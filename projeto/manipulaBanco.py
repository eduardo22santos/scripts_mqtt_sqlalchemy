from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from construirBanco import Usuario, ConftermItgu, ConfTermItu, ConfTermTempUmi, Dados, ProducaoAnimal, Animais, Localizacao

engine = create_engine("sqlite:///banco2.db", echo=True)
Cursor = sessionmaker(bind=engine)
cursor = Cursor()
base = declarative_base()

def addUsuario(Cpf, Nome, FoneCelular, Email, Senha, NivelAcesso):
    user = Usuario(
    cpf=Cpf,
    nome=Nome,
    foneCelular=FoneCelular,
    email=Email,
    senha=Senha,
    nivelAcesso=NivelAcesso,
    )
    cursor.add(user)
    cursor.commit()

def addAnimal(NomeAnimal):
    animal = Animais(especie=NomeAnimal)
    cursor.add(animal)
    cursor.commit()

def addLocalizacao(Descricao, Latitude, Longitude):
    localizacao = Localizacao(descricao=Descricao, latitude=Latitude, longitude=Longitude)
    cursor.add(localizacao)
    cursor.commit()

addUsuario('021563525', 'eduardo', '79', 'gmail', '123', 1)
addLocalizacao('Um lugar muito Bom', 1.5, 1.3)


