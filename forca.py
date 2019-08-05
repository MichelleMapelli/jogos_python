import random




def jogar_forca():

    imprime_mensagem_abertura()
    
    palavra_secreta = carregar_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

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
            print("Ops, você errou! Faltam {} tentativas".format(6-erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você ganhou o jogo!!!")
    else:
        print("Você perdeu!")

    print("Fim do Jogo!")


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def carregar_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


def imprime_mensagem_abertura():
    print("************************")
    print("***Novo jogo de FORCA***")
    print("************************")


if(__name__ == "__main__"):
    jogar_forca()