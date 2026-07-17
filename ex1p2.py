
num1 = int(input("Digite o numero para multiplicar: "))

def multiplicar(defnum):
    i = 0
    while(i < 11):
        print(defnum, "X", i,"=", defnum*i)
        i= i+1

multiplicar(num1)