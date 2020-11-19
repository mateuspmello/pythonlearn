def cf(tempc):
    tempf = (9 / 5) * tempc + 32
    return tempf

def fc(tempf):
    tempc = (tempf - 32) * (5 / 9)
    return tempc

def primo(lista):
    for l in lista:
        count = 1
        primo = 1
        while l > count:

            if count == 1 or count == l:
                count = count + 1
                continue
            else:
                if l % count == 0:
                    count = l
                    count = count + 1
                    primo = 0
                    continue 
            
            count = count + 1

        if primo == 1:
            print(l,'é primo')
            
def unir_lista(l):
    lista1 = ()
    for l1 in l:
        lista1 += l1
    return lista1

#print(cf(float(input('Insira temperatura em celsius:'))))
#print(fc(float(input('Insira temperatura em celsius:'))))
primo(range(20))
li = [(1,23),
    (1,2,3,4),
    (45,6,7,8,98,6,1)]
print(unir_lista(li))
