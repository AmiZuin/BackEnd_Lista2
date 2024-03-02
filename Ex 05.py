from datetime import datetime

class Data:
    def metodo(self, dt1, dt2):
        return dt1 - dt2

obj = Data()

print("Informe a primera data: (ex: 28-02-2023)")
dt1 = input()
print(30*"-")
print("Informe a segunda data: (ex: 10-02-2023)")
dt2 = input()
print(30*"-")

dt1_att = datetime.strptime(dt1, "%d-%m-%Y")
dt2_att = datetime.strptime(dt2, "%d-%m-%Y")

resultado = obj.metodo(dt1_att, dt2_att)

print("A diferença de dias é: ", resultado)