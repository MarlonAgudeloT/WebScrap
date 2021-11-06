# ESTE SI ESTA FUNCIONANDO
#-*- coding: utf-8 -*-
import os
import re
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pd


#Aqui ingresamos a la pagina que deseamos scrapear

bandera = True
url = "https://www.funcionpublica.gov.co/dafpIndexerBHV/?find=FindNext&query=pereira&dptoSeleccionado=Risaralda&entidadSeleccionado=2677&munSeleccionado=&tipoAltaSeleccionado=Servidor+P%C3%BAblico&bloquearFiltroDptoSeleccionado=&bloquearFiltroEntidadSeleccionado=&bloquearFiltroMunSeleccionado=&bloquearFiltroTipoAltaSeleccionado=&offset=60&max=10"

while bandera == True:
    bandera=False
    url = url
    driver = webdriver.Chrome(ChromeDriverManager().install()) # ESTO SIRVE PARA ABRIR LA PAGINA DESDE EL IDE
    driver.get(url)
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html,"html.parser") # Esto modifica el formato html para convertirlo en datos que puede leer Python
    time.sleep(5)

    datos1 = page_soup.findAll("span")
    emails = []
    def findMails(datos1):
        for name in datos1:
            TextMail = name.text
        #name=re.findall(TextMail,'[a-zA-Z0-9._%+-]+@[a-z0-9.-]+.[a-z]{2,}') #Esta es otra forma de buscar el email
            name=re.findall('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',TextMail)#Esta liena de codigo nos permite buscar el email
        #Con este If limpiamos los datos para que queden guardados de una forma mas ordenada
            if('@' in TextMail):
                TextMail=TextMail.replace(" ",'').replace('\r','')
                TextMail=TextMail.replace('\n','').replace('\t','')
                if(len(emails)==0)or(TextMail not in emails):
                #print(TextMail)
                    emails.append(TextMail)
    print("Aqui")

    findMails(datos1) # EJECUTAMOS LA FUNCION PARA QUE BUSQUE Y AGREGUE LOS DATOS A LA LISTA VACIA

    df = pd.DataFrame({"elementos":emails})

    df.to_csv('contraloriaRisaralda.csv',mode = 'a+', index = False, header = False)

    print(df)

    #href = driver.find_element_by_xpath('//a[contains(@href,"href")]')
    #href = driver.find_element_by_partial_link_text('somelink')
    #href = soup.find_all('a',href=True)
    #href=driver.find_element_by_css_selector('[href^=http://somelink.com/]')
    """href=driver.find_element_by_xpath('//a[@href="'+url+'"]')
    print(href+"Este es href")
    url = href
    #.get('href')
    print(url)"""
    """
    link_text = ""

    for a in soup.find_all('a', href=True, text=True):
        link_text = a['href']

    print ('Link: ' + link_text)
    
    time.sleep(2)
    nextpage = driver.get(link_text)
    nextpage.click()

    bandera = True"""

#AQUI BUSCAMOS LOS DATOS QUE NOS INTERESAN











#Asi buscamos las url en las nuevas paginas


