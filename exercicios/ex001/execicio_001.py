# Declaração de classe


class Gafanhoto:
    def __init__(self):  ##Metodo construtor
        # Atributos de instancia
        self.nome = ""
        self.idade = 0

    # Metodo de instancia
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."


# Declaração do objeto
g1 = (
    Gafanhoto()
)  # Instanciação da classe, criando um objeto g1 a partir da um metodo construtor da classe Gafanhoto
g1.nome = "Maria"  # g1.nome não tem parenteses depois, é um atributo
g1.idade = 17
g1.aniversario()
# g1.aniversario() tem parenteses depois, é um método
print(g1.mensagem())  # g1.mensagem() tem parenteses depois, é um método

g2 = (
    Gafanhoto()
)  # Instanciação da classe, criando um objeto g2 a partir da um metodo construtor da classe Gafanhoto
g2.nome = "Mauro"  # g2.nome não tem parenteses depois, é um atributo
g2.idade = 53
print(g2.mensagem())  # g2.mensagem() tem parenteses depois, é um método
