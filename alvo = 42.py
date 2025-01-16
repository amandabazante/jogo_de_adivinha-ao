alvo = 42

try:

  chute = int(input("Digite um número inteiro entre 0 e 100 "))

  if chute == alvo:
      print("Parabéns! Você acertou!")
  else:
      print("Que pena! O número era " + str(alvo))

except:
    print("O valor não era um número inteiro")
