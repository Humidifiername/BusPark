def read(list):
    result = []
    with open(list, 'r') as file:
        for line in file:
            result.append(line)
        return print(result)