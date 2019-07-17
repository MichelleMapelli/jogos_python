
def jogar_forca():

    print("************************")
    print("***Novo jogo de FORCA***")
    print("************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    #enquanto não False E não False // enquanto(True)
    while(not enforcou and not acertou):
        chute = input("Qual a letra? ")

        index = 0
        for letra in palavra_secreta:
            if(chute == letra):
                print("Encontrei a letra {} na posição {}".format(letra, index))
            index = index + 1

        print("Jogando...")

    print("Fim do Jogo!")

if(__name__ == "__main__"):
    jogar_forca()