def extract_evens(numbers):
    return [number for number in numbers if number % 2 == 0]



numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Original list: {numbers}')
print(f'Even numbers: {extract_evens(numbers)}')

