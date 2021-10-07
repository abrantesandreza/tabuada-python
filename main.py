#Tabuada em laço de repetição WHILE:
numero = int(input('Digite o número para calcular sua tabuada: '))
x = 1
while (x <= 10):
    print('{} x {} = {}'.format(numero, x, numero*x))
    x += 1

#Tabuada em laço de repetição FOR:
numero = int(input('DIgite um número inteiro para calcular sua tabuada: '))
for i in range (1, 11, 1):
    print('{} x {} = {}'.format(numero, i, numero*i))
    
