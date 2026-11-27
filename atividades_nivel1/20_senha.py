# Senha correta
# Crie uma senha:
# senha = "python123"
# Enquanto o usuário errar:
# continue pedindo

senha = "python123"

login = input("Digite sua senha: ")

while senha != login:
    print('Senha incorreta! Tente novamente.')
    login = input("Digite sua senha: ")
else:
    print('Senha correta! Bem vindo!')