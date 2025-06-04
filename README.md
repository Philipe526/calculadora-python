# Calculadora em Python
# Uma calculadora simples de linha de comando feita em Python.
## Funcionalidades
# - Adição
# - Subtração
# - Multiplicação
# - Divisão (com verificação de divisão por zero)
## Como usar
# Execute o script com Python:```bash python calculadora.py
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def calculadora():
    print("Calculadora Simples em Python")
    print("Operações disponíveis:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

    escolha = input("Escolha a operação (1/2/3/4): ")

    if escolha not in ['1', '2', '3', '4']:
        print("Opção inválida!")
        return

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida! Use apenas números.")
        return

    if escolha == '1':
        print(f"Resultado: {somar(num1, num2)}")
    elif escolha == '2':
        print(f"Resultado: {subtrair(num1, num2)}")
    elif escolha == '3':
        print(f"Resultado: {multiplicar(num1, num2)}")
    elif escolha == '4':
        print(f"Resultado: {dividir(num1, num2)}")

# Executar a calculadora
calculadora()
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def calculadora():
    print("Calculadora Simples em Python")
    print("Operações disponíveis:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

    escolha = input("Escolha a operação (1/2/3/4): ")

    if escolha not in ['1', '2', '3', '4']:
        print("Opção inválida!")
        return

    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida! Use apenas números.")
        return

    if escolha == '1':
        print(f"Resultado: {somar(num1, num2)}")
    elif escolha == '2':
        print(f"Resultado: {subtrair(num1, num2)}")
    elif escolha == '3':
        print(f"Resultado: {multiplicar(num1, num2)}")
    elif escolha == '4':
        print(f"Resultado: {dividir(num1, num2)}")

# Executar a calculadora
calculadora()
