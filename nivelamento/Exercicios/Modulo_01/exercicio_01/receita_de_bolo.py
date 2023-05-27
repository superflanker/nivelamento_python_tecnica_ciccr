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

"""
Ingredientes:
1 copo de fubá mimoso
1 copo de farinha de trigo
1 copo de leite
1 e 1/2 copos de açúcar
1 xícara de óleo
3 ovos
1 colher de fermento em pó
semente de erva-docesementes de erva doce a gosto 
"""

def reservar_liquidificador(n):
    print("Separando um liquidificador de {:.02f} litros para preparo da receita de bolo".format(n))

def pre_aquecimento(n):
    print("Pré-aquecendo o forno a {:.02f} graus".format(200))

def adicionar_fuba_mimoso(n):
    print("Adicionando ingrediente - fubá mimoso ({:.02f} copo(s))".format(n))

def adicionar_farinha_de_trigo(n):
    print("Adicionando ingrediente - farinha de trigo ({:.02f} copo(s))".format(n))

def adicionar_leite(n):
    print("Adicionando ingrediente - leite ({:.02f} copo(s))".format(n))

def adicionar_acucar(n):
    print("Adicionando ingrediente - açúcar ({:.02f} copo(s))".format(n))

def adicionar_oleo(n):
    print("Adicionando ingrediente - óleo ({:.02f} xicara(s))".format(n))

def adicionar_ovos(n):
    print("Adicionando ingrediente - ovos ({:.02f} ovos(s))".format(n))

def adicionar_fermento(n):
    print("Adicionando ingrediente - Fermento ({:.02f} colher(es))".format(n))

def adicionar_erva_doce(n):
    print("Adicionando ingrediente - Erva Doce ({:.02f} colher(es))".format(n))

def bater_ingredientes():
    print("Batendo todos os ingredientes")

def despejar_em_uma_forma(n):
    print("Despejando em uma forma untada")

def assando():
    print("Assando em um forno pr")

def esfriando():
    print("Esperando a forma esfriar")

def servindo():
    print("Servindo o bolo")

def receita_bolo_de_fuba():
    pre_aquecimento(200)
    reservar_liquidificador(1.5)
    adicionar_fuba_mimoso(1)
    adicionar_farinha_de_trigo(1)
    adicionar_acucar(1.5)
    adicionar_fermento(1)
    adicionar_ovos(3)
    adicionar_leite(1)
    adicionar_oleo(1)
    bater_ingredientes()
    assando()
    esfriando()
    servindo()

receita_bolo_de_fuba()