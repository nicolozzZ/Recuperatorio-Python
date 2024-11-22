list = ["manzana", "banana", "pera", "manzana", "naranja", "pera", "pera"]

def contarElementos(list):
    dicc = {}
    for i in range(len(list)):
        for j in range (len(list[i])):
            dicc.setdefault(list[i],len(list[i]))
    return dicc
    
print(contarElementos(list))
