from bot import consultar
from selenium.webdriver import Chrome
from funcoes_db import select,update
from time import sleep
from selenium.webdriver.common.by import By
url = 'https://cadunico.dataprev.gov.br/#/consultaCpf'
browser = Chrome('C:/Drivers/chromedriver.exe')
browser.get(url)

while True:
    cpf, dtnasc = select(None)
    cpf,datanasc,status = consultar(browser,cpf,dtnasc)
    print(cpf,datanasc,status)
    update(cpf,status)


