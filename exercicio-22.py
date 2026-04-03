#Detector de palindromos.

frase = input("Digite uma frase: ").lower()
if isinstance(frase, str):
    formatado = frase.replace(" ", "").lower()
    if formatado == formatado[::-1]:
        print("É um palíndromo.")
    else:
        print("Não é um palíndromo.")
else:
    print("Entrada inválida. Por favor, digite uma palavra ou frase.")
