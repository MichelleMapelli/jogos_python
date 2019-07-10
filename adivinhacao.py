import random

def jogar_adivinhacao():

    print("***********************")
    print("Novo jogo de adivinhacao")
    print("***********************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000
    pontos_perdidos = 0
    print(numero_secreto) #apenas para teste
    print("Qual o nível de dificuldade você quer?")
    print("(1)Fácil  (2)Médio  (3)Difícil")

    nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite um numero entre 1 e 100: ")
        chute = int(chute_str)
        print("Você digitou o numero :", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Voce acertou e fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("O numero que digitou é maior")
            elif (menor):
                print("O numero que digitou é menor")

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos


    print("Fim do Jogo")
