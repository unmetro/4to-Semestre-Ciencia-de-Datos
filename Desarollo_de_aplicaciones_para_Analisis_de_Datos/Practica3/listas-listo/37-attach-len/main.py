def run(text: str) -> list:
    list_text = text.split()
    words_length = []
    for word in list_text:
        words_length.append(f"{word}:{len(word)}")
    return words_length

text = 'H0la a todos como estan'
print(run(text))


# DO NOT TOUCH THE CODE BELOW
# if __name__ == '__main__':
#     import vendor

#     vendor.launch(run)
