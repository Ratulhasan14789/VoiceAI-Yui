def generate_list():
    l = [globals()[name] for name in globals().keys() if name.startswith('list_')]
    return [item for sublist in l for item in sublist]

list_1 = [1,'x']
list_2 = [2,"shf djf"]
list_3 = [3]
asd=generate_list()
print(asd)
