# Desenvolvido por Daniel Schinaider de Oliveira
#02
nome = input("Informe seu nome de usuário: ")
senha = input("Informe sua senha: ")

while nome == senha:
    print("\n Sua senha não pode ser idêntica ao seu nome de usuario")

    nome = input("\n Informe seu nome de usuário: ")
    senha = input("\n Informe sua senha: ")

print("Bem-vindo " , nome)
