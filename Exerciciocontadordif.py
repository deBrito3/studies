from time import sleep


def contador(init, fin, p):
    if p < 0:
        p *= -1
    print(f'Contagem de {init} até {fin} de {p} em {p}')

    if init < fin:
        cont = init
        while cont <= fin:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.2)
            cont += p
        print("Fim")
    else:
        cont = init
        while cont >= fin:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.2)
            cont -= p
        print("Fim")


contador(1, 10, 1)
contador(10, 1, -2)
print("Agora é sua vez de personalizar:")
init = int(input("Início:"))
fin = int(input("Final:"))
p = int(input("Passo:"))
contador(init, fin, p)
