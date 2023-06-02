def calcular_salario(x, y):
    z = (x * y) + 5

    if z <= 0:
        resposta = 'A'
    else:
        if z <= 100:
            resposta = 'B'
        else:
            resposta = 'C'

    return z, resposta

coords = [(3, 2), (150,3), (7, -1), (-2, 5), (50, 3)]

for (x, y) in coords:
    z, resposta = calcular_salario(x, y)
    print("{:d} & {:d} & {:d} & {:s} \\\\".format(int(x), int(y), int(z), str(resposta)))
    print("\\hline")
