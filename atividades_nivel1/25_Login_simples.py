# Login simples

# Crie um sistema onde:

# usuário correto: admin
# senha correta: 1234

# Menu:

# 1 - Fazer login
# 2 - Sair

# Regras:

# enquanto errar login, continua tentando
# ao acertar:
# mostrar “Login realizado”
# encerrar programa



usuario_correto = 'admin'
senha_correta = '1234'


while True:
    
    opcao = input(
            'Menu:\n\n'

            '1 - Fazer login\n'
            '2 - Sair\n')

    if opcao == '1':
        login = input('Digite o usuário: ').strip().lower()
        senha = input('Digite a senha: ')
        
        if login != usuario_correto or senha != senha_correta:
            print('Usuário ou senha incorretos! tente novamente.\n')
        else:
            print('Login realizado com sucesso. Seja bem vindo!\n')
            break
    else:
        print('Encerrando o programa...')
        break


