# groupby = agrupando valores (itertools)

from itertools import groupby	

students = [
    {'name' : 'Bianca', 'score ': 'A'},
    {'name': 'Isabella', 'score ': 'A'},
    {'name': 'Estephane', 'score ': 'B'},
    {'name': 'Beatriz', 'score ': 'A'},
    {'name': 'Thor', 'score ': 'C'},
    {'name': 'Nathan', 'score ': 'D'},
    {'name': 'Marcelo', 'score ': 'A'},
    {'name': 'Bruno', 'score ': 'B'},
    {'name': 'Adriana', 'score ': 'A'},
    {'name': 'Gustavo', 'score ': 'C'},
]

def order(student):
    return student ['score']

grouped_students = sorted(students, key=order)
groups = groupby(grouped_students, key=order)

for key, group in groups:
    print(key)
    for student in group:
        print(student)