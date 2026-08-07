name = input("Digite Seu Nome: ")

def ajeitar_nome(nomepar="André da silva Camargo"):
    named = nomepar.split(" ")
    size = len(named)-1
    ultnome = named[size]
    ultnome= ultnome.upper()
    iniciais = ""
    for i in range(size):
        if named[i] not in ['da', 'de', 'do', 'das', 'dos']:
           iniciais += named[i][0].upper()+". "

    return print(ultnome," "+iniciais)

ajeitar_nome(name)