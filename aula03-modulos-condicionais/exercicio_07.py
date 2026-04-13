ano_nasc = int(input("Digite o ano de nascimento: "))
ano_atual = 2026
idade = ano_atual - ano_nasc


if idade <0:
    print(f"Digite um ano de nascimento valido")
elif 16 <= idade <= 17 or idade >70:
    print(f"Seu voto é opcional")
elif idade < 16:
    print(f"Você ainda não pode votar!")
else:
    print(f"Seu voto é obrigatório!")