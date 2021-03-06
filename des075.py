print('DESAFIO 75'.center(40))
'''
Ler 4 valores pelo teclado e guardar em uma tupla. Após isso, mostre:
a) quais foram os números pares / b) quantas vezes apareceu o valor 9 / c) em que posição foi digitado o primeiro valor 3
'''
print()
numbers = ((int(input('Digite um número: '))),
           (int(input('Digite outro número: '))),
           (int(input('Digite o terceiro número: '))),
           (int(input('Digite o último número:  '))))
print(f'\n\033[1mOs números digitados foram: {numbers}\033[m')

pares = 'Blank'
for cont in range(0, 3+1):
    #print(numbers[verificador])
    if (numbers[cont] % 2) == 0:
        if pares == 'Blank':
            pares = str(numbers[cont])
        else:
            pares = pares + ', ' + str(numbers[cont])
if pares == "Blank":
    print('Não foram digitados valores pares.'.rjust(40))
else:
    print(f'\033[1;40;7m Os números pares são: {pares} \033[m'.rjust(52))

nrepeat = int(input('\n* Qual número deseja contar: '))
qtdrepeat = numbers.count(nrepeat)
if qtdrepeat == 0:
    print(f'O número {nrepeat} não aparece na listagem.'.rjust(40))
else:
    print(f'\033[1;40;7m O número {nrepeat} apareceu {qtdrepeat} vez(es). \033[m'.rjust(52))

nsearch = int(input('\n* Qual número deseja localizar: '))
if nsearch not in numbers:
    print(f'Número {nsearch} não localizado nenhuma posição.'.rjust(40))
else:
    print(f'\033[1;40;7m Número {nsearch} localizado na posição {numbers.index(nsearch)+1} \033[m'.rjust(52))

print()
print('Analisador encerrado. Volte sempre.'.center(40))

