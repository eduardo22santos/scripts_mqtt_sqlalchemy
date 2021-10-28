from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.operators import custom_op


engine = create_engine('sqlite:///banco.db', echo=True)
Cursor = sessionmaker(bind=engine)
cursor = Cursor()
base = declarative_base()
 
class ordenha(base):
    __tablename__='ordenha'
    id = Column(Integer, primary_key=True)
    data = Column(String)
    horario = Column(String)
    bulbo_seco = Column(Float)
    #bulbo_umido = Column(Float)
    globo_negro = Column(Float)
    #velocidade_vento = Column(Float)
    umidade = Column(Float)
    orvalho = Column(Float)
    itu = Column(Float)
    itgu = Column(Float)
    #ctr = Column(Float)
    #falha = Column(Boolean)

    def __repr__(self):
        pass

class pasto(base):
    __tablename__='pasto'
    id = Column(Integer, primary_key=True)
    data = Column(String)
    horario = Column(String)
    bulbo_seco = Column(Float)
    #bulbo_umido = Column(Float)
    globo_negro = Column(Float)
    #velocidade_vento = Column(Float)
    umidade = Column(Float)
    orvalho = Column(Float)
    itu = Column(Float)
    itgu = Column(Float)
    #ctr = Column(Float)
    #falha = Column(Boolean)

    def __repr__(self):
        pass
base.metadata.create_all(engine)


