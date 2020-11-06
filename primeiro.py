from string import Template 

for num in [12,13,14]:
    if num % 3 == 0:
        print('o numero é', num)
    else:
        print('o numero não é', num)

temp = 20

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

musicos = [('axel','cantor','feliz'),
('kurt','cantor','triste')]

#msg = '{1} é {2} e está {3}'

#for nome, profissao, estado in musicos:
#    print(msg.format(nome, profissao, estado))

st = Template('$aviso aconteceu em $quando')

s = st.substitute({'aviso':'Falta de Eletrecidade',
'quando':'03 de abril de 2022'})

print(s)