# Login simples

# Crie:

# usuario_correto = "admin"
# senha_correta = "1234"

# Peça usuário e senha.
# Verifique se ambos estão corretos.


usuario_correto = "admin"
senha_correta = "1234"

usuario = input('Digite o usuário: ')
senha = input('Digite a senha: ')


if usuario == usuario_correto and senha ==senha_correta: 
    print('Login bem-sucedido! Seja bem vindo, admin!')
else:
    print('Login falhou! Usuário ou senha incorretos.')