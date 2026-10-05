import random

numero_secreto = random.randint(1, 100)

print("Adivinhe o número entre 1 e 100!")

while True:
    palpite = int(input("Seu palpite: "))

    if palpite == numero_secreto:
        print("Você acertou!")
        break
    elif palpite < numero_secreto:
        print("É maior que isso")
    else:
        print("É menor que isso")
