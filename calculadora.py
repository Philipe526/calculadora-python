import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math

# Funções matemáticas
def somar(a, b): return a + b
def subtrair(a, b): return a - b
def multiplicar(a, b): return a * b
def dividir(a, b): return "Erro: divisão por zero!" if b == 0 else a / b
def potencia(a, b): return a ** b
def raiz_quadrada(a): return math.sqrt(a) if a >= 0 else "Erro: número negativo!"
def porcentagem(a, b): return (a * b) / 100
def modulo(a, b): return a % b if b != 0 else "Erro: divisão por zero!"

# Função chamada ao clicar no botão
def calcular():
    operacao = operacao_var.get()
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get()) if operacao != 'Raiz Quadrada' else 0
    except ValueError:
        messagebox.showerror("Erro", "Digite apenas números.")
        return

    match operacao:
        case 'Soma': resultado = somar(num1, num2)
        case 'Subtração': resultado = subtrair(num1, num2)
        case 'Multiplicação': resultado = multiplicar(num1, num2)
        case 'Divisão': resultado = dividir(num1, num2)
        case 'Potência': resultado = potencia(num1, num2)
        case 'Raiz Quadrada': resultado = raiz_quadrada(num1)
        case 'Porcentagem': resultado = porcentagem(num1, num2)
        case 'Módulo': resultado = modulo(num1, num2)
        case _: resultado = "Operação inválida."

    resultado_var.set(f"Resultado: {resultado}")

# Janela principal
root = tk.Tk()
root.title("Calculadora Moderna")
root.geometry("350x300")
root.resizable(False, False)

# Estilo
style = ttk.Style()
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("TButton", font=("Segoe UI", 11), padding=6)
style.configure("TEntry", font=("Segoe UI", 11))
style.configure("TCombobox", font=("Segoe UI", 11))

# Variáveis
operacao_var = tk.StringVar(value='Soma')
resultado_var = tk.StringVar()

# Widgets
frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

ttk.Label(frame, text="Número 1:").grid(row=0, column=0, sticky="w", pady=5)
entry1 = ttk.Entry(frame)
entry1.grid(row=0, column=1, pady=5)

ttk.Label(frame, text="Número 2:").grid(row=1, column=0, sticky="w", pady=5)
entry2 = ttk.Entry(frame)
entry2.grid(row=1, column=1, pady=5)

ttk.Label(frame, text="Operação:").grid(row=2, column=0, sticky="w", pady=5)
operacoes = ['Soma', 'Subtração', 'Multiplicação', 'Divisão', 'Potência', 'Raiz Quadrada', 'Porcentagem', 'Módulo']
operacao_menu = ttk.Combobox(frame, textvariable=operacao_var, values=operacoes, state='readonly')
operacao_menu.grid(row=2, column=1, pady=5)

ttk.Button(frame, text="Calcular", command=calcular).grid(row=3, column=0, columnspan=2, pady=15)
ttk.Label(frame, textvariable=resultado_var, font=("Segoe UI", 12, "bold")).grid(row=4, column=0, columnspan=2)

root.mainloop()
