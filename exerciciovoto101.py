def voto(y):
    from datetime import date
    if y <= 0:
        print('O ano digitado é invalido')
    else:
        current_year = int(date.today().year)
        idade = current_year - year
        print(f'Com {idade} anos: ', end='')
        if 16 > idade:
            print('Você não vota')
        elif 16 <= idade < 18 or idade > 64:
            print('O voto é opcional')
        else:
            print('O voto é obrigatório')


year = int(input('Digite o ano do nascimento:'))
voto(year)
