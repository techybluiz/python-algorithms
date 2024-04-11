# Emprestimo de 1.000.000
# realizar pagamento daqui 5 anos
# data do emprestimo = 20/12/2020
# pagamento todo dia 20

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

valor_emprestimo = 1_000_000
fmt = '%d/%m/%Y'
data_emprestimo = datetime.strptime('20/12/2020', fmt)
data_formatada = data_emprestimo.strftime('%d/%m/%Y')
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos

data_parcelas = []
data_parcela = data_emprestimo
while data_parcela < data_final:
    data_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=+1)
    
numero_parcelas = len(data_parcelas)
valor_parcela = valor_emprestimo / numero_parcelas

for data in data_parcelas:
    print(data.strftime('%d/%m/%Y'), f'R$ {valor_parcela:,.2f}')

print()
print(
    f'Você pegou R$ {valor_emprestimo:,.2f} para pagar '
    f'em {delta_anos.years} anos '
    f'({numero_parcelas} meses) em parcelas de '
    f'R$ {valor_parcela:,.2f}.')
