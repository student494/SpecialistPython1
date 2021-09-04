# Даны два словаря:
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
# Объедините их в один
for keys, values in dictionary_2.items():
    dictionary_1[keys] = values
print(dictionary_1)
