from datetime import date
from sqlalchemy import Column, create_engine,Integer,String,Date
from sqlalchemy.orm import scoped_session,sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#criação do banco de dados

engine = create_engine('sqlite:///cadunico.db', convert_unicode = True)

db_session  = scoped_session(sessionmaker(autocommit=False,
                                            bind=engine))

base = declarative_base()
base.query = db_session.query_property()

#criacao da tabela

class Pessoas(base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key = True)
    cpf = Column(String(20))
    dtnasc = Column(String(20))
    status = Column(String(100))
    job = Column(String(100))

    def __repr__(self):
        return f'cpf {self.cpf} validado!'

    def save(self):
        db_session.add(self)
        db_session.commit()

#criacao efetiva do banco
def init_db():
    base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()