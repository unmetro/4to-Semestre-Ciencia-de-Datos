def run(words: list) -> dict:
    group_words = dict()
    for color in words:
        first_letter = color[0]
        if first_letter not in group_words:
            group_words[first_letter] = []
        group_words[first_letter].append(color)
    return group_words

list_colors = ['blue','black','red','green','white']
print(run(list_colors))

# # DO NOT TOUCH THE CODE BELOW
# if __name__ == '__main__':
#     import vendor

#     vendor.launch(run)
