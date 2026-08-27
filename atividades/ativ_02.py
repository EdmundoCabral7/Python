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
        self.desconto = categoria.desconto
        self.categoria = categoria 

    def preco_final(self):
        d = self.categoria.desconto 
        return self.preco * (1 - d / 100)

eletronicos = Categoria("Eletrônicos", 15)
importados = Categoria("Importados", 20)    

p = Produto("Notebook", 4000.00, eletronicos)   
s = Produto("Smartphone", 3000.00, importados)
c = Produto("Câmera", 1500.00, eletronicos)

print(p.categoria)
print(s.categoria)
print(c.categoria)
print(p.preco_final())
print(s.preco_final())
print(c.preco_final())
print(p.preco)
print(s.preco)
print(c.preco)


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


pedido1 = Pedido(1, "Luiz")
pedido1.adicionar(p, 2)
print(pedido1.numero, pedido1.cliente, pedido1.total())


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