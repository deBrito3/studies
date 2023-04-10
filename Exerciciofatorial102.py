def fat(num=1, show=False):
    """ -> Calcula o Fatorial de um número
        :param num: Número a ser calculado
        :param show: Escolhe mostra a conta ou não. (Opcional)
        :return: O valor fatorial de um número n.
    """
    f = 1
    for i in range(num, 0, -1):
        f = f * i
        if show:
            print(f'{i}' , end='')
            if i > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')

    print(f)


fat(5, True)
