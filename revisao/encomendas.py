"""Tipos de encomenda aceitos pela transportadora."""

from abc import ABC, abstractmethod

STATUS = ["Aguardando coleta", "Em rota", "Entregue"]


class Encomenda(ABC):
    TAXA_BASE = 5.0
    PESO_MAXIMO = 30

    def __init__(self, codigo, peso_kg, destinatario):
        self.codigo = codigo
        self.destinatario = destinatario
        self.__peso_kg = 0
        self.__etapa = 0
        self.set_peso(peso_kg)

    def get_peso(self):
        return self.__peso_kg

    def set_peso(self, peso):
        if peso <= 0 or peso > self.PESO_MAXIMO:
            print(f"Peso invalido para {self.codigo}: {peso} kg")
            return False
        self.__peso_kg = peso
        return True

    def get_status(self):
        return STATUS[self.__etapa]

    def avancar_status(self):
        if self.__etapa < len(STATUS) - 1:
            self.__etapa += 1
            return True
        return False

    def distancia(self):
        return self.destinatario.cidade.distancia_km

    @abstractmethod
    def calcular_frete(self):
        pass

    @abstractmethod
    def prazo_dias(self):
        pass

    def __str__(self):
        return (f"[{self.codigo}] {self.destinatario.nome} - "
                f"R$ {self.calcular_frete():.2f} - "
                f"{self.prazo_dias()} dia(s) - {self.get_status()}")


class EncomendaPadrao(Encomenda):
    def calcular_frete(self):
        return self.TAXA_BASE + 0.10 * self.distancia() + 2.0 * self.get_peso()

    def prazo_dias(self):
        return 1 + self.distancia() // 100


class EncomendaExpressa(EncomendaPadrao):
    ACRESCIMO = 1.8

    def calcular_frete(self):
        return super().calcular_frete() * self.ACRESCIMO

    def prazo_dias(self):
        return max(1, super().prazo_dias() // 2)


class EncomendaFragil(Encomenda):
    PERCENTUAL_SEGURO = 0.03

    def __init__(self, codigo, peso_kg, destinatario, valor_declarado):
        super().__init__(codigo, peso_kg, destinatario)
        self.valor_declarado = valor_declarado

    def calcular_frete(self):
        base = self.TAXA_BASE + 0.12 * self.distancia() + 2.5 * self.get_peso()
        seguro = self.valor_declarado * self.PERCENTUAL_SEGURO
        return base + seguro

    def prazo_dias(self):
        return 2 + self.distancia() // 100

    def __str__(self):
        return super().__str__() + " [FRAGIL]"