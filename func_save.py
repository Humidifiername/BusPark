def save(list, enter):
    with open(list, 'a') as file:
        file.write(f'{enter}\n')