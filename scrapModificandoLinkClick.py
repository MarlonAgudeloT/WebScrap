#-*- coding: utf-8 -*-
import re
from collections import deque
from urllib.parse import urlsplit
import requests
import zipfile
import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd


#Aqui ingresamos a la pagina que deseamos scrapear

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.funcionpublica.gov.co/dafpIndexerBHV/?find=FindNext&query=dane&dptoSeleccionado=&entidadSeleccionado=&munSeleccionado=&tipoAltaSeleccionado=Servidor+P%C3%BAblico&bloquearFiltroDptoSeleccionado=&bloquearFiltroEntidadSeleccionado=&bloquearFiltroMunSeleccionado=&bloquearFiltroTipoAltaSeleccionado=&offset=0&max=10")

quotes_page = 'https://www.funcionpublica.gov.co/dafpIndexerBHV/?find=FindNext&query=dane&dptoSeleccionado=&entidadSeleccionado=&munSeleccionado=&tipoAltaSeleccionado=Servidor+P%C3%BAblico&bloquearFiltroDptoSeleccionado=&bloquearFiltroEntidadSeleccionado=&bloquearFiltroMunSeleccionado=&bloquearFiltroTipoAltaSeleccionado=&offset=0&max=10'
uClient = uReq(quotes_page)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser") # Esto modifica el formato html para convertirlo en datos que puede leer Python
#datos = page_soup.findAll("div",{"class":"div-resultados"})
time.sleep(5)
#datos1 = page_soup.findAll("td",{"class":"columna-datos"}) # Especificamos la clase en la que deseamos buscar
datos1 = page_soup.findAll("span" == r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com")
#print(datos1)
# print(datos)

# Con este for buscamos los datos dentro de cada uno de los nombres
"""response = requests.get(quotes_page)

new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.com", response.text, re.I))
emails = []
for mails in new_emails: 
    
    emails.append(mails.text) 

print(emails)"""

elementos = []
for elem in datos1:
    #titulo = elem.find("td",{"class":"columna-datos"})
    #email = elem.find_all("span")
    elementos.append(elem.text)


    #print(email)

"""with open("data1.txt", "w+") as f:
    for dato in elementos:
        str_value = str(dato)
        f.write(str_value)
        f.write("\n")  
        print(dato)"""

df = pd.DataFrame({"elementos":elementos})

df.to_csv('emails2.csv',mode = 'a', index = False, header = False)

print(df)
# Desde aqui cambia de pagina


#time.sleep(2)
#nextpage = driver.find_element_by_xpath('//*[@id="div-resultados-busqueda"]/div[2]/ul[2]/li[14]/a')
#nextpage.click()

"""for i in nextpage:
    try:
        driver.find_element_by_xpath("//*[contains(text(), '{}')]".format(i)).click()
    except:
        print("Element with name '%s' is not found" % i)"""