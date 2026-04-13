nota1 = float(input("Digite sua primeira nota parcial: "))
nota2 = float(input("Digite sua segunda nota parcial: "))
nota3 = float(input("Digite sua terceira nota parcial: "))
nota4 = float(input("Digite sua quarta nota parcial: "))

media = nota1 + nota2 + nota3 + nota4

if media <0 or media >10:
    print(f"Digite números válidos")
elif 5 <= media <= 10:
    print(f"Aprovado")
elif media >=5  <7:
    print(f"recuperação")
else:
    print(f"Reprovado")
