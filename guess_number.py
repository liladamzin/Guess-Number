# > IMPORTANDO BIBLIOTECA DE "INTELIGENCIA ARTIFICAL" ↓

import random

# > INICIO DO JOGO ↓

print("Bem vindo ao Guess Number!")
choice_number = input("Digite o número teto do desafio: ")

# > VERIFICAÇÃO DO TIPO DE TEXTO ↓

if choice_number.isdigit():
    choice_number = int(choice_number)

else:
    print("O valor informado não é numérico; Favor execute novamente e informe um número!")
    quit()

# > GERANDO NÚMERO ALEATÓRIO ↓

random_number = random.randint(0, choice_number)

# > NÚMERO DE TENTATIVAS ↓

n_choices = 0

# > LOOPING ↓

while True:
    choice_user = input("Adivinhe o número: ")

    if choice_user.isdigit():
        choice_user = int(choice_user)
    else:
        print("O valor informado não é numérico; Favor execute novamente e informe um número!")
        continue

    n_choices = n_choices + 1

    if choice_user == random_number:
        print("Acertou!")
        break
    elif choice_user > random_number:
        print("Chutou alto! O número aleatório é menor que isso...")
    else:
        print("Chutou baixo! O número aleatório é maior que isso...")

# > FIM DO JOGO ↓

print("Número de Tentativas: " + str(n_choices))

