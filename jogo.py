import random

print("Escolha a dificuldade:")
print("1 - Fácil (1 a 50, 10 tentativas)")
print("2 - Médio (1 a 100, 7 tentativas)")
print("3 - Difícil (1 a 200, 5 tentativas)")
dificuldade = input("Opção: ")

if dificuldade == "1":
    limite = 50
    max_tentativas = 10
elif dificuldade == "3":
    limite = 200
    max_tentativas = 5
else:
    limite = 100
    max_tentativas = 7

numero_secreto = random.randint(1, limite)

print(f"\nAdivinhe o número entre 1 e {limite}!")

tentativas = 0
acertou = False

while tentativas < max_tentativas:
    palpite = int(input("Seu palpite: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Você acertou em {tentativas} tentativas!")
        acertou = True
        break
    elif palpite < numero_secreto:
        print("É maior que isso")
    else:
        print("É menor que isso")

if not acertou:
    print(f"Suas tentativas acabaram. O número era {numero_secreto}")
