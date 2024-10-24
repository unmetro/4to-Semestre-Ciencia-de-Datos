def extract_evens(numbers):
    return [number for number in numbers if number % 2 == 0]


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f'Original list: {numbers}')
    print(f'Even numbers: {extract_evens(numbers)}')
    import vendor

    vendor.launch(extract_evens)
