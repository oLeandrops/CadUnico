from bot import consultar
from selenium.webdriver import Firefox
from funcoes_db import select,update

url = 'https://cadunico.dataprev.gov.br/#/consultaCpf'
browser = Firefox()
browser.get(url)


while True:
    cpf, dtnasc = select(None)
    cpf,datanasc,status = consultar(browser,cpf,dtnasc)
    print(cpf,datanasc,status)
    update(cpf,status)


