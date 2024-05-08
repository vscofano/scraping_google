import pandas as pd
import re


file_list = input('Digite o nome do arquivo txt: ')
df = pd.read_csv(f'{file_list}.txt',sep='\t') #abre o arquivo txt e transforma em df
lista_de_listas = df.values.tolist()
links_lista = [str(link) for link in lista_de_listas]
padrao = [r'https://www.instagram.com/p/[\w-]+/?',
          r'https://www.instagram.com/reel/[\w-]+/?',
         r'https://www\.instagram\.com/[\S]+/reels/']

'''
padrao_1 = r'https://www.instagram.com/p/[\w-]+/?'
padrao_2 = r'https://www.instagram.com/reel/[\w-]+/?'
padrao_3 = r'https://www.instagram.com/[\w/]+/reels'
'''

c=0
for link in links_lista:
    for i in padrao:
        correspondencia = re.findall(i,link)
        if correspondencia:
            c+=1
            print(correspondencia)
nova_lista = [link for link in links_lista if not any(re.findall(p, link) for p in padrao)]      
print(c)


df = pd.DataFrame(nova_lista)
df.to_csv(f'lista_raspada_{file_list}')
#print(df) 


