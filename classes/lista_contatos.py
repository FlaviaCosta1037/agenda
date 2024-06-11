class lista_contatos:
    def __init__(self):
        self.contatos = {}
    
    def cadastrar_contato(self,contato):
        if contato.nome in self.contatos:
            raise Exception(f"Já existe um contato com este {contato.nome}!")
        else:
            self.contatos[contato.nome] = contato