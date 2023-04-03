numero = int(input("Digite um número: "))

fibonacci = [0, 1]

while fibonacci[-1] < numero:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

if numero in fibonacci:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
