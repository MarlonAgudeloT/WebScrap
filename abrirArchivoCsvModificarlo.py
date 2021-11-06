import re
import pandas as pd

with open("contraloriaRisaralda.csv","r") as archivo:

    contenido = archivo.read()

#print (contenido)

patron = r'[a-zA-Z0-9._%+-]+@[a-zA-z0-9.-]+.[a-z]{2,}'

coincidencia = re.findall(patron,contenido)

print(coincidencia)

df = pd.DataFrame({"elementos":coincidencia})

df.to_csv('emails_contraloriaRisaralda.csv',mode = 'a', index = False, header = False)

print(df)

