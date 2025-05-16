# Atividade 01
# Titulo: Calcular a média e informar se o aluno foi aprovado.
# obs: Criar um programa que peça duas notas ao usuário.

print('SEJA BEM-VINDO!!!')
print('=== BOLETIM ESCOLAR ===')


# Aprovado = 6, 7, 8, 9, 10
# Reprovado = 1, 2, 3, 4, 5

while True:
    try:
        n1 = float(input('Informe a sua nota: '))
        n2 = float(input('Informe a sua nota: '))

    except ValueError as e:
        print(f'Não digite por extenso, por favor. - {e}')

    else:
        if 0 <= n1 <= 10 and 0 <= n2 <= 10:
            media = (n1 + n2) / 2
            if media >= 6:
                print('Média do aluno: {lenn:.2f}')
                print('APROVADO')
            elif media < 6:
                print('Média do aluno: {lenn:.2f}')
                print('REPROVADO')
        elif n1 < 0 or n2 < 0:
            if n1 < 0:
                print('Valor inválido. Nota 1 deve conter valor maior que 0.')
            elif n2 < 0:
                print('Valor inválido. Nota 2 deve conter valor maior que 0.')
            elif n2 < 0:
                print('Valor inválido. Nota 2 deve conter valor maior que 0.')    

        

    finally:
        print('Obrigado por estudar na nossa escola')
        break 
