salario = float(input("Digite o valor do seu salário: "))
percentual = 0
novo_salario= 0

if salario <= 0:
    print(f"Digite um salário válido!")
else:
    if 0 < salario <= 280:
        percentual = 20
        novo_salario = salario + (salario * percentual/100)
    elif 280 < salario <= 700:
        percentual = 15
        novo_salario = salario + (salario * percentual/100)
    elif 700 < salario <= 1500:
        percentual = 10
        novo_salario = salario + (salario * percentual/100)
    else:
        percentual = 5
        novo_salario = salario + (salario * percentual/100)

    print(f"Salário antes do reajuste: {salario}")
    print(f"O percentual aplicado foi de {percentual}%")
    print(f"O valor do aumento foi de {novo_salario - salario:.2f}")
    print(f"O novo salário após o aumento é de: {novo_salario}")

