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

    for pessoa in pessoas:
        for c, v in pessoa.items():
            print('{}:{}'.format(c,v))


def buscarpessoaporcpf():

    with open('cadastro_pessoas.json') as arquivo:

        cpfbusca = str(input("Digite o CPF a buscar:"))
        pessoas = json.load(arquivo)
        print(pessoas)

    for pessoa in range(len(pessoas)):
        if cpfbusca == pessoa.values:
            print(pessoa)

buscarpessoaporcpf()




