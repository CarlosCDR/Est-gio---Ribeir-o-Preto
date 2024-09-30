def conta_letra_a(texto):
    # Converte o texto para minúsculas para facilitar a contagem
    texto_lower = texto.lower()
    quantidade = texto_lower.count('a')  # Conta quantas vezes 'a' aparece
    return quantidade

# Solicita que o usuário insira uma string
texto_usuario = input("Informe uma string: ")

# Conta a letra 'a' na string
quantidade_a = conta_letra_a(texto_usuario)

# Mostra o resultado
if quantidade_a > 0:
    print(f"A letra 'a' aparece {quantidade_a} vezes na string.")
else:
    print("A letra 'a' não aparece na string.")