from operator import index
import pandas as pd
from funcoes_db import insert

df = pd.read_csv('TESTE_CADUNICO.csv', sep=',', encoding='latin_1',dtype=str)
for i in df.index:
    insert(cpf = df['ï»¿CPF'][i],dtnasc = df['DT'][i],status=None,job='TesteBruno')