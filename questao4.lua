faturamento_sp = 67836.43
faturamento_rj = 36678.66
faturamento_mg = 29229.88
faturamento_es = 27165.48
faturamento_outros = 19849.53

# Calculando o valor total mensal da distribuidora
total_faturamento = faturamento_sp + faturamento_rj + faturamento_mg + faturamento_es + faturamento_outros

# Calculando o percentual de representação de cada estado
perc_representacao_sp = (faturamento_sp / total_faturamento) * 100
perc_representacao_rj = (faturamento_rj / total_faturamento) * 100
perc_representacao_mg = (faturamento_mg / total_faturamento) * 100
perc_representacao_es = (faturamento_es / total_faturamento) * 100
perc_representacao_outros = (faturamento_outros / total_faturamento) * 100

print("Percentual de representação de cada estado no faturamento mensal da distribuidora:")
print("SP: {:.2f}%".format(perc_representacao_sp))
print("RJ: {:.2f}%".format(perc_representacao_rj))
print("MG: {:.2f}%".format(perc_representacao_mg))
print("ES: {:.2f}%".format(perc_representacao_es))
print("Outros: {:.2f}%".format(perc_representacao_outros))
