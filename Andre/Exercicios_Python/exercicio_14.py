#Exercicio 14 - Treinamento Python 2024

def is_palindromo(frase):
    formato_frase = ''.join(frase.split()).lower()
    
    return formato_frase == formato_frase[::-1]

def main():
    frase = input("Digite uma frase: ")
    if is_palindromo(frase):
        print("A frase é um palíndromo.")
    else:
        print("A frase não é um palíndromo.")

if __name__ == "__main__":
    main()
