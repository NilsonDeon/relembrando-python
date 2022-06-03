
nome = input("Insira seu nome: ")
sexo = input("Insira seu sexo (F/M): ")
peso = float(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))

imc = peso/(altura**2)

print(f"Olá, {nome}")

if sexo == "F":
    if imc < 19.1:
        print("Abaixo do peso")
    elif imc >= 19.1 and imc < 27.3:
        print("Peso ideal")
    elif imc >= 27.3 and imc < 31.1:
        print("Acima do peso")
    elif imc >= 31.1:
        print("obeso")
else:
    if imc < 20.7:
        print("Abaixo do peso")
    elif imc >= 20.7 and imc < 27.3:
        print("Peso ideal")
    elif imc >= 27.3 and imc < 32.3:
        print("Acima do peso")
    elif imc >= 32.3:
        print("obeso")
