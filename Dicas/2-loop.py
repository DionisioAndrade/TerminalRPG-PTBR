# 2. Estruturas de Repetição (while)
# Usamos while para criar loops, como quando o jogador está em uma batalha e o combate continua até que a vida de alguém chegue a 0.

# Exemplo:
dragao_vida = 200
jogador_vida = 100

while dragao_vida > 0 and jogador_vida > 0:
    print("A batalha continua!")
    # Aqui você inseriria o código do combate
    dragao_vida -= 30  # Simulando dano no dragão
    jogador_vida -= 20  # Simulando dano no jogador

print("A batalha terminou.")

# Explicação:
# O while repete o bloco de código enquanto as condições forem verdadeiras. Neste exemplo, o loop continua até que a vida do dragão ou do jogador chegue a 0. Esse conceito é usado para sistemas de combate repetitivos.