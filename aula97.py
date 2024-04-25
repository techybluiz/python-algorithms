# cpf = input('Digite somente os numeros do cpf:' )
# print()
# soma = 0

# for i in range(9):
#     soma += int(cpf[i]) * (10-i)

# resto = soma * 10 % 11
# if resto > 9:
#     primeiro_digito = 0
# else:
#     primeiro_digito = resto

# print(f'O primeiro digito do cpf é {primeiro_digito}')

cpf = '36955577026'
nove_digitos = cpf[:9]
contador = 10

resultado_1 = 0
for digito in nove_digitos:
    resultado_1 += int(digito) * contador
    contador -= 1
digito1 = (resultado_1 * 10) % 11
print(f'O primeiro digito é {digito1}')

dez_digitos = nove_digitos + str(digito1)
contador_segundo = 11
resultado_2 = 0
for digito in dez_digitos:
    resultado_2 += int(digito) * contador_segundo
    contador_segundo -= 1
digito2 = (resultado_2 * 10) % 11
print(f'O segundo digito é {digito2}')





