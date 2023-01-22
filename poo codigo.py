class Pessoas():
    def __init__(self,nome,sobrenome,idade,endereco,bairro):
        self.nome = nome
        self.__sobrenome = sobrenome
        self.__idade= idade
        self.__endereco = endereco
        self.__bairro = bairro

    #criandos os metodos de acesso as variaveis privadas get e sets
    def get_nome(self):
        return self.nome

    def get_sobrenome(self):
        return self.__sobrenome

    def get_endereco (self):
        return self.__endereco

    def set_endereco(self,endereco):
        self.__endereco = endereco


    def get_idade(self):
        return self.__idade

    def get_bairro(self):
        return self.__bairro

    def funcionario_faz(self,empresa = 'mahle'):
        print(f'o funcionario {self.nome} é funcionario da empresa {empresa}')

class Gerente(Pessoas):
    def __init__(self, nome, sobrenome, idade, endereco, bairro):
        super().__init__(nome, sobrenome, idade, endereco, bairro)
        self.__cargo = 'Gerente'


    #sobreescrevendo a função da classe mãe
    def funcionario_faz(self, empresa='mahle'):
        print(f'o {self.__cargo}  da empresa {empresa} é {self.get_nome()}')

