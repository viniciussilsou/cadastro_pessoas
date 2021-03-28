import json

def deletarpessoa():

    cpfdelete = str(input("Digite CPF para Excluir:\n"))

    with open("cadastro_pessoas.json") as arquivo:
        jsonpessoa = json.load(arquivo)

    for pessoa in jsonpessoa:

        if cpfdelete == pessoa.get("cpf"):
            confirmacao = int(input("Deseja excluir {} ?\n 1 - SIM \n 2 - NÃO\n".format(pessoa)))

            if confirmacao == 1:
                jsonpessoa.remove(pessoa)
                print("CADASTRO DELETADO COM SUCESSO !\n")
            else:
                print("FIM")
        else:
            print("CPF não encontrado ! \n")
            repetir = int(input("Deseja realizar nova busca?\n 1-SIM\n 2-NÃO\n"))

            if repetir == 1:
                deletarpessoa()
            else:
                exit()

    with open("cadastro_pessoas.json",'w') as arquivojson:

        arquivodump = json.dumps(jsonpessoa, indent=4)
        arquivojson.write(arquivodump)


