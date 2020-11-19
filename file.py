import sys
import csv
import time

temp = open('temp.txt','w')

for i in range(100):
    temp.write('%3d\n' % i)

temp.close()

temp = open('temp.txt')

for x in temp:
    sys.stdout.write(x)

temp.close()

# print (open('temp.txt').readlines())

dt = (
    ('temperatura',15,'C','10:40','2020-01-01'),
    ('temperatura',15,'C','10:40','2020-01-01')
)

cso = open('cs.csv','w')
fl = csv.writer(cso)
fl.writerows(dt)
cso.close()


with open('cs.csv','r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=',')
    for col in leitor:
        sys.stdout.write('%s\n' % str(col))


print(time.localtime())
