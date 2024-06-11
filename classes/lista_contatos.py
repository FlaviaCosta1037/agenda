from classes.contato import Contato
class lista_contatos:
    def __init__(self):
        self.contatos = {}
    
    def cadastrar_contato(self,contato):
        if contato._nome in self.contatos:
            raise Exception(f"Já existe um contato com este {contato._nome}!")
        else:
            self.contatos[contato._nome] = contato

    def consultar_contato(self, nome):
        if nome in self.contatos:
            return self.contatos[nome]
        else:
            raise Exception(f"O contato com o nome '{nome}' não foi encontrado!")

    def alterar_contato(self, nome, novo_contato):
        if nome in self.contatos:
            self.contatos[nome] = novo_contato
        else:
            raise Exception(f"O contato com o nome '{nome}' não foi encontrado!")
        
    def excluir_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
        else:
            raise Exception(f"O contato com o nome '{nome}' não foi encontrado!")
        
    def listar_contatos(self):
        if self.contatos:
            print("Lista de Contatos:")
            for nome, contato in self.contatos.items():
                print(f"Contato: {nome} {contato.sobrenome} {contato.telefone}")
        else:
            print("Não há contatos cadastrados.")