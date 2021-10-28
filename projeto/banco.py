from sqlalchemy import create_engine, Column, Integer, String, Float, Date, Time, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.operators import custom_op
from sqlalchemy.orm import relationship
from sqlalchemy.orm.decl_api import DeclarativeMeta


engine = create_engine('sqlite:///banco2.db', echo=True)
Cursor = sessionmaker(bind=engine)
cursor = Cursor()
base = declarative_base()

class ConftermItgu(base):
    __tablename__='conftermItgu'

    idConftermItgu = Column(Integer, primary_key=True)
    animaisCodAnimal = Column(Integer, ForeignKey("animais.codAnimal"))
    idadeMinima = Column(Integer)
    idadeMaxima = Column(Integer)
    itguMin = Column(Float)
    itguMax = Column(Float)
    situacao = Column(String)

    animal = relationship('Animais', back_populates='confTermItgu')

    def __repr__(self) -> str:
        return super().__repr__()

class ConfTermItu(base):
    __tablename__='confTermItu'

    idConfItu = Column(Integer, primary_key=True)
    animaisCodAnimal = Column(Integer, ForeignKey("animais.codAnimal"))
    idadeMinima = Column(Integer)
    idadeMaxima = Column(Integer)
    ituMin = Column(Float)
    ituMax = Column(Float)
    situacao = Column(String)

    animal = relationship('Animais', back_populates='confTermItu')

    def __repr__(self) -> str:
        return super().__repr__()

class ConfTermTempUmi(base):
    __tablename__='confTermTempUmi'

    idConfTermUmi = Column(Integer, primary_key=True)
    animaisCodAnimal = Column(Integer, ForeignKey("animais.codAnimal"))
    idadeMinima = Column(Integer)
    idadeMaxima = Column(Integer)
    tempMin = Column(Float)
    tempMax = Column(Float)
    umidMin = Column(Float)
    UmidMax = Column(Float)

    animal = relationship('Animais', back_populates='confTermTempUmi')

    def __repr__(self) -> str:
        return super().__repr__()

class Dados(base):
    __tablename__='dados'

    id = Column(Integer, primary_key=True)
    producaoAnimal_idProducaoAnimal = Column(Integer, ForeignKey('producaoAnimal.idProducaoAnimal'))
    data = Column(Date)
    hora = Column(Time)
    tempBulboSeco = Column(Float)
    tempBulboUmido = Column(Float)
    tempGloboNegro = Column(Float)
    tempPontoOrvalho = Column(Float)
    umidade = Column(Float)
    itgu = Column(Float)
    itu = Column(Float)

    producaoAnimal = relationship('ProducaoAnimal', back_populates='dados')

    def __repr__(self) -> str:
        return super().__repr__()

class ProducaoAnimal(base):
    __tablename__='producaoAnimal'

    idProducaoAnimal = Column(Integer, primary_key=True)
    animais_CodAnimais = Column(Integer, ForeignKey("animais.codAnimal"))
    localizacao_idLocalizacao = Column(Integer, ForeignKey("localizacao.idLocalizacao"))
    dataNascimento = Column(Date)
    equipamento = Column(String)
    dataInicioMonitoramento = Column(Date)
    dataFimMonitoramento = Column(Date)

    dados = relationship('Dados', back_populates='producaoAnimal')
    animal = relationship('Animais', back_populates='producaoAnimal')
    localizacao = relationship('Localizacao', back_populates='producaoAnimal')

    def __repr__(self) -> str:
        return super().__repr__()

class Animais(base):
    __tablename__='animais'

    codAnimal = Column(Integer, primary_key=True)
    especie = Column(String)
    producaoAnimal = relationship('ProducaoAnimal', back_populates='animal')
    confTermTempUmi = relationship('ConfTermTempUmi', back_populates='animal')
    confTermItu = relationship('ConfTermItu', back_populates='animal')
    confTermItgu = relationship('ConftermItgu', back_populates='animal')

    def __repr__(self) -> str:
        return super().__repr__()

class Localizacao(base):
    __tablename__='localizacao'

    idLocalizacao = Column(Integer, primary_key=True)
    usuarioCpf = Column(String, ForeignKey("usuario.cpf"))
    descricao = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    producaoAnimal = relationship('ProducaoAnimal', back_populates='localizacao')
    #usuario = relationship('Usuario', back_populates='localizacao')

    def __repr__(self) -> str:
        return super().__repr__()

class Usuario(base):
    __tablename__='usuario'

    id = Column(Integer, primary_key=True)
    cpf = Column(String)
    nome = Column(String)
    foneCelular = Column(String)
    email = Column(String)
    senha = Column(String)
    nivelAcesso = Column(Integer)
    
    localizacao = relationship('Localizacao')

    def __repr__(self) -> str:
        return super().__repr__()

base.metadata.create_all(engine)