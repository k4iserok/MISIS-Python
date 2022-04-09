#Посчитать количество определенных слов в файле


with open('raspisanie.txt', 'r', encoding="utf-8") as raspisanie:
    predmet = raspisanie.readlines()
    lec=[]
    lab=[]
    pract=[]
    for i in predmet:
        if 'лек' in i:
            lec.append(i)
        elif 'прак' in i:
            pract.append(i)
        elif 'лаб' in i:
            lab.append(i)
print(f'{len(lec)} Лекций')
print(f'{len(lab)} Лабораторных')
print(f'{len(pract)} Практик')

