
def jogar_forca():

    print("************************")
    print("***Novo jogo de FORCA***")
    print("************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    #letras_faltando = str(letras_acertadas.count("_"))

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    #enquanto não False E não False // enquanto(True)
    while(not enforcou and not acertou):
        chute = input("Qual a letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou o jogo!!!")
    else:
        print("Você perdeu!")

    print("Fim do Jogo!")

if(__name__ == "__main__"):
    jogar_forca()