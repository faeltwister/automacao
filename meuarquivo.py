import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Instala e configura o serviço do driver do Chrome
servico = Service(ChromeDriverManager().install())

link = 'https://www.globo.com/'

def agendador():
    navegador = webdriver.Chrome(service=servico)

    print("Entrando no Site...")
    time.sleep(3)
    navegador.get(link)
    time.sleep(3)
    print("Digitando o nome...")
    time.sleep(2)
    # navegador.find_element('xpath','//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').send_keys("Rafael")
    # navegador.find_element('xpath','//*[@id="section-10356508"]/section/div[2]/div/div[2]/form/div[1]/div/div[1]/div/input').click()
    time.sleep(5)  # Aguarda 5 segundos (ajuste conforme necessário)

    print("Fechando...")

    print("Finalizado!")

    navegador.quit()



# Executa a função a cada 1 minuto
while True:
    agendador()

    # Aguarda 1 minuto
    time.sleep(60)  
