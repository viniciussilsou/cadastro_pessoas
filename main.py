from cadastroPessoas import carrregajsonparaarquivo,createpeople,loadpeopletojson
from buscar_pessoa import buscarpessoaporcpf
from deleta_pessoa import deletarpessoa
import json


def selecionarfuncao():

    func = int(input("SELECIONE:\n"
                 "1 - NOVO CADASTRO\n"
                 "2 - BUSCAR CADASTRO\n"
                 "3 - EXLCUIR CADASTRO\n"))

    return func

def cadastropessoas():

    funcao = selecionarfuncao()

    if funcao == 1:
        lista = carrregajsonparaarquivo()
        novapessoa = createpeople()
        lista.append(novapessoa)
        loadpeopletojson(lista)

    elif funcao == 2:
        buscarpessoaporcpf()

    elif funcao == 3:
        deletarpessoa()


cadastropessoas()










