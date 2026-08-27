# Associação

class Categoria:
    def __init__(self, nome, desconto):
        self.nome = nome
        self.desconto = desconto 
    def __str__(self):
        return f"{self.nome} | ({self.desconto}% off)"

class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria 

    def preco_final(self):
        d = self.categoria.desconto 
        return self.preco * (1 - d / 100)

papelaria = Categoria("Papelaria", 10)
p = Produto("Caderno", 25.0,
papelaria)
print(p.categoria)
print(p.preco_final())

class Pedido:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente 
        self.itens = [] 


# Agregação e composição

class ItemPedido:
    def __init__(self, produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

    def subtotal(self):
        return self.produto.preco * self.quantidade

class Pedido:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
        self.itens = [] 

    def adicionar(self, produto, qtd):
        item = ItemPedido(produto, qtd) 
        self.itens.append(item)

    def total(self):
        return sum(i.subtotal() for i in self.itens)


class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

class Turma:
    def __init__(self, codigo):
        self.codigo = codigo
        self.alunos = []
    
    def matricular(self, aluno): 
        self.alunos.append(aluno)

ana = Aluno("Ana", 2026001)
t1 = Turma("SI-4A")
t1.matricular(ana)


# A classe gerenciadora

class Estoque:
    def __init__(self):
        self.__produtos = [] 
    def cadastrar(self, produto):
        if not isinstance(produto, Produto):
            print("Só é possível cadastrar produtos.")
            return
        self.__produtos.append(produto)

    def listar(self):
        for p in self.__produtos:
            print(p)
    def buscar(self, nome):
        for p in self.__produtos:
            if p.nome == nome:
                return p
        return None

    def total_itens(self):
        return len(self.__produtos)

papelaria = Categoria("Papelaria", 10)
eletronico = Categoria("Eletrônicos", 5)

p1 = Produto("Caderno", 25.0, papelaria)
p2 = Produto("Fone", 120.0, eletronico)

estoque = Estoque()
estoque.cadastrar(p1)
estoque.cadastrar(p2)
estoque.listar()

achado = estoque.buscar("Fone")
print(achado.preco_final()) 