alvo = 42
quantidade_tentativas = 5
jogador_acertou = False


while quantidade_tentativas > 0 and not jogador_acertou:

    try:

        chute = int(input("Digite um número inteiro entre 0 e 100 "))

        if chute == alvo:
            print("Parabéns! Você acertou!")
            jogador_acertou = True
        elif chute > alvo:
            print("Errou, o número é menor")
            quantidade_tentativas -= 1
        else:
            print("Errou, o número é maior")
            quantidade_tentativas = quantidade_tentativas - 1

    except:
        print("O valor não era um número inteiro")

if not jogador_acertou:
    print("Que pena, o número era ")
