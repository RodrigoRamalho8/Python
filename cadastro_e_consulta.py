import getpass

class User:
    def __init__(self, cpf, nome, senha, telefone, email):
       self.cpf = cpf
       self.nome = nome
       self.senha = senha
       self.telefone = telefone
       self.email = email

    def __str__(self):
       return f"Nome: {self.nome}, Telefone: {self.telefone} e Email: {self.email}"

# Lista para armazenar os usuários
usuarios = []
    

def procurar():
    cpf = input("Insira um CPF para consultar: ")
    for user in usuarios:
        if user.cpf == cpf:
            print(user)
            return
        print("Usuário não encontrado.")

def cadastrar():
    cpf = input("Cadastre seu CPF: ")
    nome = input("Cadastre seu nome: ")
    senha = getpass.getpass("Cadastre sua senha: ")1
    telefone = input("Cadastre seu telefone: ")
    email = input("Cadastre seu email: ")

    novo_usuario = User(cpf, nome, senha, telefone, email)
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
