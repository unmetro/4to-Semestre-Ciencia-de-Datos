def run(start: float, stop: float, step: float) -> list:
    values = list()
    value = start
    while value <= stop:
        values.append(value)
        value += step
    return values

start = 0
stop = 1
step = 0.21

print(f'lista frange: {run(start,stop,step)}')

# # DO NOT TOUCH THE CODE BELOW
# if __name__ == '__main__':
#     import vendor

#     vendor.launch(run)
