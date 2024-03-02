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
    
obj = ValidarDados()

print("Digite seu CPF: (Ex: 111.111.111-11)")
cpf = input()
print(30*"-")

resultado = obj.validar_cpf(cpf)

if resultado == False:
    print("CPF inválido!")

else:
    print("CPF válido!")
