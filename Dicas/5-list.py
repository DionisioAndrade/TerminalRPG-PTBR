# Listas e Dicionários (para itens e atributos)
# As listas e dicionários armazenam coleções de dados, como inventário de itens ou atributos do personagem.

# Exemplo de Lista:
itens = ["Espada", "Poção de Cura", "Escudo"]

# Acessar um item
print(f"Você encontrou uma {itens[1]}.")

# Exemplo de Dicionário:
jogador = {
    "nome": "Aldar",
    "vida": 100,
    "ataque": 30
}

print(f"{jogador['nome']} tem {jogador['vida']} de vida e {jogador['ataque']} de ataque.")
# Explicação:
# Lista: Armazena itens em uma coleção ordenada, permitindo o acesso a cada item por índice.
# Dicionário: Armazena pares chave-valor, útil para guardar atributos do personagem como vida e ataque.
