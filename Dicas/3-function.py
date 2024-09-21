# 3. Funções (def)
# Funções ajudam a modularizar o código, tornando-o mais organizado e reutilizável.

# Exemplo:
def ataque_jogador():
    dano = 30
    print(f"O jogador causou {dano} de dano.")
    return dano

vida_dragao = 200
vida_dragao -= ataque_jogador()
print(f"Vida do dragão restante: {vida_dragao}")
# Explicação:
# A função ataque_jogador encapsula a lógica do ataque do jogador e retorna o dano causado. Assim, você pode chamar essa função sempre que o jogador atacar.