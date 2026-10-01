"""Localizacao geografica usada no calculo de frete e prazo."""


class Cidade:
    def __init__(self, nome, uf, distancia_km):
        self.nome = nome
        self.uf = uf
        self.distancia_km = distancia_km

    def __str__(self):
        return f"{self.nome}/{self.uf}"


class Destinatario:
    def __init__(self, nome, telefone, cidade):
        self.nome = nome
        self.telefone = telefone
        self.cidade = cidade

    def __str__(self):
        return f"{self.nome} ({self.cidade})"
