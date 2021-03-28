import json

def buscarpessoaporcpf():

    with open('cadastro_pessoas.json') as arquivo:

        cpfbusca = str(input("Digite o CPF a buscar:"))
        pessoas = json.load(arquivo)

    for pessoa in pessoas:
        if cpfbusca == pessoa.get("cpf"):
            for c, v in pessoa.items():
                print('{}:{}'.format(c, v))
    else:
        print("CPF não encontrado !\n")
        repetir = int(input("Deseja realizar nova busca?\n 1-SIM\n 2-NÃO\n"))

        if repetir == 1:
            buscarpessoaporcpf()
        else:
            exit()





