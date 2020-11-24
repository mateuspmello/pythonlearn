import functools

from math import log10
from string import ascii_lowercase


#######
#lambda
#######
amp = lambda x, y, z: (x**2 + y**2 + z**2)**.5

print(amp(1,2,3))

###########
#mapeamento
###########
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(list(map(log10, nums)))


##########
#filtragem
##########
print(list(filter(lambda x: x == 3, nums)))


##########
#redução
##########
nums = range(100)

print(functools.reduce(lambda x,y : x+y, nums))

#############
#transposicao
#############

print(ascii_lowercase)
print (list(zip(ascii_lowercase, range(1,100))))
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list(zip(*matriz)))

###################
#list comprehension
###################

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print([x for x in nums if x % 2])


###################
#list comprehension
###################
instrumentais = [
    ('King Crimson', 'Fracture'),
    ('Metallica','Call of Ktulu'),
    ('Yes', 'Mood for a Day'),
    ('Pink Floyd', 'One of This Days'),
    ('Rush', 'YYZ')
]

print( sorted(faixa[-1] + '/' + faixa[0]
    for faixa in instrumentais if
    faixa[0].upper() < 'N')
    )