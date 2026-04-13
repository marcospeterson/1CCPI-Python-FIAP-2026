num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

if num1 ==0 or num2 == 0:
    print(f"Não é possível verificar múltiplos com 0!")
elif num1 % num2 == 0 or num2 % num1 == 0 :
    print(f"Esses números são múltiplos!")
else:
    print(f"Esses números não são múltiplos!")