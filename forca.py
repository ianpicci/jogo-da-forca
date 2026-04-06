import random

print("===Jogo da Forca===")

palavra_secreta = "teste"
letras_descobertas = ["_", "_", "_", "_", "_"]

while True:
    print("\nPalavra:", " ".join(letras_descobertas))
    letra = input("Digite uma letra: ")

    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                letras_descobertas[i] = letra
        print("Acertou!")
    else:
        print("Errou!")

