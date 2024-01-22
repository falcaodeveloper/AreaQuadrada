'''Crie um programa que calcule as áreas das seguintes figuras geométricas:
1-) Quadrado;
2-) Retângulo;
3-) Círculo;
4-) Triângulo.
O usuário deverá digitar as letras "Q" ou "R" para quadrado ou retângulo, "C" para círculo e "T" para triângulo.'''
#Desenvolvido por Ulisses F. Falcão em 15/01/2024

import moduloArea as m

mensagem = 'Digite a letra "Q" para quadrado, "R" para retângulo, "C" para círculo e "T" para triângulo.\n'
invalido = 'Você digitou uma letra INVÁLIDA.'
erro = 'Preste ATENÇÃO ao que é solicitado! Reinicie o programa.'
entrada = input(mensagem).strip().upper()
verdadeiro = entrada.isalpha()
caracteres = len(entrada)
if verdadeiro == True and caracteres == 1:
    if entrada == 'Q':
        comprimento = float(input('Digite o tamanho de um dos lados do quadrado: '))
        print('Área do quadrado: {:.2f}' .format(m.areaQuadrado(comprimento)))
    elif entrada == 'R':
        base = float(input('Digite o valor da base: '))
        altura = float(input('Digite o valor da altura: '))
        print('A área do retângulo é: {:.2f}' .format(m.areaRetangulo(base, altura)))
    elif entrada == 'C':
        raio = float(input('Digite o comprimento do raio: '))
        print('A área do círculo é: {:.2f}' .format(m.areaCirculo(raio)))
    elif entrada == 'T':
        base = float(input('Digite o comprimento da base do triângulo: '))
        altura = float(input('Digite o comprimento da altura do triângulo: '))
        print('A área do triângulo é: {:.2f}' .format(m.areaTriangulo(base, altura)))
    else:
        print('{}\n{}{}' .format(invalido, mensagem, erro))
else:
    print(erro)
    