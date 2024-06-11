class Contato:
    def __init__(self, nome: str, sobrenome: str, telefone: Utilidades):
        self.nome = nome
        self.sobrenome = sobrenome
        self.telefone = telefone

    @property
    def nome(self):
        return self.nome
    
    @nome.setter
    def nome(self, novo_nome):
        if len(novo_nome.strip()) > 1:
            self.__novo_nome = novo_nome.upper().strip()
        else:
            raise AttributeError(f"O nome do contato deve ter ao menos 2 caracteres!")
    
    @property
    def sobrenome(self):
        return self._sobrenome
    
    @sobrenome.setter
    def sobrenome(self, novo_sobrenome):
        self._sobrenome = novo_sobrenome
    
    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        numero_formatado = self.formatar_numero_telefone(novo_telefone)
        if numero_formatado:
            self._telefone = numero_formatado
        else:
            raise ValueError("O número de telefone é inválido. Deve conter 11 dígitos.")

    def formatar_numero_telefone(self, numero):
        numeros = [char for char in numero if char.isdigit()]
        
        if len(numeros) != 11:
            raise ValueError("Número de telefone inválido. Deve conter 11 dígitos.")
        
        numero_formatado = "({}) {}-{}".format("".join(numeros[:2]), "".join(numeros[2:6]), "".join(numeros[6:]))
        
        return numero_formatado

    