
z = [1,'b','c','d']

for e in z:
    print(e)

z[-1] = 'e'
z.append('b')
z.remove(1)
z.sort()
print('----------')
for i,e in enumerate(z):
    print(i,' => ',e)

tupla = (1,2,3)
primeiroelemento = tupla[0]
print(primeiroelemento)

s1 = set(range(3))
s2 = set(range(10,7,-1))
s3 = set(range(2,10,2))

print('s1:', s1, '\ns2:', s2, '\ns3:', s3)

#dicionário
dic = {'nome':'Mateus', 'sobrenome':'Mello', 'idade':38}
print(dic.items())