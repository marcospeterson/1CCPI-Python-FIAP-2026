from operator import truediv
from time import process_time_ns

num1 = 5
num2 = 2

print(type(num1), type(num2))

resultado_op = num1 % num2

print(resultado_op, type(resultado_op))

#OPERADORES DE ATRIBUIÇÃO
num = 15
print()#pular linha
print(num)

num = num +2 #acumulando 2
print(num)

num*=2
print(num)

#OPERADORES RELACIONADOS
print(6 !=6)

idade =20
print(idade >= 18)

logado = True
print(logado,type(logado))

maior_idade = idade >= 17
print(maior_idade, type (maior_idade))

# STRINGS...
nome1 = "Marcos"
nome2 = "marcos"

print(nome1.upper() ==nome2.upper()) #upper coloca todos em maiusculo para verificar se o texto esta igual