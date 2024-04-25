from datetime import datetime, timedelta
from pytz import timezone
from dateutil.relativedelta import relativedelta

date_str = '2024/04/10 17:30:23'
fmt = '%Y/%m/%d %H:%M:%S'
date_inicio = datetime.strptime('2024/04/10 17:30:23', fmt)
date_fim = datetime.strptime('2024/12/12 08:20:56', fmt)
#delta = datetime.now(timezone('Asia/Tokyo')) #exibe a data e hora atualmente

delta = timedelta(days=10, hours=2) #diferença entre duas datas
print(date_fim - delta)
print(date_fim + relativedelta(seconds=59))