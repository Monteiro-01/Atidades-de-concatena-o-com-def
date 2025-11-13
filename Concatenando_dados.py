#Deve receber dois dados diferentes e concatená-los em uma única string.
def concatenar_dados():    
    info = input("Digite o primeiro dado: ")
    info2 = input("Digite o segundo dado: ")
    info_concatenado = info + info2
    return "Dados concatenados são:", info_concatenado