from math import pow, pi

#Fórmula para calculo da área do quadrado.
def areaQuadrado(valor):
    return pow(valor, 2)

#Fórmula para calculo da área do retângulo.
def areaRetangulo(b, h):
    return b * h

#Fórmula para calculo da área do círculo.
def areaCirculo(raio):
    return pi * pow(raio, 2)

#Fórmula para calculo da área do.
def areaTriangulo(base, altura):
    return base * altura / 2