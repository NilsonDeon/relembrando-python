
from random import randrange

game = int(input("Quantas partidas você deseja? "))
hp = int(input("Quantas vidas você deseja? "))
rng = int(input("de 0 até que número? "))
correct = 0

for i in range((game)):
    
    while hp > 0:
        num = randrange(0, (rng+1))

        guess = int(input("Qual o número? "))

        if guess == num:
            print("\nvocê certou! \n")
            correct += 1
            break
        else:
            print("\nvocê errou!")
            print(f"O número era {num}\n")
            hp -= 1;

print(f"Você acertou {correct} números.\n")