#usando calendar para calendarios e datas

# ultimo dia do mes -> monthrange
# nome e numero do dia -> weekday

import calendar

# print(calendar.calendar(2024))
# print(calendar.month(2024, 4))
primeiro_dia , ultimo_dia = (calendar.monthrange(2024, 4))
print(calendar.day_name[primeiro_dia])
print(calendar.weekday(2022, 12, ultimo_dia))