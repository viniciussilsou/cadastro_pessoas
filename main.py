from cadastroPessoas import carrregajsonparaarquivo,createpeople,loadpeopletojson


def createnewperson():

    lista = carrregajsonparaarquivo()
    novapessoa = createpeople()
    lista.append(novapessoa)
    loadpeopletojson(lista)

createnewperson()

