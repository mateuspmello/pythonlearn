
for num in [12,13,14]:
    if num % 3 == 0:
        print('o numero é', num)
    else:
        print('o numero não é', num)

temp = int(input('Entre com a temperatura'))

if temp < 0:
    print('Congelando')
elif 0 <= temp <= 20:
    print('Frio')
elif 21 <= temp <= 40:
    print('Quente')
else:
    print('Muito Quente')

for n in range(2,100,2): 
    print(n)
else:
    print('nao')
    