from random import randint

temas = (
    'CyberPunk',
    'Espacial',
    'Futebol',
    'Guerra',
    'Heroi',
    'Horror',
    'Medicina',
    'Medieval',
    'Música',
    'Romance',
    'Vampiro',
    'Zumbi'
)

print(f'O tema sorteado foi {temas[randint(0, 11)]}. Boa sorte e Divirta-se!')
