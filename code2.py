#Из  текста  выбрать  числа  и  записать  в  массив N.Количество чисел не более 10.
a=input()
f=[]
d=[int(i) for i in a.split() if i.isdigit()]
for i in d:
    f.append(i)
print(*f)
