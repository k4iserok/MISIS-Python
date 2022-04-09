# Средний бал и список отстающих учеников

import statistics as stat
with open ('spisok.txt','r',encoding='utf-8') as spisok:
    spisokk = spisok.read().split('\n')
    ocenki = [i[-1] for i in spisokk]
    med = stat.median(ocenki)
    bad = [i for i in spisokk if i[-1] < med]
print(f'Медианой оценок является: {med}\nСписок плохих учеников: {bad}')













