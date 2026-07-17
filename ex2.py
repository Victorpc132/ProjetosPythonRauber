nome = input("digite o nome do atleta: ")
idade = int(input("digite a idade do atleta:  "))
peso = float(input("digite o peso do atleta: "))

def calcularatleta(pnome, pidade,ppeso):
    if pidade > 23 and ppeso > 50:
        print("Master")

    if pidade > 18 and pidade < 23 and ppeso > 50:
        print("Pleno")

    if pidade < 17 and ppeso > 50:
        print("Junior")


    if pidade > 23 and ppeso < 50:
        print("Pleno")

    if pidade > 18 and pidade < 23 and peso < 50:
        print("Mini")

    if pidade < 18 and ppeso <50:
        print("Insuficiente para participar")     
    
calcularatleta(nome, idade, peso)
