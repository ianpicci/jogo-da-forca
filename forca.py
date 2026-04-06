import random

print('===Jogo da Forca===')

# Lista de palavras
palavras = ['teste', 'teste2']

palavra_secreta = random.choice(palavras)

letra = str(input("Digite uma letra: "))

print(palavra_secreta)

if letra in palavra_secreta:
  print("Acertou uma letra")
  
else:
  print("Errou!")

palavra_mostrada = ""

for caractere in palavra_secreta:
  if caractere == letra:
    palavra_mostrada += caractere
  else:
    palavra_mostrada += "_"

print("Palavra:", palavra_mostrada)