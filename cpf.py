import re

entrada_cpf = input ('Digite o cpf:')

entrada_cpf = re.sub(
        r'[^0-9]',
        '',
        entrada_cpf
)
if len(entrada_cpf) != 11:
        raise ValueError('CPF deve conter 11 digitos')
if not entrada_cpf.isdigit():
        raise ValueError('CPF deve conter apenas números')

valor_sequencia = entrada_cpf == entrada_cpf[0] * len(entrada_cpf)
primeiro_caractere_entrada_repetido = valor_sequencia * \
    len(entrada_cpf)
print(entrada_cpf , primeiro_caractere_entrada_repetido)

