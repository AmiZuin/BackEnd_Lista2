class Contagem:
    def contaPrimos(self, n1, n2):
        primos = []

        for numero in range(n1, n2 + 1):
            if self.eh_primo(numero):
                primos.append(numero)

        return len(primos)

    def eh_primo(self, numero):
        if numero < 2:
            return False

        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False

        return True

#Classe
class numeros:
    def __init__(self, n1, n2):
        self.__n1 = n1
        self.__n2 = n2

#Encapsulamento
    def get_n1(self):
        return self.__n1
    
    def set_n1(self, novo_n1):
        self.__n1 = novo_n1

    def get_n2(self):
        return self.__n2
    
    def set_n2(self, novo_n2):
        self.__n2 = novo_n2

    
#Objetos
num = numeros(10, 15)

print("##### O Primeiro Número deve ser Menor que o Segundo #####")
novo_n1 = int(input("Digite o Primeiro Número: "))
print(30*"-")
novo_n2 = int(input("Digite o Segundo Número: "))
print(30*"-")

num.set_n1(novo_n1)
num.set_n2(novo_n2)

obj = Contagem()
resultado = obj.contaPrimos(num.get_n1(), num.get_n2())

print(f"A quantidade de Números Primos entre {num.get_n1()} e {num.get_n2()} é: {resultado}")


