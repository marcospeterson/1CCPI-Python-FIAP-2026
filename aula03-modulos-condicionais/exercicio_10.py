print("A seguir digite os lados de um triângulo em ordem decrescente.")

lado_a = float(input("Digite o lado A de um triângulo: "))
lado_b = float(input("Digite o lado B de um triângulo: "))
lado_c = float(input("Digite o lado C de um triângulo: "))

if lado_a >= lado_b + lado_c:
    print("Os valores dos lados digitados não formam um triângulo!")
else:
        if lado_a**2 == lado_b**2 + lado_c**2:
            print("Triângulo retângulo;")
        elif lado_a**2 > lado_b**2 + lado_c**2:
            print("Triângulo obtusângulo;")
        elif lado_a**2 < lado_b**2 + lado_c**2:
            print("Triângulo acutângulo;")


if lado_a == lado_b == lado_c:
    print("Triângulo equilátero;")
elif lado_a == lado_b or lado_b == lado_c or lado_c == lado_a:
    print("Triângulo isósceles;")

