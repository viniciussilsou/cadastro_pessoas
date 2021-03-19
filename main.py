from cadastroPessoas import carrregajsonparaarquivo,createpeople,loadpeopletojson
from buscar_pessoa import buscarpessoaporcpf
import json


def createnewperson():

    lista = carrregajsonparaarquivo()
    novapessoa = createpeople()
    lista.append(novapessoa)
    loadpeopletojson(lista)

def printarquivo():

    with open('cadastro_pessoas.json') as arquivo:

        pessoas = json.load(arquivo)

    for pessoa in pessoas:
        for c, v in pessoa.items():
            print('{}:{}'.format(c,v))

buscarpessoaporcpf()






