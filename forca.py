import random

print("=== Jogo da Forca ===")

lista_palavras = ["python", "banana", "janela", "futebol", "cadeira"]
palavra_secreta = random.choice(lista_palavras)

letras_descobertas = ["_"] * len(palavra_secreta)
tentativas = 6
letras_tentadas = []

while tentativas > 0:
    print("\nPalavra:", " ".join(letras_descobertas))
    print("Tentativas restantes:", tentativas)
    print("Letras tentadas:", ", ".join(letras_tentadas))

    letra = input("Digite uma letra: ").lower()

    if len(letra) != 1 or not letra.isalpha():
        print("Digite apenas uma letra válida.")
        continue

    if letra in letras_tentadas:
        print("Você já tentou essa letra.")
        continue

    letras_tentadas.append(letra)

    if letra in palavra_secreta:
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                letras_descobertas[i] = letra
        print("Acertou!")
    else:
        tentativas -= 1
        print("Errou!")

    if "_" not in letras_descobertas:
        print("\nParabéns! Você venceu!")
        print("A palavra era:", palavra_secreta)
        break

if "_" in letras_descobertas:
    print("\nQue pena! Você perdeu.")
    print("A palavra era:", palavra_secreta)