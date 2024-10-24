def is_perfect(n: int) -> bool:
    if n < 1:
        return False
    divisors = [1]
    for i in range(2, n):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors) == n


# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    print(is_perfect(28))
    import vendor

    vendor.launch(is_perfect)
