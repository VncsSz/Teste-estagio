texto = "exemplo de string"

# Convertendo a string em uma lista de caracteres
lista_caracteres = list(texto)

# Obtendo o tamanho da lista de caracteres
tamanho = len(lista_caracteres)

# Invertendo os caracteres da lista
for i in range(tamanho // 2):
    temp = lista_caracteres[i]
    lista_caracteres[i] = lista_caracteres[tamanho - i - 1]
    lista_caracteres[tamanho - i - 1] = temp

# Convertendo a lista de caracteres em uma string
texto_invertido = "".join(lista_caracteres)


print(texto_invertido)
