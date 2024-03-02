import math

class Calculadora:
    def soma(self, valor, valor2):
        return valor + valor2
        

    def subtracao(self, valor, valor2):
        return valor - valor2
        

    def multiplicacao(self, valor, valor2):
        return valor * valor2
        

    def radiciacao(self, valor):
        return math.sqrt(valor)
        

    def fatorial(self, valor):
        if valor == 1:
            return 1
        else:
            return valor * self.fatorial(valor - 1)
        
calculo = Calculadora()

resultado_soma = calculo.soma(5, 5)
resultado_subtracao = calculo.subtracao(5, 5)
resultado_multiplicacao = calculo.multiplicacao(5, 5)
resultado_radiciacao = calculo.radiciacao(4)
resultado_fatorial = calculo.fatorial(5)

print(f'O resultado da Soma é: {resultado_soma}')
print(50*"-")
print(f'O resultado da Subtração é: {resultado_subtracao}')
print(50*"-")
print(f'O resultado da Multiplicação é: {resultado_multiplicacao}')
print(50*"-")
print(f'O resultado da Radiciação é: {resultado_radiciacao}')
print(50*"-")
print(f'O resultado do Fatorial é: {resultado_fatorial}')


