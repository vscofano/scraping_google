import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd


print('---------------------------')
print('')
print('Bem Vindo, Meu nome é Chaos e sou um Scrapper de dados dos resultados de pesquisa do Google')  
print('---------------------------')
print('')
nome_lista = input('Digite o nome para salvar o arquivo de urls raspados: ')  
print('')
url = input('Cole o url do resultado da pesquisa: ')
print('')
driver = webdriver.Firefox()#iniciando o navegador
driver.get(url)#entrando na pagina de resultados
time.sleep(2)
driver.refresh #recarregando à pagina

#fazendo a página rolar até o final usando JS
body = driver.find_element("tag name","body")
while True:
   try:
      caixa =  driver.find_element(By.XPATH, '//div[@class="ClPXac Pqkn2e"]')
      break
   except Exception as e:
      body.send_keys(Keys.END)
      time.sleep(1)

url = driver.find_element(By.XPATH, '//div[@class="ClPXac Pqkn2e"]//a').get_attribute('href') #link para exibir todos os resultados
driver.get(url)
time.sleep(2)
body = driver.find_element("tag name","body")
while True:
   try:
      btn = driver.find_element(By.XPATH,'//a[@aria-label="Mais resultados"]')
      if btn:
         btn.click()
         time.sleep(1)
         print('Carregando mais resultados...')
      else:
         body.send_keys(Keys.END)
         time.sleep(1)
   except Exception as e:
      break
time.sleep(2)
divs = driver.find_elements(By.XPATH,"//div[@class='MjjYud']")
lista_resultados = []
c=0
if divs:
   for div in divs:
      c+=1
      #nome = div.find_element(By.TAG_NAME,"h3")
      link = div.find_element(By.TAG_NAME,"a")
      resultado = "%s" % (link.get_attribute("href"))
      print(resultado)
      #lista_resultados.append(nome.text)
      lista_resultados.append(link.get_attribute("href"))
      print(lista_resultados)

print(f'Encontrei {c} links')

with open(f"{nome_lista}.txt","w") as arquivo:
    for resultado in lista_resultados:
        arquivo.write("%s\n" % resultado)
    arquivo.close()
print('Ja salvei o arquivo')
   
   
