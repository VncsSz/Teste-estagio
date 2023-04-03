import json

with open('dados.json') as f:
    faturamento = json.load(f)

# Cálculo do menor e maior faturamento
menor_faturamento = float('inf')
maior_faturamento = float('-inf')
for dia in faturamento:
    valor = dia['valor']
    if valor > 0:
        if valor < menor_faturamento:
            menor_faturamento = valor
        if valor > maior_faturamento:
            maior_faturamento = valor

# Cálculo da média mensal de faturamento
soma_faturamento = 0
dias_com_faturamento = 0
for dia in faturamento:
    valor = dia['valor']
    if valor > 0:
        soma_faturamento += valor
        dias_com_faturamento += 1
media_faturamento = soma_faturamento / dias_com_faturamento

# Cálculo do número de dias com faturamento acima da média
dias_acima_media = 0
for dia in faturamento:
    valor = dia['valor']
    if valor > media_faturamento:
        dias_acima_media += 1

# Impressão dos resultados
print('Menor faturamento diário:', menor_faturamento)
print('Maior faturamento diário:', maior_faturamento)
print('Número de dias com faturamento acima da média:', dias_acima_media)
