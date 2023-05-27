"""
Calculadora simples para exemplificar os conceitos vistos no módulo 01
@author Augusto Mathias Adams <augusto.mathias@sesp.pr.gov.br>
"""

# definição de operações da calculadora

def soma(a, b):
    """
    Efetua a Soma dos Números a e b
    Args:
        a (real): número a
        b (real): número b
    Returns:
        real: a soma de a e b
    """
    s = a + b
    return s

def subtrai(a, b):
    """
    Efetua a Subtração dos Números a e b
    Args:
        a (real): número a
        b (real): número b
    Returns:
        real: a subtração de a e b
    """
    s = a - b
    return s

def multiplica(a, b):
    """
    Efetua a multiplicação dos Números a e b
    Args:
        a (real): número a
        b (real): número b
    Returns:
        real: a multiplicação de a e b
    """
    s = a * b
    return s

def divide(a, b):
    """
    Efetua a divisão dos Números a e b
    Args:
        a (real): número a
        b (real): número b
    Returns:
        real: a multiplicação de a e b
    """
    try:
        s = a / b
        return s
    except ZeroDivisionError as e:
        print("Não é possível divisão por zero")


# loop principal

while True:
    # entrada de operandos e a operação - Notação Polonesa 

    print("Digite o primeiro operando: ")
    try:
        opa = float(input())
    except ValueError as e:
        print("Somente números são permitidos")
        continue

    print("Digite o segundo operando: ")
    try:
        opb = float(input())
    except ValueError as e:
        print("Somente números são permitidos")
        continue

    print("Informe o tipo de operação(0 - Soma; 1 - Subtração. 2 - Multiplicação; 3 - Divisão): ")
    try:
        op = int(input())
    except ValueError as e:
        print("Somente números inmteiros são permitidos")
        continue

    # análise e execução de operação

    if op == 0:
        print(soma(opa, opb))
    elif op == 1:
        print(subtrai(opa, opb))
    elif op == 2:
        print(multiplica(opa, opb))
    elif op == 3:
        print(divide(opa, opb))
    else:
        print("Operação sem Suporte")