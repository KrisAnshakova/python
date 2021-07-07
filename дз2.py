list1=[]
i = 0
while i <= 6:
    y = int(input("Введи переменную до 10- "))
    if y <= 10:
       # y = list(y)
        list1.extend([y])
        i = i + 1
    else:
        print("Условие не выполненно")
print(tuple(list1))
l1, l2, l3, l4,l5, l6,l7 =tuple(list1)
l1, l2, l3, l4,l5, l6,l7 = l2, l1, l4, l3, l6, l5, l7
print(l1, l2, l3, l4,l5, l6,l7)