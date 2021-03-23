import json

def carrregajsonparaarquivo():

    with open("cadastro_pessoas.json") as arquivo:
        arquivojson = json.load(arquivo)

        return arquivojson

def createpeople():

    pessoa = {}
    telefone = {}

    pessoa['cpf'] = input("Digite CPF:\n")
    pessoa['nome'] = input("Digite Nome:\n")
    pessoa['idade'] = input("Qual Idade:\n")
    telefone['ddd'] = input("Digite DDD\n")
    telefone['Número'] = input("Digite Telefone:\n")

    pessoa['telefone'] = telefone

    return pessoa

def loadpeopletojson(listadepessoas):

    with open("cadastro_pessoas.json",'w') as arquivojson:

        arquivodump = json.dumps(listadepessoas, indent=4)
        arquivojson.write(arquivodump)







