# Calcular 2 notas mostrar média
print('='*5, ' DESAFIO 07 ', '='*5)
av1 = float(input('Informe a nota referente a avaliação 1: '))
av2 = float(input('Informe a nota para a avaliação 2: '))
m = (av1 + av2) / 2

print()
print('\033[7;40;1mA média do aluno é {:.1f}.\033[m' .format(m))

