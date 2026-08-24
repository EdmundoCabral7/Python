# Criar minha primeira classe 
# Protegendo a classe com encapsulamento

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self._preco = preco
        self.__quantidade = quantidade

    def valor_total(self):
        return self.get_preco() * self.get_quantidade()

    def tem_estoque(self):
        return self.get_quantidade() > 0

    def get_preco(self):
        return self._preco

    def get_quantidade(self): 
        return self.__quantidade

    def set_preco(self, preco):
        if preco >= 0:
            self._preco = preco
        else:
            print("Preço inválido! Informe um valor positivo.")

    def __str__(self):
        return f"{self.nome} | R${self.get_preco():.2f} | Quantidade: {self.get_quantidade()}"

camera = Produto("Câmera", 1500.00, 5)
computador = Produto("Computador", 3000.00, 10)
celular = Produto("Celular", 2000.00, 0)

print(camera.nome, camera.get_preco(), camera.get_quantidade())
print(computador.nome, computador.get_preco(), computador.get_quantidade())
print(celular.nome, celular.get_preco(), celular.get_quantidade())
print(camera.valor_total(), camera.tem_estoque())
print(computador.valor_total(), computador.tem_estoque())
print(celular.valor_total(), celular.tem_estoque())
print(camera)
print(computador)
print(celular)

