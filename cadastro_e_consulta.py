import getpass

class User:
    def __init__(self, usuario, nome, senha, telefone, email):
       self.usuario = usuario
       self.nome = nome
       self.senha = senha
       self.telefone = telefone
       self.email = email

    def __str__(self):
       return f"Nome: {self.nome}, Telefone: {self.telefone} e Email: {self.email}"

# Lista para armazenar os usuários
usuarios = []
    

def procurar():
    usuario = input("Insira um usuário para consultar: ")
    for user in usuarios:
        if user.usuario == usuario:
            print(user)
            return
        print("Usuário não encontrado.")

def cadastrar():
    usuario = input("Cadastre seu usuário: ")
    nome = input("Cadastre seu nome: ")
    senha = getpass.getpass("Cadastre sua senha: ")
    telefone = input("Cadastre seu telefone: ")
    email = input("Cadastre seu email: ")

    novo_usuario = User(usuario, nome, senha, telefone, email)
    usuarios.append(novo_usuario)
    print("Usuário cadastrado com sucesso!")





def menu():
    print("============MENU==============")
    print("1 - Para cadastrar usuario")
    print("2 - Para consultar um usuario")
    print("3 - Para fechar")
    print("==============================")
    escolha = int(input())
    return escolha

def escolher(escolha):
    if (escolha == 1):
        cadastrar()
    if (escolha == 2):
        procurar()
    if (escolha == 3):
        exit()
    else:
        print("Escolha inválida!")
        escolher(escolha)
while True:
    escolha = menu()


    if escolha == 1:
        cadastrar()
    elif escolha == 2:
        procurar()
    elif escolha == 3:
        break
    else:
        print("Escolha inválida!")

print ("Encerrando o programa.")
