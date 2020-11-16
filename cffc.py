def cf(tempc):
    tempf = (9 / 5) * tempc + 32
    return tempf

def fc(tempf):
    tempc = (tempf - 32) * (5 / 9)
    return tempc

def primo(lista):
    for l in lista:
        count = 2
        while l > count:
            if l % count == 1:
                print('Número ',l,' é primo')
            count = count + 1

print(cf(float(input('Insira temperatura em celsius:'))))
print(fc(float(input('Insira temperatura em celsius:'))))
primo(range(100))
