# 7. Sistema de Batalha Simples
# Aqui está um exemplo de um sistema de batalha onde o jogador e o dragão se enfrentam. A vida de ambos diminui conforme eles atacam.

# Exemplo:
import random

# Atributos
jogador_vida = 100
dragao_vida = 150

def ataque(dano_min, dano_max):
    return random.randint(dano_min, dano_max)

# Loop de batalha
while jogador_vida > 0 and dragao_vida > 0:
    # Ataque do jogador
    dano_jogador = ataque(20, 40)
    dragao_vida -= dano_jogador
    print(f"Você atacou o dragão e causou {dano_jogador} de dano.")
    
    if dragao_vida <= 0:
        print("Você derrotou o dragão!")
        break

    # Ataque do dragão
    dano_dragao = ataque(10, 30)
    jogador_vida -= dano_dragao
    print(f"O dragão atacou você e causou {dano_dragao} de dano.")

    if jogador_vida <= 0:
        print("Você foi derrotado pelo dragão.")
        break

    # Status da batalha
    print(f"Vida do jogador: {jogador_vida} | Vida do dragão: {dragao_vida}")

# Explicação:
# Usamos random.randint() para gerar um dano aleatório entre um valor mínimo e máximo, tanto para o jogador quanto para o dragão.
# A batalha continua enquanto ambos tiverem vida maior que 0. Quando um deles chega a 0, o loop termina e o resultado é exibido.
