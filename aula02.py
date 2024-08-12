# idade = 20
# tem_cartao = False

# if idade >= 18:

#     if tem_cartao:
#         print("Você pode comprar o produto")
#     else:
#         print("Você não pode comprar o produto")

# else:
#     print("Você é menor de idade e não pode comprar o produto")


# contador = 1  # Inicializa o contador com 1

# while contador <= 5:  # Continua o loop enquanto contador for menor ou igual a 5
#     print(f"Número atual: {contador}")  # Imprime o valor atual do contador
#     contador += 1  # Incrementa o contador em 1 a cada iteração

# print("Fim da contagem.")

#Criando uma lista com alguns números

numeros = [1, 2, 3, 4, 5]

# Acessando elementos da lista
print("Primeiro número:", numeros[0])  # Acessa o primeiro elemento
print("Terceiro número:", numeros[2])  # Acessa o terceiro elemento

# Adicionando um elemento à lista
numeros.append(6)
print("Lista após adicionar um elemento:", numeros)

# Removendo um elemento da lista
numeros.remove(3)
print("Lista após remover o elemento 3:", numeros)

# Tamanho da lista
tamanho = len(numeros)
print("Tamanho da lista:", tamanho)

print("Iterando sobre a lista:")
for numero in numeros:
    print(numero)



# Criando uma tupla com alguns números
numeros = (1, 2, 3, 4, 5)

# Acessando elementos da tupla
print("Primeiro número:", numeros[0])  # Acessa o primeiro elemento
print("Terceiro número:", numeros[2])  # Acessa o terceiro elemento

# Tamanho da tupla
tamanho = len(numeros)
print("Tamanho da tupla:", tamanho)

# Iterando sobre a tupla
print("Iterando sobre a tupla:")
for numero in numeros:
    print(numero)

# Tentando modificar um elemento (vai gerar um erro, pois tuplas são imutáveis)
try:
    numeros[0] = 10
except TypeError as e:
    print("Erro ao tentar modificar a tupla:", e)

# Criando um dicionário com alguns dados
aluno = {
    "nome": "João",
    "idade": 20,
    "curso": "Engenharia",
    "notas": [9, 8, 7.5, 10]
}

# Acessando elementos do dicionário
print("Nome do aluno:", aluno["nome"])  # Acessa o valor associado à chave "nome"
print("Idade do aluno:", aluno["idade"])  # Acessa o valor associado à chave "idade"
