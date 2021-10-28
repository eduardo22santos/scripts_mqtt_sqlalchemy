def print2(nome='', cpf='000.000.00-000', celular=False):
    if nome != '':
        print(nome)
    if cpf != '000.000.00-000':
        print(cpf)
    if celular == True:
        print('Celular ok')


print2(celular=True)