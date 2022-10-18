from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

#url = 'https://cadunico.dataprev.gov.br/#/consultaCpf'
#browser =  Firefox()
#browser.get(url)

def consultar(browser,cpf,dtnasc):
    browser.implicitly_wait(0.5)
    browser.find_element(By.CSS_SELECTOR,'[id="numeroCpfPessoa"]').send_keys(Keys.BACKSPACE*11)
    browser.find_element(By.CSS_SELECTOR,'#mui-1').send_keys(Keys.BACKSPACE*9)
    browser.find_element(By.CSS_SELECTOR,'[id="numeroCpfPessoa"]').send_keys(cpf)
    carregando = len(browser.find_elements(By.CSS_SELECTOR,'#mui-1'))
    while carregando < 0:
        carregando = len(browser.find_elements(By.CSS_SELECTOR,'#mui-1'))
    browser.find_element(By.CSS_SELECTOR,'#mui-1').send_keys(dtnasc)
    browser.find_element(By.CSS_SELECTOR,'[class="br-button ConsultaCpf_botaoGovBr__1Vp3a"]').click()
    carregando1 = len(browser.find_elements(By.CSS_SELECTOR,'div[class*="LoadingGlobal"'))
    while carregando1 > 0:
        carregando1 = len(browser.find_elements(By.CSS_SELECTOR,'div[class*="LoadingGlobal"'))
    if len(browser.find_elements(By.CSS_SELECTOR,'span[class="Message_title__LINZ4"]')) > 0:
        mensagem = browser.find_element(By.CSS_SELECTOR,'span[class="Message_title__LINZ4"]').text
    else:
        mensagem = browser.find_element(By.CSS_SELECTOR,'span[class="ConsultaCpf_title__2cgXL"]').text
    return cpf, dtnasc, mensagem



if __name__ == '__main__':
    pessoas = [{'cpf':'39951112897','dt':'16091991'},
            {'cpf':'05904106360','dt':'02091992'},
            {'cpf':'07496554880','dt':'08061959'}
                        ]
    
    for dados in pessoas:
        print(consultar(dados['cpf'],dados['dt']))















