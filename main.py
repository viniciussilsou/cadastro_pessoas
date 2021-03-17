from cadastroPessoas import carrregajsonparaarquivo,createpeople,loadpeopletojson
import json


def createnewperson():

    lista = carrregajsonparaarquivo()
    novapessoa = createpeople()
    lista.append(novapessoa)
    loadpeopletojson(lista)

def printarquivo():

    with open('cadastro_pessoas.json') as arquivo:

        pessoas = json.load(arquivo)
        pessoa = pessoas[1]
        print(pessoa['nome'])

printarquivo()




