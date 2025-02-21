import os
list = ["manzana", "banana", "pera", "manzana", "naranja", "pera", "pera"]

def contarElementos(list):
    dicc = {}
    for i in range(len(list)):
        for j in range (len(list[i])):
            dicc.setdefault(list[i],len(list[i]))
    return str(dicc)
    
print(contarElementos(list))

File = open('File.txt', 'w')
File.write(contarElementos(list))
File.close()
if (os.path.exists('File.txt')):
  print('el archivo se creo correctamente')
