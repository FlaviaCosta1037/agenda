from classes.lista_contatos import lista_contatos
from classes.contato import Contato

class ProgramaContatos:
    def __init__(self):
        self.__dados = lista_contatos()

    def exibir_agenda(self):
        print('-' * 20)
        print(' '*7 + 'Agenda' + ' ' * 8)
        print('-' * 20)
        print('1 - Exibir contatos')
        print('2 - Cadastrar contato')
        print('3 - Alterar contato')
        print('4 - Remover contato')
        print('5 - Listar contatos')

    def cadastrar_contato(self):
        nome_contato = input("Informe o nome do contato: ")
        sobrenome_contato = input("Informe o sobrenome do contato: ")
        numero_contato = input("Informe o numero do contato: ")
        novo_contato = Contato(nome_contato, sobrenome_contato, numero_contato)
        self.__dados.cadastrar_contato(novo_contato)
        print("Contato cadastrado com sucesso!")

    def consultar_contato(self):
        nome_contato = input("Informe o nome do contato: ")
        
        try:
            contato = self.__dados.consultar_contato(nome_contato)
            print(f"Nome: {contato.nome}")
            print(f"Sobrenome: {contato.sobrenome}")
            print(f"Telefone: {contato.telefone}")
        except Exception as e:
            print(e)
        

    def alterar_contato(self):
        nome_contato = input("Informe o nome do contato: ")
        novo_nome_contato = input("Informe o novo nome do contato: ")
        novo_sobrenome_contato = input("Informe o novo sobrenome do contato: ")
        novo_numero_contato = input("Informe o novo número do contato: ")
        novo_contato = Contato(novo_nome_contato, novo_sobrenome_contato, novo_numero_contato)
        try:
            self.__dados.alterar_contato(nome_contato, novo_contato)
            print("Contato alterado com sucesso!")
                       
            del self.__dados.contatos[nome_contato]  
            self.__dados.contatos[novo_nome_contato] = novo_contato

        except Exception as e:
            print(e)
        
    def remover_contato(self):
        nome_contato = input("Informe o nome do contato: ")
        self.__dados.excluir_contato(nome_contato)
        print("Contato removido com sucesso!")

    def listar(self):
        self.__dados.listar_contatos()

    def iniciar(self):
        while True:
            try:
                self.exibir_agenda()
                opcao = input("Informe a opção desejada: ")
                if opcao == "1":
                    self.consultar_contato()
                elif opcao == "2":
                    self.cadastrar_contato()
                elif opcao == "3":
                    self.alterar_contato()
                elif opcao == "4":
                    self.remover_contato()
                elif opcao == "5":
                    self.listar()
                else:
                    break
            except Exception as e:
                print(e)