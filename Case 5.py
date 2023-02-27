'''
Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''


# Definindo a string a ser invertida
string = str(input('Escreva qualquer coisa: '))

# Invertendo os caracteres da string
string_invertida = ""
for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

# Imprimindo a string invertida
print(string_invertida)