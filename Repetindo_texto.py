#Agora vamos solicitar ao usuário una string e um número inteiro como entrada. Depois teremos que repetir a string o número de vezes indicado pelo inteiro e exibir o resultado.
def repetir_texto():
    texto = input("Digite uma string: ")
    vezes = int(input("Digite um número inteiro: "))
    resultado = (texto + ' ') * vezes
    return "Resultado da repetição:", resultado