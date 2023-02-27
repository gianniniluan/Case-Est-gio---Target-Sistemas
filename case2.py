'''
Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,informado um número,
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
'''


num =  30   #Quantidade de sequências na lista
i1 =  0     #Primeiro indice da sequência
i2 = 1      #Segundo indice da sequência
cont = 3    #Iniciação do contador

lista = [i1, i2]   #Lista iniciada

while cont <= num:  #Enquanto o contador for menor ou igual o número inserido, o looping executará
    i3 = i1 + i2    #Sequência Fibonacci / O proxímo valor da lista será a soma dos dois números anteriores
    lista.append(i3)    #Adicionando o resultado da soma na lista criada
    i1 = i2     #Realocando o indice para a sequência do looping
    i2 = i3     #Realocando o indice para a sequência do looping
    cont += 1     #Será somado 1 ao contador toda vez que o looping for realizado

num_ehfib = int(input('Insira o número que você deseja saber se está na lista de Fibonacci: '))
print('-'*30)

if num_ehfib in lista:     #Se o número inserido pelo usuário estiver na lista, o programa executará o código abaixo
    print(f'O número {num_ehfib} está na lista!')
else:     #Se não estiver na lista, o programa executará o código abaixo
    print(f'O número {num_ehfib} não está na lista!')

print('-'*30)
print(f'A sequência de Fibonacci é: {lista}')