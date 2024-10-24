def in_range(n, start, end):
    return start <= n <= end


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    n = 5
    start = 1
    end = 10
    print(f'Is {n} in the interval [{start}, {end}]? {in_range(n, start, end)}')
    import vendor

    vendor.launch(in_range)
