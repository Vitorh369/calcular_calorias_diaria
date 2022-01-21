def valida_int(pergunta , min, max):
    x = int(input(pergunta))
    while ((x < min) or ( x > max)):
        x =int(input(pergunta))
    return x

while True:
    varialvel_homem = 11
    variavel_mulher = 10

    atividades_leves_durante_dia = 1.1
    atividades_moderadas_durante_dia = 1.3
    atividade_intensa_durante_o_dia = 1.5

    peso = float(input('\nQual seu peso?'))
    genero = int(input('Qual seu sexo? 1 Homem ou 2 Mulher? selecione uma das opçoes!'))

    if (genero == 1):
        genero = 2.205 * peso * varialvel_homem


    elif (genero == 2):
        genero = 2.205 * peso * variavel_mulher

    else:
        print('\n Digite as opcões corretamente!')
        continue


    print('1 - Atividade leves, durante o dia;')
    print('2 - Atividades moderada, durante o dia;')
    print('3 - atividades intensas, durante o dia;')
    atividades_durante_o_dia = valida_int('Com as seguintes opçoes, como é seu dia?', 1, 3)


    kcal_diario = genero
    if (atividades_durante_o_dia == 1):
        kcal_diario *= atividades_leves_durante_dia
        print('suas calorias diarias são {:4.2f}'.format(kcal_diario))

    elif (atividades_durante_o_dia == 2):
        kcal_diario *= atividades_moderadas_durante_dia
        print('suas calorias diarias são {:4.2f}'.format(kcal_diario))

    elif (atividades_durante_o_dia == 3):
        kcal_diario *= atividade_intensa_durante_o_dia
        print('suas calorias diarias são {:4.2f}'.format(kcal_diario))
