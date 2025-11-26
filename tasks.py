def custom_hash(name):
    total = 0
    for char in name:
        total += ord(char)
    return total % 10


def create_hash_table():
    students = ["Salohiddin", "Akmal", "Ruslan"]
    table = {}
    for name in students:
        index = custom_hash(name)

        if index not in table:
            table[index] = [name]
        else:
            table[index].append(name)

    return table


hash_table = create_hash_table()
print(hash_table)
