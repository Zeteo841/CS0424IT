# Molto veloce, molto semplice, molto compatto

import sys

pi = 3.1415 

def Introduzione():
    print(f"*\nCiao, sono un programma che aiuta a calcolare il perimetro di diverse forme geometriche, scegli la forma ed io calcolero' il perimetro\n")
    
def Menu():
    print(f"***************MENU*****************\n")
    print(f"\tA) Quadrato\n")
    print(f"\tB) Cerchio\n")
    print(f"\tC) Rettangolo\n")
    print(f"\tD) Esci dal programma\n")
    
def Quadrato(l):
    perimetro = l * 4
    return perimetro

def Cerchio(r):
    perimetro = 2 * pi * r
    return perimetro

def Rettangolo(M, m):
    perimetro = ((2 * M) + (2 * m))
    return perimetro

def Main():
    Introduzione()
    while True:
        Menu()
        forma = input("Scegli una forma a tua piacimento: ").strip().upper()
    
        while forma not in ['A', 'B', 'C','D']:
         forma = input("Scelta non valida. Scegli 'A', 'B' o 'C': ").strip().upper()
        
        if forma == 'A':
            lato = float(input("Perfetto, hai scelto il quadrato!\nChe lunghezza ha un suo lato? "))
            print(f"Il perimetro del quadrato è: {Quadrato(lato)}\n")
        elif forma == 'B':
            raggio = float(input("Perfetto, hai scelto il cerchio!\nChe lunghezza ha il suo raggio? "))
            print(f"Il perimetro del cerchio è: {Cerchio(raggio)}\n")
        elif forma == 'C':
            M = float(input("Perfetto, hai scelto il rettangolo!\nChe lunghezza ha il suo lato maggiore? "))
            m = float(input("Che lunghezza ha il suo lato minore? "))
            print(f"Il perimetro del rettangolo è: {Rettangolo(M, m)}\n")
        elif forma == 'D':
            print("Uscita dal programma...") 
            sys.exit(1)
    
Main()
        
    

    
    