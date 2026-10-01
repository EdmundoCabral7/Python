"""Nucleo do sistema: cadastro, despacho e relatorios."""

from encomendas import EncomendaPadrao, EncomendaExpressa


class Transportadora:
    def __init__(self, nome):
        self.nome = nome
        self.__encomendas = []
        self.__entregadores = []

    def cadastrar(self, encomenda):
        if self.buscar(encomenda.codigo) is not None:
            print(f"Codigo {encomenda.codigo} ja cadastrado.")
            return False
        self.__encomendas.append(encomenda)
        return True

    def contratar(self, entregador):
        self.__entregadores.append(entregador)

    def buscar(self, codigo):
        for e in self.__encomendas:
            if e.codigo == codigo:
                return e
        return None

    def despachar(self, codigo, entregador):
        enc = self.buscar(codigo)
        if enc is None:
            print(f"Encomenda {codigo} nao encontrada.")
            return False
        if enc.get_status() != "Aguardando coleta":
            print(f"Encomenda {codigo} ja foi despachada.")
            return False
        if not entregador.carregar(enc):
            print(f"{entregador.nome} nao tem capacidade para {codigo}.")
            return False
        enc.avancar_status()
        return True

    def confirmar_entrega(self, codigo):
        enc = self.buscar(codigo)
        if enc is not None and enc.get_status() == "Em rota":
            enc.avancar_status()
            return True
        return False

    def faturamento(self):
        total = 0
        for e in self.__encomendas:
            total += e.calcular_frete()
        return total

    def contar_por_tipo(self):
        padrao = 0
        expressas = 0
        frageis = 0
        for e in self.__encomendas:
            if isinstance(e, EncomendaExpressa):
                expressas += 1
            elif isinstance(e, EncomendaPadrao):
                padrao += 1
            else:
                frageis += 1
        return padrao, expressas, frageis

    def relatorio(self):
        print(f"===== {self.nome} =====")
        for e in self.__encomendas:
            print(e)
        padrao, expressas, frageis = self.contar_por_tipo()
        print(f"Padrao: {padrao} | Expressa: {expressas} | Fragil: {frageis}")
        print(f"Faturamento previsto: R$ {self.faturamento():.2f}")
        print("--- Entregadores ---")
        for ent in self.__entregadores:
            print(ent)
