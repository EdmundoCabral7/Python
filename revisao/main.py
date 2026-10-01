"""Demonstracao do sistema EntregaJa Logistica."""

from localizacao import Cidade, Destinatario
from encomendas import EncomendaPadrao, EncomendaExpressa, EncomendaFragil
from entregador import Entregador
from transportadora import Transportadora

natal = Cidade("Natal", "RN", 20)
mossoro = Cidade("Mossoro", "RN", 280)
recife = Cidade("Recife", "PE", 300)

ana = Destinatario("Ana Lima", "84 99999-0001", natal)
bruno = Destinatario("Bruno Rocha", "84 99999-0002", mossoro)
carla = Destinatario("Carla Souza", "81 99999-0003", recife)

tr = Transportadora("EntregaJa Logistica")

tr.cadastrar(EncomendaPadrao("E001", 4, ana))
tr.cadastrar(EncomendaExpressa("E002", 2, bruno))
tr.cadastrar(EncomendaFragil("E003", 5, carla, 1200.0))
tr.cadastrar(EncomendaPadrao("E004", 10, bruno))
tr.cadastrar(EncomendaPadrao("E002", 1, ana))

joao = Entregador("Joao", 15)
maria = Entregador("Maria", 8)
tr.contratar(joao)
tr.contratar(maria)

tr.despachar("E001", joao)
tr.despachar("E004", joao)
tr.despachar("E003", joao)
tr.despachar("E003", maria)
tr.despachar("E001", maria)
tr.despachar("E999", maria)

tr.confirmar_entrega("E001")

print()
tr.relatorio()
