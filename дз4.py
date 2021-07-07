
result = []
a = list(input("Введи нескольких слов, разделённых пробелами-  ").split( ))
result.append(a)
print(sum(result, []))
for ind, el in enumerate (sum(result, []), 1):
    if len(el) > 10:
        print(ind, el[0:10])
        break
    print(ind, el)
