cod_estado = int(input("Digite o código do estado (1 a 5): "))
peso_carga_tone = float(input("Digite o peso da carga do caminhão em toneladas: "))
cod_carga = int(input("Digite o código da carga (10 a 40): "))
peso_carga_kg = peso_carga_tone * 1000
imposto = 0
preco_por_kg = 0

if cod_estado ==1:
    imposto = 35
elif cod_estado == 2:
    imposto = 25
elif cod_estado == 3:
    imposto = 15
elif cod_estado ==4:
    imposto = 5
else:
    imposto = 0


if 10 <= cod_carga <=20:
    preco_por_kg =100
elif 21 <= cod_carga  <=30:
    preco_por_kg = 250
elif 31 <= cod_carga <=40:
    preco_por_kg = 340

preco_carga = preco_por_kg * peso_carga_kg


print(f"O peso da carga do caminhão convertido em quilos é igual a: {peso_carga_kg} kg.")
print (f"O preço da carga do caminhão é de: R${preco_carga:.2f}")
print (f"O percentual do imposto foi de {imposto}%, totalizando R${preco_carga*(imposto/100):.2f} de imposto.")
print (f"O valor total transportardo foi de: R${preco_carga + (preco_carga*(imposto/100)):.2f}")