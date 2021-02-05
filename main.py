import random
import collections
from estadistica import media, desvEst
from bokeh.plotting import figure, output_file, show 

def tirar_dado(numero_de_tiros):
    secuencia_de_tiros = []
    aux=0
    for _ in range(numero_de_tiros):
        tiro_dado_1 = random.choice([1, 2, 3, 4, 5, 6])
        tiro_dado_2 = random.choice([1, 2, 3, 4, 5, 6])
        aux= tiro_dado_1+tiro_dado_2
        secuencia_de_tiros.append(aux)

    return secuencia_de_tiros

def main(numero_de_tiros, numero_de_intentos):
    tiros = []
    estimados=[]
    for _ in range(numero_de_intentos):
        secuencia_de_tiros = tirar_dado(numero_de_tiros)
        med_d=media(secuencia_de_tiros)
        estimados.append(med_d)
        tiros.append(secuencia_de_tiros)
    
    counter = dict(collections.Counter(estimados))
    x=list(counter.keys())
    y=list(counter.values())

    graficar(x,y)
    # print(f'{counter.keys()}')
    
def graficar(x,y):
    plot=figure(title="Distribucion Normal")
    plot.vbar(x, top=y, width=0.3, color="#161d6f")
    output_file("vertical_bar.html")
    show(plot)
    
    
if __name__ == '__main__':
    numero_de_tiros = int(input('Cuantas tiros del dado: '))
    numero_de_intentos = int(input('Cuantas veces correra la simulacion: '))

    main(numero_de_tiros, numero_de_intentos)
