from dataclasses import dataclass
from modeloDB import Pessoas,db_session

def insert(cpf,dtnasc,status,job):
    pessoas = Pessoas(cpf=cpf, dtnasc=dtnasc,status=status,job=job)
    db_session.add(pessoas)
    db_session.commit()
    print (f'Pessoa  cadastrada com sucesso')
    


def select(status):
    pessoas = Pessoas.query.filter(Pessoas.status == status).first()
    cpf = pessoas.cpf
    data = pessoas.dtnasc
    status = pessoas.status
    return cpf, data

def update(cpf,status):
    pessoas = Pessoas.query.filter(Pessoas.cpf==cpf).first()
    pessoas.status = status
    db_session.add(pessoas)
    db_session.commit()
    print('Pessoa atualizada...')


def select_all():
    pessoas = Pessoas.query.all()
    for p in pessoas:
        print(p.cpf, p.dtnasc, p.status)

def delete(condicao):
    pessoas = Pessoas.query.filter(Pessoas.dtnasc==condicao).first()
    pessoas.pop()
    Pessoas.save()
    print('Deletado com sucedsso')


if __name__ == '__main__':
    #insert(cpf='46774533817',dtnasc='19031999',status=None)
    #print(select(None))
    select_all()
    #delete('DT_NASC')
    #update('46774533817','Esse CPF não foi encontrado na base do Cadastro Único.')
