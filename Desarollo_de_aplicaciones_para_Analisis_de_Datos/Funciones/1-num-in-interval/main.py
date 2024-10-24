def in_range(n, start, end):
    return start <= n <= end



n = 5
start = 1
end = 10
print(f'Is {n} in the interval [{start}, {end}]? {in_range(n, start, end)}')
