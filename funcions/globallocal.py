a = 2
b = 4

def suma_si_parells(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return a + b
    else:
        return 0
    
suma_si_parells(a,b) # 6

salut = "Hola"
def saludar():
    print(salut)