class Pessoa:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def exibir(self):
        print(f"{self.nome} - {self.cpf} - {self.idade}")

class Aluno(Pessoa):
    def __init__(self, nome, cpf, idade, matricula, curso):
        super().__init__(nome, cpf, idade)
        self.matricula = matricula
        self.curso = curso

    def exibir(self):
        super().exibir()
        print(f"Matrícula: {self.matricula} - Curso: {self.curso}")

    def situacao(self, media):
        return "Aprovado" if media >= 7 else "Reprovado"



class Professor(Pessoa):
    def __init__(self, nome, cpf, idade, siape, titulacao):
        super().__init__(nome, cpf, idade)
        self.siape = siape
        self.titulacao = titulacao

    def exibir(self):
        print(f"{self.nome} - {self.cpf} - {self.idade} - {self.siape} - {self.titulacao}")

luiz = Aluno("Luiz", "000.000.000-00", 20, "2023001", "BSI")
luiz.situacao(9.5)
wendell = Professor("Wendell", "000.000.000-01", 30, "123456", "Mestrado")

print(luiz.nome)
print(wendell.titulacao)
print(luiz.curso)
print(luiz.situacao(6.5))