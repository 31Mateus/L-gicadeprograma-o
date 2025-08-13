primeiro_numero = int(input("Digite um número inteiro: "))
segundo_numero = int(input("Digite outro número inteiro: "))

print(primeiro_numero - segundo_numero)

if primeiro_numero > segundo_numero:
    primeiro_numero = primeiro_numero - segundo_numero
else:
    segundo_numero = segundo_numero - primeiro_numero