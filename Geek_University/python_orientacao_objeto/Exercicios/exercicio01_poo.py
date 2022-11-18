class Pessoa():

    def __init__(self: object, nome: str, telefone: int, endereco: str) -> None:
        self.__nome: str = nome
        self.__telefone: int = telefone
        self. __endereco: str = endereco

    @property
    def nome(self: str) -> str:
        return self.__nome

    @property
    def telefone(self: int) -> int:
        return self.__telefone

    @property
    def endereco(self: str) -> str:
        return self.__endereco

    def update_endereco(self, new_data: str) -> str:
        self.__endereco: str = new_data
        return self.__endereco


if __name__ == '__main__':
    cadastro: object = Pessoa('Hugo', 1199345656, 'Rua José Benetido - 334')

    print(f"...Nome{cadastro.nome} \n\nContato: {cadastro.telefone} \n\nEndereco{cadastro.endereco}")
    endereco_cadastro = cadastro.update_endereco('Rua Jose francisco - 334')
    print(cadastro.__dict__)
