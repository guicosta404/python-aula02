# Calculadore simples
try:
    num1 = float(input("Digite um número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nEscolha a operação (1/2/3/4): ")
    
    if operacao == '1':
        resultado = num1 + num2
    elif operacao == '2':
        resultado = num1 - num2
    elif operacao == '3':
        resultado = num1 * num2
    elif operacao == '4':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print("Não existe divisão pro zero.")
    print(f"{resultado:.2f}")          
    
except ValueError:
    print("Entrada inválida.")                        