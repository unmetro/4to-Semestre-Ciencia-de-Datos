def run(values: list) -> list:
    for i in range(len(values)+1):
        if values[i] != i:
            values.insert(i,i)
    return values

values = [0,1,3,5]
print(f"lista completada: {run(values)}")


# # DO NOT TOUCH THE CODE BELOW
# if __name__ == '__main__':
#     import vendor

#     vendor.launch(run)
