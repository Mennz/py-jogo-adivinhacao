import random

numero_secreto = random.randint(1, 100)

print("Adivinhe o número entre 1 e 100!")

tentativas = 0

while True:
    palpite = int(input("Seu palpite: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Você acertou em {tentativas} tentativas!")
        break
    elif palpite < numero_secreto:
        print("É maior que isso")
    else:
        print("É menor que isso")
