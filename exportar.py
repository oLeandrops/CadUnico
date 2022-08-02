import pandas as pd
from sqlalchemy import create_engine


engine = create_engine(
    'sqlite:///cadunico.db', echo=True)

conexao_sa = engine.connect()

pessoas = pd.read_sql_table('pessoas',conexao_sa, index_col='id')
pessoas.to_excel('basevalidada.xlsx')
print(pessoas)