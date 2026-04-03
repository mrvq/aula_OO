# Declaração de classe


class Gafanhoto:
    """
    Essa classe cria um Gafanhoto, que é uma pessoa que tem nome e idade
    Para criar uma nova pessoa, use
    variavel = Gafanhoto(nome, idade)
    """

    def __init__(self, n="", i=0):  ##Metodo construtor
        # Atributos de instancia
        self.nome = n
        self.idade = i

    # Metodo de instancia
    def aniversario(self):
        self.idade += 1

    def __str__(self):  # Dunder Method
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."

    # sobreescrever o metodo
    def __getstate__(self):
        return f"Estado: nome = {self.nome} ; idade = {self.idade}"


# Declaração do objeto
g1 = Gafanhoto("Maria", 17)
g1.aniversario()
# print(g1)
print(g1.__dict__)  # Atributo
print(g1.__getstate__())  # Metodo
print(g1.__class__)
# print(g1.__doc__)  # Dunder attribute

# g2 = Gafanhoto("Mauro", 54)
# print(g2)
# print(g2.__getstate__())
