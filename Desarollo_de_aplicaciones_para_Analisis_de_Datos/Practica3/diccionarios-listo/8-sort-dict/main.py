

def run(unsorted_items: dict) -> list[tuple]:
    sorted_items = sorted(unsorted_items.items(),key = lambda item: item[1])
    return sorted_items

input_dict = {'a': 'two', 'b': 'one', 'c': 'three'}
output = run(input_dict)
print(output)
