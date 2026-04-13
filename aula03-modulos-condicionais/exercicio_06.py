num1 = float(input("Digite um número para fazer uma operação matemática: "))
num2 = float(input("Digite outro número para fazer a operação: "))
caracter = input ("Digite a operação na qual quer fazer! /, *, +,-: ")

if caracter not in["+","-","*","/"]:
    print(f"Digite uma operação válida!")
elif caracter == "+":
    print(f"a soma de {num1} e {num2} é igual a: {num1+num2} ")
elif caracter == "-":
    print(f"a subtração de {num1} e {num2} é igual a: {num1 - num2} ")
elif caracter == "*":
    print(f"a multiplicação de {num1} e {num2} é igual a: {num1 * num2} ")
elif caracter == "/":
    if num2 == 0:
        print("Não é possível dividir por zero!")
else:
    print(f"a divisão de {num1} e {num2} é igual a: {num1 / num2:.2f} ")
