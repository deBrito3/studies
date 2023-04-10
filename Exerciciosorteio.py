from random import randrange
from time import sleep


def raffle(rol):
    i = 0
    print("Sorteando os valores da lista: ", end='')
    while i < 5:
        rol.append(randrange(11))
        print(f'{rol[i]} ', end='')
        sleep(0.3)
        i += 1
    print("Pronto!")


def pair(rol):
    print(f'Somando os valores pares de {rol} temos: ', end='')
    soma = 0
    for i in rol:
        resto = i % 2
        if resto == 0:
            soma = soma + i
    print(soma)


rol = list()
raffle(rol)
pair(rol)
