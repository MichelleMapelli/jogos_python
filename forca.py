
def jogar_forca():

    print("************************")
    print("***Novo jogo de FORCA***")
    print("************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    letras_faltando = str(letras_acertadas.count("_"))

    enforcou = False
    acertou = False

    print(letras_acertadas)

    #enquanto não False E não False // enquanto(True)
    while(not enforcou and not acertou):
        chute = input("Qual a letra? ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

    print("Fim do Jogo!")

if(__name__ == "__main__"):
    jogar_forca()