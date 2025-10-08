from datetime import datetime

print(datetime.now().date())
print(datetime.now().month)
print(datetime.now().year)
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().second)

usuario = {}
usuario["nome"] = input("Digite o seu nome: ")
usuario["email"] = input("Digite o seu email: ")
usuario["senha"] = input("Digite a sua senha: ")
usuario["data_criacao"] = datetime.now().date()

print(usuario)