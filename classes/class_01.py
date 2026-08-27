# Programação orientada a objetos
# Aula 01 = Classes e Objetos

# 1. palavra-chave class + Nome. Self é parâmetro que representa a própria instância do objeto. Ele é usado para acessar variáveis que pertencem à classe.
# 2. O construtor da classe é o método __init__() que é chamado quando um objeto é instanciado
# 3. Atributo do objeto, self.nome é uma variável que vai receber o nome da função

class Aluno: 
    def __init__(self, nome, matricula, n1, n2): 
        self.nome = nome
        self.matricula = matricula
        self.n1 = n1
        self.n2 = n2

    def media (self):
        return (self.n1 + self.n2) / 2

    def esta_aprovado(self):
        return self.media() >= 7.0

luiz = Aluno("Luiz Augusto", 2026001, 8.0, 6.0)

print(luiz.nome, luiz.matricula, luiz.n1, luiz.n2)
print (luiz.media(), luiz.esta_aprovado())

#Encapsulamento

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.__n1 = 0

    def get_n1(self): # leitura controlada
        return self.__n1
    def set_n1(self, valor): # escrita COM VALIDAÇÃO
        if 0 <= valor <= 10:
            self.__n1 = valor
        else:
            print("Nota inválida! Informe de 0 a 10.")

ana = Aluno("Ana")
ana.set_n1(8) # aceita
ana.set_n1(-50) # >>> Nota inválida! Informe de 0 a 10.
    