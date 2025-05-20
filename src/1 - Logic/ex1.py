# Validar um CPF (formato brasileiro) 
# utilizei o metodo de confirmar os 2 ultimos digitos

cpf = input('digite o cpf(somente os 9 primeiros digitos):')

soma = 0
i = 10
j = 0

while i > 2:
    calc = int(cpf[j]) * i
    soma += calc
    i -= 1
    j += 1
mult10 = soma * 10
rest11 = mult10 % 11
if rest11 > 9:
    cpf = cpf + str(0)
else:
    cpf = cpf + str(rest11)

# agora realizar o segundo digito

soma = 0
i = 11
j = 0

while i >= 2:
    calc = int(cpf[j]) * i
    soma += calc
    i -= 1
    j += 1
mult10 = soma * 10
rest11 = mult10 % 11
if rest11 > 9:
    cpf = cpf + str(0)
else:
    cpf = cpf + str(rest11)

print(f'cpf com os ultimos 2 digitos verificadores: {cpf}\nValidado com Sucesso!')