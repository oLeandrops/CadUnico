import pandas as pd
from sqlalchemy import create_engine


engine = create_engine(
    'sqlite:///cadunico.db', echo=True)

conexao_sa = engine.connect()
job = 'JOB71757'
pessoas = pd.read_sql_table('pessoas',conexao_sa, index_col='id')
pessoas = pessoas.query('job=="JOB71757"')
pessoas.to_csv(f'Bases_validadas/basevalidada{job}.csv')
pessoas.to_excel(f'Bases_validadas/basevalidada{job}.xlsx')
#print(pessoas)