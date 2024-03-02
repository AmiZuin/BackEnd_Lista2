import re

class ValidarDados:
    def validar_cpf(self, cpf):
        padrao_cpf = r'^\d{3}\.?\d{3}\.?\d{3}-?\d{2}$'

        if not re.match(padrao_cpf, cpf):
            return False
        
        numeros = re.sub(r'\D', '', cpf)

        if len(set(numeros)) == 1:
            return False
        
        cpf_numeros = [int(digito) for digito in numeros[:-2]]
        primeiro_digito_verificador = int(numeros[-2])
        segundo_digito_verificador = int(numeros[-1])

        soma = 0
        for i, digito in enumerate(cpf_numeros):
            soma += digito * (10 - i)

        resto_divisao = soma % 11

        if resto_divisao < 2:
            primeiro_digito_calculado = 0
        else:
            primeiro_digito_calculado = 11 - resto_divisao

        if primeiro_digito_calculado != primeiro_digito_verificador:
            return False

        cpf_numeros.append(primeiro_digito_calculado)
        soma = 0

        for i, digito in enumerate(cpf_numeros):
            soma += digito * (11 - i)

        resto_divisao = soma % 11

        if resto_divisao < 2:
            segundo_digito_calculado = 0
        else:
            segundo_digito_calculado = 11 - resto_divisao

        return segundo_digito_calculado == segundo_digito_verificador

#Classe
class Clientes:
    def __init__(self, nome, endereco, cep, cpf):
        self.__nome = nome
        self.__endereco = endereco
        self.__cep = cep
        self.__cpf = cpf

#Encapsulamento
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, novo_nome):
        self.__nome = novo_nome
    
    def get_endereco(self):
        return self.__endereco
    
    def set_endereco(self, novo_endereco):
        self.__endereco = novo_endereco
    
    def get_cep(self):
        return self.__cep
    
    def set_cep(self, novo_cep):
        self.__cep = novo_cep
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, novo_cpf):
        self.__cpf = novo_cpf
    

#Objetos
cliente = Clientes('Arthur', 'Rua Castro Alves', '18.968-980', '798.462.874-66')

while True:
    print("1 - Exibir dados do Cliente")
    print("2 - Mudar dados do Cliete")
    print("3 - Finalizar Sessão")
    escolha = int(input())
    print(30*"-")

    if escolha == 1:
        #Método de Acesso
        print("Nome: ", cliente.get_nome())
        print("Endereço: ", cliente.get_endereco())
        print("CEP: ", cliente.get_cep())
        print("CPF: ", cliente.get_cpf())
        print(30*"-")

    elif escolha == 2:
        while True:
            novo_nome = input("Nome: ")
            novo_endereco = input("Endereço: ")
            novo_cep = input("CEP: ")
            novo_cpf = input("CPF: ")
            print(30*"-")

            resultado = ValidarDados()

            if novo_nome != "":
                cliente.set_nome(novo_nome)
            
            if novo_endereco != "":
                cliente.set_endereco(novo_endereco)

            if novo_cep != "":
                cliente.set_cep(novo_cep)

            if novo_cpf != "":
                if resultado.validar_cpf(novo_cpf) == False:
                    print(f'O CPF {novo_cpf} é inválido. Insira os dados novamente.')

                else:
                    cliente.set_cpf(novo_cpf)
                    break

            else:
                break
        
    else:
        break