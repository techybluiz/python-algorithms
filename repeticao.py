def esconder_palavra(palavra):
    return '*' * len(palavra)

def revelar_letra(palavra, palavra_oculta, letra):
    nova_palavra = ''
    for i in range(len(palavra)):
        if palavra[i] == letra:
            nova_palavra += letra
        else:
            nova_palavra += palavra_oculta[i]
    return nova_palavra

def jogo():
    palavra_secreta = "python"
    palavra_oculta = esconder_palavra(palavra_secreta)
    tentativas = 0
    letras_utilizadas = []

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra secreta.")

    while '*' in palavra_oculta:
        print("\nPalavra: ", palavra_oculta)
        letra = input("Digite uma letra: ").lower()

        if letra in letras_utilizadas:
            print("Você já tentou esta letra. Tente outra.")
            continue

        letras_utilizadas.append(letra)
        tentativas += 1

        if letra in palavra_secreta:
            palavra_oculta = revelar_letra(palavra_secreta, palavra_oculta, letra)
            print("Letra correta!")
        else:
            print("Letra errada! Tente novamente.")

    print("\nParabéns! Você acertou a palavra '{}' com {} tentativas.".format(palavra_secreta, tentativas))

jogo()