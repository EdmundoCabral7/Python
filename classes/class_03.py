# Herança

class Funcionario:
    def __init__(self, nome, cpf, salario):
        self.nome = nome
        self.cpf = cpf
        self.salario = salario

    def exibir(self):
        print(f"{self.nome} - {self.cpf}")

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, setor):
        super().__init__(nome, cpf, salario)
        self.setor = setor

    def exibir(self):
        print(f"{self.nome} - Setor: {self.setor}")


g = Gerente("Ana", "000.000.000-00", 8000, "TI")
print(g.nome) 
print(g.setor) 

# Sobrescrita de métodos

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def calcular_pagamento(self):
        return self.salario

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus):
        super().__init__(nome, salario)
        self.bonus = bonus

    def calcular_pagamento(self): 
        return self.salario + self.bonus 

f = Funcionario("Bruno", 3000)
g = Gerente("Ana", 8000, 2000)
print(f.calcular_pagamento()) 
print(g.calcular_pagamento()) 

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus, setor):
        super().__init__(nome, salario)
        self.bonus = bonus
        self.setor = setor

    def calcular_pagamento(self):
        return self.salario + self.bonus

    def exibir(self):
        print(f"Setor: {self.setor}")

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus, setor):
        super().__init__(nome, salario)
        self.bonus = bonus
        self.setor = setor

    def exibir(self):
        super().exibir() 
        print(f"Setor: {self.setor}")

g = Gerente("Ana", 8000, 2000, "TI")
print(type(g)) 
print(isinstance(g, Gerente)) 
print(isinstance(g, Funcionario))
f = Funcionario("Bruno", 3000)
print(isinstance(f, Gerente)) 