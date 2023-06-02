"""
Receita de Bolo da Vovó
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

import random

def preaquecer_forno() -> None:
    """
    Pré-aquecendo o forno
    Args:
        None
    Returns:
        None
    """
    print("Pré-aquecendo o forno a 200 graus")

def misturar_ingredientes() -> None:
    """
    Misturar os Ingredientes em um liquidificador
    Args:
        None
    Returns:
        None
    """
    print("Misturando ingredientes em um liquidificador:")
    print("     1 copo de fubá mimoso")
    print("     1 copo de farinha de trigo")
    print("     1 e 1/2 copos de açúcar")
    print("     1 colher de fermento em pó ")
    print("     1 copo de leite")
    print("     1 xícara de óleo")
    print("     3 ovos")

def despejar_massa_na_forma() -> None:
    """
    Despejar massa na forma
    Args:
        None
    Returns:
        None
    """
    print("Despejando a massa em uma forma")

def assar_o_bolo() -> None:
    """
    Assar o Bolo
    Args:
        None
    Returns:
        None
    """
    print("Assando o bolo")

def palito_seco() -> bool:
    """
    Verifica se o palito está seco
    Args:
        None
    Returns:
        boolean
    """
    r = random.random()
    # se for menor que 1/30, simulamos palito seco
    if r < 1/30:
        print("O palito está seco")
        return True
    print("O palito ainda não está seco")
    return False

def deixar_esfriar() -> None:
    """
    Deixar Esfriar
    Args:
        None
    Returns:
        None
    """
    print("Deixando esfriar")
def polvilhar_com_erva_doce() -> None:
    """
    Polvilhar com erva doce
    Args:
        None
    Returns:
        None
    """
    print("Polvilhando com erva doce")
def servir_o_bolo() -> None:
    """
    Servir o Bolo
    Args:
        None
    Returns:
        None
    """
    print("Servindo o Bolo")


def fazer_bolo() -> None:
    """
    Fazer o bolo - wrapper do algoritmo principal
    Args:
        None
    Returns:
        None
    """
    # vamos falsear
    preaquecer_forno()
    misturar_ingredientes()
    despejar_massa_na_forma()
    assar_o_bolo()
    while not palito_seco():
        assar_o_bolo()
    deixar_esfriar()
    polvilhar_com_erva_doce()
    servir_o_bolo()

# chamada para a função fazer_bolo

fazer_bolo()
