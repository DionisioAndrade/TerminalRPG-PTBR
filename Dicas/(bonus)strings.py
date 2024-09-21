def linha():
    linhas = '-'*10
    print(linhas)

linha() 
s1 = "Olá"
s2 = "Mundo"
resultado = s1 + " " + s2
print(resultado)  # Saída: Olá Mundo

linha() 
s = "Oi! "
resultado = s * 3
print(resultado)  # Saída: Oi! Oi! Oi!

linha() 
s = "Python"
print(s[0:3])  # Saída: Pyt
print(s[-1])   # Saída: n (último caractere)
print(s[2:])   # Saída: thon (a partir do índice 2 até o final)

linha() 
s = "Python"
print(len(s))  # Saída: 6

linha() 
a = 'Lucas'
s = "Olá Mundo Mundo"
resultado = s.replace("Mundo", a)
print(resultado)  # Saída: Olá Python

linha() 
s = "   Olá Mundo   "
print(s)
print(s.strip())   # Saída: Olá Mundo
print(s.lstrip())  # Saída: "Olá Mundo   "
print(s.rstrip())  # Saída: "   Olá Mundo"

linha() 
s = "PytHoN é InCrível"
print(s.upper())
print("PYTHON" in s.upper())  # Saída: True
print("JAVA" in s.upper())    # Saída: False         


nome = "Maria"
idade = 30
resultado = nome + " tem " + str(idade) + " anos."
print(resultado)

nome = "João"
idade = 25
resultado = "{} tem {} anos. e 1 + 1 = {}".format(nome.upper(), idade, 1+1)
print(resultado)

nome = "Ana"
idade = 28
resultado = f"{nome.upper()} tem {idade} e 1 + 1 = {1+1} anos."
print(resultado)


nome = "Carlos"
idade = 35
#%s = string
#%d = inteiro
#%f = float
#%x = hexa
resultado = "%s tem %d anos." % (nome, idade)
print(resultado)