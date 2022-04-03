class User:
    __slots__=(
    '_id'
    '_nome',
    '_idade',
    '_email,'
    '_profissao'
    )

    def __init__(self, id=None, nome="", idade=None, email="", profissao="" ):
        self.id = id
        self.nome = nome
        self.idade = idade
        self.email = email
        self.profissao = profissao

    @property
    def id(self):
        return self._id
    
    @property
    def nome(self):
        return self.nome


    def nome(self, nome):
        self._nome = nome

    @property
    def idade(self):
        return self._idade

    def idade(self, idade):
        self._idade = idade

    @property
    def email(self):
        return self._email

    def email(self, email):
        self._email = email

    @property
    def profissao(self):
        return self._profissao

    def profissao(self, profissao):
        self._profissao = profissao    