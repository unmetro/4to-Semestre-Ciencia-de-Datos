def split_case(s):
    upper = []
    lower = []
    for i in s:
        if any(j.isupper() for j in i) and any(j.islower() for j in i):
            pass
        elif i.isupper():
            upper.append(i)
        else:
            lower.append(i)
    result = (lower,upper)
    return result
            



lista = ['cocodrilo', 'ZEBRA', 'MAPACHE', 'Serpiente', 'ballena']
print(f'Original list: {lista}')
print(f'Split case: {split_case(lista)}')

