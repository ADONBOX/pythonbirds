class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar (self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    elisa = Pessoa(nome='Elisa')
    natercia = Pessoa(elisa, nome="Natercia")
    print(Pessoa.cumprimentar(natercia))
    print(id(natercia))
    print(natercia.cumprimentar())
    print(natercia.nome)
    print(natercia.idade)

    for filho in natercia.filhos:
        print(filho.nome)

