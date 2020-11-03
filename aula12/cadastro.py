usuario = input("Informe nome de usuário: ")
senha = input("Informe sua senha: ")

usuario_bd = "Gabriel"
senha_bd = "notafraid1"

if usuario_bd == usuario and senha_bd == senha:
    print("Login efetuado com sucesso!")
else:
    print("Usuário e senha incorretos!")
