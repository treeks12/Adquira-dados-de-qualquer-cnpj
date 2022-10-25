import re
import os
import requests
from bs4 import BeautifulSoup
from pprint import pprint

def uf_check(vl):
    if vl == "São Paulo":
        vl = "SP"
    elif vl == "Minas Gerais":
        vl = "MG"
    elif vl == "Espírito Santo":
        vl = "ES"
    elif vl == "Paraná":
        vl = "PR"
    elif vl == "Rio Grande do Sul":
        vl = "RS"
    elif vl == "Santa Catarina":
        vl = "SC"
    elif vl == "Mato Grosso do Sul":
        vl = "MS"
    elif vl == "Mato Grosso":
        vl = "MT"
    elif vl == "Goiás":
        vl = "GO"
    elif vl == "Distrito Federal":
        vl = "DF"
    elif vl == "Bahia":
        vl = "BA"
    elif vl == "Sergipe":
        vl = "SE"
    elif vl == "Alagoas":
        vl = "AL"
    elif vl == "Pernambuco":
        vl = "PE"
    elif vl == "Paraíba":
        vl = "PB"
    elif vl == "Rio Grande do Norte":
        vl = "RN"
    elif vl == "Ceará":
        vl = "CE"
    elif vl == "Piauí":
        vl = "PI"
    elif vl == "Maranhão":
        vl = "MA"
    elif vl == "Pará":
        vl = "PA"
    elif vl == "Amapá":
        vl = "AP"
    elif vl == "Amazonas":
        vl = "AM"
    elif vl == "Rondônia":
        vl = "RO"
    elif vl == "Roraima":
        vl = "RR"
    elif vl == "Acre":
        vl = "AC"
    elif vl == "Tocantins":
        vl = "TO"
    return vl
        

cnpj = input("Escreva o cnpj: ")
cnpj = re.sub('[^0-9]', '', cnpj)
cnpjbiz = "https://cnpj.biz/" + cnpj

url = cnpjbiz
req = requests.get(url)
soup = BeautifulSoup(req.text, "html.parser")
data = [b.string for b in soup.findAll('b')]
data2 = [p.get_text() for p in soup.find_all("p")]

def procura(lista, palavra):
    try:
        posicao = [i for i, s in enumerate(lista) if str(palavra) in s]
    
        posicao2 = re.sub('[^0-9]', '', str(posicao))
        return int(posicao2)
    
    except:
        return False


if procura(data2, "Complemento: ") != False:
    complemento02 = data2[procura(data2, "Complemento: ")]
    complemento = complemento02.replace("Complemento: ", "")
    complemento2 = True
else:
    complemento2 = False

razao02 = data2[procura(data2, "Razão Social: ")]
razao = razao02.replace("Razão Social: ", "")

ins_estadual02 = re.sub('[^0-9]', '', data2[procura(data2, "Inscrição Estadual")])
ins_estadual = ins_estadual02.replace("Inscrição Estadual", "")

logradouro02 = re.sub('[^a-zA-Z ]', '', data2[procura(data2, "Logradouro: ")])
logradouro = logradouro02.replace("Logradouro: ", "")
numero_logradouro = re.sub('[^0-9]', '', data2[procura(data2, "Logradouro: ")])
bairro02 = data2[procura(data2, "Bairro: ")]
bairro = bairro02.replace("Bairro: ", "")

cep = re.sub('[^0-9]', '', data2[procura(data2, "CEP: ")])
municipio02 = data2[procura(data2, "Município: ")]
municipio = municipio02.replace("Município: ", "")

estado_uf02 = data2[procura(data2, "Estado: ")]
estado_uf1 = estado_uf02.replace("Estado: ", "")
estado_uf = uf_check(estado_uf1)

print(f"CNPJ: {cnpj}\nRazão Social: {razao}\nInscrição Estadual: {ins_estadual}\nLogradouro: {logradouro}{numero_logradouro}")
if complemento2 == True:
    print(f"complemento: {complemento}")
print(f"Bairro: {bairro}\nCEP: {cep}\nMunicípio: {municipio}\nEstado: {estado_uf}\n")

os.system("PAUSE")
