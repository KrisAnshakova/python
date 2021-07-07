reg = [7, 5, 3, 3, 2]
i = 0
while  len(reg) <= 8:
    new1 = int(input("Введите число- "))
    if new1==3 :
        reg.insert(4, new1)
    elif new1 == 4 or new1==5:
         reg.insert(2, new1)
    elif  new1 > 7 :
        reg.insert(0, new1)
    elif new1==7 :
        reg.insert(1, new1)
    elif new1 <= 2:
         reg.insert(5, new1)
    i = + 1
print(reg)