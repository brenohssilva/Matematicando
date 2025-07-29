import random

def gerar_operacao_valida():
    operadores = ['+', '-', '×', '÷']
    while True:
        op = random.choice(operadores)
        if op == '+':
            a = random.randint(1, 30)
            b = random.randint(1, 30)
            c = a + b
        elif op == '-':
            a = random.randint(5, 30)
            b = random.randint(1, a)  # evita resultado negativo
            c = a - b
        elif op == '×':
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = a * b
        elif op == '÷':
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            a = b * c  # garante divisão exata
        return a, op, b, '=', c

def gerar_cruzadinha():
    # Gerar 6 operações
    cruzadinha = [gerar_operacao_valida() for _ in range(6)]

    # Exibir cruzadinha
    print("Cruzadinha Matemática:\n")
    print(f"  {cruzadinha[0][0]} {cruzadinha[0][1]} [{cruzadinha[0][2]}] = {cruzadinha[0][4]}")
    print(f"         -       ×       ×")
    print(f"[{cruzadinha[1][0]}]   [{cruzadinha[2][0]}]   [{cruzadinha[3][0]}]")
    print(f"   =        =        =")
    print(f"{cruzadinha[4][0]}   +   {cruzadinha[5][0]}   =   [{cruzadinha[5][4]}]")

    # Gabarito
    print("\nGabarito:")
    for i, (a, op, b, _, res) in enumerate(cruzadinha):
        print(f"{i+1}: {a} {op} {b} = {res}")

# Executar
gerar_cruzadinha()
