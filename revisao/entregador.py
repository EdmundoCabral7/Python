"""Entregadores e a carga que cada um transporta."""


class Entregador:
    def __init__(self, nome, capacidade_kg):
        self.nome = nome
        self.capacidade_kg = capacidade_kg
        self.__carga = []

    def carga_atual(self):
        total = 0
        for e in self.__carga:
            total += e.get_peso()
        return total

    def pode_levar(self, encomenda):
        return self.carga_atual() + encomenda.get_peso() <= self.capacidade_kg

    def carregar(self, encomenda):
        if not self.pode_levar(encomenda):
            return False
        self.__carga.append(encomenda)
        return True

    def total_encomendas(self):
        return len(self.__carga)

    def __str__(self):
        return f"{self.nome} - {self.carga_atual()}/{self.capacidade_kg} kg"
