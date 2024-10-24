def is_palindrome(word):
    word = word.lower()
    word = word.replace(" ", "")
    return word == word[::-1]



# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    print(is_palindrome("Never odd or even"))
    import vendor

    vendor.launch(is_palindrome)
