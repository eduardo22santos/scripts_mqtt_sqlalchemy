from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.operators import custom_op
from dadosDeCampo import ordenha, pasto
import csv

engine = create_engine('sqlite:///banco.db', echo=True)
Cursor = sessionmaker(bind=engine)
cursor = Cursor()
base = declarative_base()

tabela = open('tabelas/dois_globos_csv.csv','r')
leitor = csv.reader(tabela)

for coluna in leitor:
    if coluna[1] == 'horario':
        continue
    else:
        dados = ordenha(data=coluna[0],horario=coluna[1],bulbo_seco=float(coluna[2]),globo_negro=float(coluna[4]),umidade=float(coluna[3]),orvalho=float(coluna[7]),itu=float(coluna[6]),itgu=float(coluna[5]))
        cursor.add(dados)
        #cursor.flush()
cursor.commit()