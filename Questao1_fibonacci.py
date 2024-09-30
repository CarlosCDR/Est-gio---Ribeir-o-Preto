def fibonacci(n):
    i, j = 0, 1
    # Gera a sequência até o número ser maior ou igual ao informado
    while j < n:
        i, j = j, i + j
    
    # Verifica se o número é parte da sequência de Fibonacci
    if n == j or n == 0:
        return True
    return False

# Pedi ao usuario que digite um numero a ser verificado
numero = int(input("Digite um número: "))

# Mostra o resultado para o usuario
if fibonacci(numero):
    print(f"O número {numero} pertence a sequência de Fibonacci.")
else:
    print(f"O número {numero} Não pertence a sequência de Fibonacci.")