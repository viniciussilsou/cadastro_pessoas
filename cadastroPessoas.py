import json

def carrregajsonparaarquivo():

    with open("cadastro_pessoas.json") as arquivo:
        arquivojson = json.load(arquivo)

        return arquivojson

def createpeople():

    pessoa = {}
    telefone = {}

    pessoa['cpf'] = input("Digite cpf:\n")
    pessoa['nome'] = input("Digite nome:\n")
    pessoa['idade'] = input("Qual idade:\n")
    telefone['ddd'] = input("Digite DDD\n")
    telefone['Número'] = input("Digite Telefone:\n")

    pessoa['telefone'] = telefone

    print(pessoa)

    return pessoa

def loadpeopletojson(listapessoas):

    with open("cadastro_pessoas.json") as arquivojson:
       arquivodump = json.dumps(listadepessoas)
        arquivojson.write(arquivodump)







