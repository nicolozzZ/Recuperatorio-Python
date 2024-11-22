import random
list = ['taiwan', 'china', 'hongkong', 'USE', 'argentina', 'brazil', 'rusia', 'mongolia', 'peru', 'chile']

def cambioLista(list):
    
    for i in range(len(list)):
        ramdomCountry = random.randint(list[i])
        if i < 3:
            list[i] = ramdomCountry
        if len(list)
    return list
print(cambioLista(list))
