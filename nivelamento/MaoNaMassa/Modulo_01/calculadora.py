"""
Calculadora simples para exemplificar os conceitos vistos no módulo 01
@author Augusto Mathias Adams <augusto.mathias@sesp.pr.gov.br>

MIT License

Copyright (c) 2023 Augusto Mathias Adams

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN
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

q = ord('a')

while q != 'q':
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

    print("Pressione qualquer tecla para continuar, q para sair")

    q = input()
