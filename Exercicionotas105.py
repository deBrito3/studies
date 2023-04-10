def notas(*n, sit=False):
    note = dict()
    note['Total'] = len(n)
    note['Maior'] = max(n)
    note['Menor'] = min(n)
    note['Média'] = sum(n) / len(n)
    if sit:
        if note['Média'] >= 7:
            note['Situação'] = 'Boa'
        elif note['Média'] >= 5:
            note['Situação'] = 'Razoável'
        else:
            note['Situação'] = 'Ruim'
    return note


resp = notas(3.5, 9, 10, 9, sit=True)
print(resp)
