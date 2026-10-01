"""
=============================================================================
SIMULADO DE AVALIACAO PRATICA
Analise de Sistemas Orientado a Objetos — UNI-RN — 2026.2
Prof. Wendell Oliveira de Araujo

SISTEMA DE VENDA DE INGRESSOS DE CINEMA

Nome:  ______________________________________  Matricula: ______________

INSTRUCOES
  - Complete apenas os trechos marcados com # TODO.
  - NAO altere a classe Filme nem o programa de teste do final do arquivo.
  - Execute o programa quantas vezes quiser: a saida esperada esta no
    enunciado em PDF. Se a sua saida bater com ela, a questao esta correta.
  - Consulta liberada: slides das aulas, seus arquivos poo01 a poo04 e
    anotacoes. Nao e permitido consultar colegas.
=============================================================================
"""

# =============================================================================
# CLASSE FORNECIDA — nao altere
# =============================================================================

class Filme:
    def __init__(self, titulo, duracao, classificacao):
        self.titulo = titulo
        self.duracao = duracao
        self.classificacao = classificacao

    def __str__(self):
        return f"{self.titulo} ({self.duracao} min, {self.classificacao})"


# =============================================================================
# QUESTAO 1 (3,0) — Classe Ingresso com encapsulamento
#
# Crie a classe Ingresso com:
#   - construtor recebendo: comprador, preco e poltrona
#   - o preco deve ser um atributo PRIVADO
#   - get_preco()  -> devolve o preco
#   - set_preco(valor) -> so altera se o valor for maior que zero;
#                         caso contrario, exibe:
#                         Preco invalido! Deve ser maior que zero.
#   - valor() -> devolve o valor a ser pago pelo ingresso
#   - __str__() -> devolve, por exemplo:
#                  Ana Beatriz | poltrona A1 | R$ 30.00
#
# DICA: faca o __str__ usar self.valor(), e nao o atributo direto.
#       Isso sera importante na Questao 2.
# =============================================================================

class Ingresso:
    def __init__(self, comprador, preco, poltrona):
        self.comprador = comprador
        self.__preco = preco
        self.poltrona = poltrona

    def get_preco(self):
        return self.__preco

    def set_preco(self, valor):
        if valor > 0:
            self.__preco = valor
        else:
            print("Preco invalido! Deve ser maior que zero.")

    def valor(self):
        return self.__preco

    def __str__(self):
        return f"{self.comprador} | poltrona {self.poltrona} | R$ {self.valor():.2f}"


# =============================================================================
# QUESTAO 2 (2,5) — Heranca: IngressoMeiaEntrada
#
# Crie a classe IngressoMeiaEntrada, que E UM tipo de Ingresso:
#   - construtor recebendo: comprador, preco, poltrona e tipo_desconto
#     (use super() para aproveitar o construtor da superclasse)
#   - sobrescreva valor() para devolver METADE do preco
#   - sobrescreva __str__() para acrescentar o tipo de desconto ao final,
#     aproveitando a versao da superclasse. Exemplo:
#     Bruno Carvalho | poltrona A2 | R$ 15.00 (meia - estudante)
# =============================================================================

class IngressoMeiaEntrada(Ingresso):
    def __init__(self, comprador, preco, poltrona, tipo_desconto):
        super().__init__(comprador, preco, poltrona)
        self.tipo_desconto = tipo_desconto

    def valor(self):
        return self.get_preco() / 2

    def __str__(self):
        return f"{super().__str__()} (meia - {self.tipo_desconto})"
    


# =============================================================================
# QUESTAO 3 (3,0) — Classe gerenciadora Sessao
#
# Crie a classe Sessao com:
#   - construtor recebendo: filme (um OBJETO da classe Filme) e horario
#   - a colecao de ingressos deve ser um atributo PRIVADO, iniciando vazia
#   - vender(ingresso) -> adiciona o ingresso a colecao
#   - listar() -> exibe todos os ingressos, um por linha
#   - buscar(comprador) -> devolve o OBJETO ingresso encontrado, ou None
#   - total_ingressos() -> devolve a quantidade de ingressos vendidos
#   - faturamento() -> devolve a soma do valor de TODOS os ingressos
#
# ATENCAO: o faturamento deve funcionar corretamente com ingressos inteiros
#          e de meia-entrada misturados na mesma sessao.
# =============================================================================

class Sessao:
    def __init__(self, filme, horario):
        self.filme = filme
        self.horario = horario
        self.__ingressos = []

    def vender(self, ingresso):
        self.__ingressos.append(ingresso)

    def listar(self):
        for ingresso in self.__ingressos:
            print(ingresso)

    def buscar(self, comprador):
        for ingresso in self.__ingressos:
            if ingresso.comprador == comprador:
                return ingresso
        return None

    def total_ingressos(self):
        return len(self.__ingressos)

    def faturamento(self):
        return sum(ingresso.valor() for ingresso in self.__ingressos)

# =============================================================================
# QUESTAO 4 (1,5) — Justificativas
#
# Responda nos espacos abaixo, em poucas linhas, com suas proprias palavras.
#
# a) Por que a relacao entre Sessao e Ingresso e de COMPOSICAO,
#    e nao de agregacao?
#
#    R: Porque se a Sessão não existir, não vai ter um ingresso para a sessão, ou seja, o ingresso depende da sessão para existir
#
#
# b) Por que IngressoMeiaEntrada HERDA de Ingresso, em vez de TER um Ingresso
#    como atributo?
#
#    R: Porque IngressoMeiaEntrada é um tipo específico de Ingresso
#
#
# c) Onde exatamente esta o polimorfismo no metodo faturamento()?
#
#    R:  O valor() é chamado para cada ingresso individualmente, e dependendo do ingressos ser Inteiro ou Meia, vai retornar valores diferentes, é isso que permite a existência do método faturamento()
#
#
# =============================================================================


# =============================================================================
# PROGRAMA DE TESTE — nao altere nada daqui para baixo
# =============================================================================

if __name__ == "__main__":
    duna = Filme("Duna: Parte Dois", 166, "14 anos")
    sessao = Sessao(duna, "19:30")

    print("=== SESSAO ===")
    print(f"{sessao.filme} - {sessao.horario}")

    sessao.vender(Ingresso("Ana Beatriz", 30.0, "A1"))
    sessao.vender(IngressoMeiaEntrada("Bruno Carvalho", 30.0, "A2", "estudante"))
    sessao.vender(Ingresso("Carla Dias", 30.0, "B5"))
    sessao.vender(IngressoMeiaEntrada("Diego Nunes", 30.0, "B6", "idoso"))

    print("\n--- INGRESSOS VENDIDOS ---")
    sessao.listar()

    print(f"\nTotal de ingressos: {sessao.total_ingressos()}")
    print(f"Faturamento: R$ {sessao.faturamento():.2f}")

    achado = sessao.buscar("Carla Dias")
    print(f"\nBusca por 'Carla Dias': {achado}")

    perdido = sessao.buscar("Fulano")
    if perdido is None:
        print("Busca por 'Fulano': nao encontrado")

    print()
    ing = Ingresso("Teste", 20.0, "C1")
    ing.set_preco(-5)
    print(f"Preco apos tentativa invalida: R$ {ing.get_preco():.2f}")