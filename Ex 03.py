import math

class Sobrecarga():
    def metodo(self, *valores):
        if len(valores) == 1 and isinstance(valores[0], float):
            raio = valores[0]
            area = math.pi * raio**2
            print(f'A área do circulo é: {area}')

        elif len(valores) == 2 and all(isinstance(valor, float) for valor in valores):
            lado = valores[0]
            area = lado ** 2
            print(f'A área do quadrado é: {area}')

        elif len(valores) == 3 and all(isinstance(valor, int) for valor in valores):
            a, b, c = valores
            perimetro = a + b + c
            print(f'O perímetro do triangulo é: {perimetro}')

        elif len(valores) == 2 and all(isinstance(valor, (float, int)) for valor in valores):
            base = valores[0]
            altura = valores[1]
            area = 0.5 * base * altura
            print(f'A área do triangulo é: {area}')

        elif len(valores) == 6:
            x1, y1 = valores[0], valores[1]
            x2, y2 = valores[2], valores[3]
            x3, y3 = valores[4], valores[5]
            area = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
            print(f'A área do triangulo é: {area}')

        else:
            print("Uso incorreto")

obj = Sobrecarga()

obj.metodo(1.5)
print(50*"-")
obj.metodo(2.5, 3.5)
print(50*"-")
obj.metodo(2, 5, 7)
print(50*"-")
obj.metodo(2, 3.5)
print(50*"-")
obj.metodo(2, 3, -1, 5, 4, -2)
print(50*"-")
obj.metodo("Hello Word!")


