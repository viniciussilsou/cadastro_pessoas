import json

def loadjsonfile():

    with open("cadastro_pessoas.json") as file:
        jsonfile = json.load(file)

        return jsonfile

def createpeople():

    pessoa = {}

    pessoa['cpf'] = input("Digite cpf:\n")
    pessoa['nome'] = input("Digite nome:\n")
    pessoa[]

    print(pessoa)

    return pessoa

createpeople()



