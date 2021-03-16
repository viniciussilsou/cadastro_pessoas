from cadastroPessoas import carrregajsonparaarquivo,createpeople,loadpeopletojson


def createnewperson():

    lista = carrregajsonparaarquivo()
    novapessoa = createpeople()
    print(novapessoa)
    lista.append(novapessoa)
    lista = str(lista)
    print(lista)
    loadpeopletojson(lista)

createnewperson()

