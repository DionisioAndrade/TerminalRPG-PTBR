# Tratamento de Erros
# Você pode usar try e except para garantir que o jogo não quebre quando o jogador insere dados incorretos.

# Exemplo:
while True:
    try:
        escolha = int(input("Escolha 1 para atacar ou 2 para defender: "))
        if escolha not in [1, 2]:
            raise ValueError("Escolha inválida.")
        break
    except ValueError as e:
        print(e)
        print("Por favor, insira um número válido.")
# Explicação:
# O bloco try-except captura erros e evita que o programa falhe ao lidar com entradas inválidas. Neste caso, se o jogador inserir algo que não seja 1 ou 2, uma mensagem de erro é exibida e ele é solicitado a tentar novamente.