'''cod_estado = int(input("Digite o código do estado (1 a 5): "))
peso_carga_tone = float(input("Digite o peso da carga do caminhão em toneladas: "))
cod_carga = int(input("Digite o código da carga (10 a 40"))
peso_carga_kg = peso_carga_tone * 1000
preco_carga = 0
preco = 0
imposto_estado = 0
imposto = 0
valor_total = 0
if cod_estado ==1:
    imposto_estado = 35
    if 10 <= cod_carga <20:
        preco = 100
    elif 20 <= cod_carga <30:
        preco = 250
    elif 30 <= cod_carga <40:
        preco = 340
    preco_carga = preco *peso_carga_kg
    imposto = preco_carga * (imposto_estado /100)
    valor_total = preco_carga - imposto
elif cod_estado == 2:
    imposto = 25

    '''



