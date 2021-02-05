import random
import math
def media(X):
    return sum(X)/len(X)

def varianza(X):
    mu=media(X)
    acumulador=0
    for i in X:
        acumulador+= (i-mu)**2
    
    return acumulador/len(X)

def desvEst(x):
    return math.sqrt(varianza(x))


if __name__== "__main__":
    x=[random.randint(1,21) for i in range (20)]
    mu=media(x)
    print(x)
    var=varianza(x)
    desv=desvEst(x)
    print(f'la media es: {mu}')
    print(f'la varainza es es: {var}')
    print(f'la desviacion estandar es: {desv}')


# import random
# import math

# def media(X):
#     return sum(X) / len(X)


# def varianza(X):
#     mu = media(X)

#     acumulador = 0
#     for x in X:
#         acumulador += (x - mu)**2

#     return acumulador / len(X)


# def desviacion_estandar(X):
#     return math.sqrt(varianza(X))


# if __name__ == '__main__':
#     X = [random.randint(1, 21) for i in range(20)]
#     mu = media(X)
#     Var = varianza(X)
#     sigma = desviacion_estandar(X)

#     print(f'Arreglo X: {X}')
#     print(f'Media = {mu}')
#     print(f'Varianza = {Var}')
#     print(f'Desviacion estandar = {sigma}')