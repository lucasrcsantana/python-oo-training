class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self._ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @property
    def ano(self):
        return self._ano

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self, nome):
        self._nome = nome.title()
    
    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return (f"Programa: {self._nome} - Ano: {self._ano} - Likes: {self._likes}")


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao

    @property
    def duracao(self):
        return self._duracao

    def __str__(self):
        return (f"Filme: {self._nome} - Ano: {self._ano} - Duração {self._duracao} minutos - Likes: {self._likes}")


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self._temporadas = temporadas

    @property
    def temporadas(self):
        return self._temporadas

    def __str__(self):
        return (f"Série: {self._nome} - Ano: {self._ano} - Duração {self._temporadas} temporadas - Likes: {self._likes}")

vingadores = Filme(
    nome="vingadores - guerra infinita", 
    ano=2018, 
    duracao=160
    )

atlanta = Serie(
    nome="atlanta",
    ano=2017,
    temporadas=2
    )

vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()

print(vingadores)
print(atlanta)
