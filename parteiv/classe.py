class Cell(object):
    """
    Classe para células de planilha
    """

    def __init__(self, formula='', format='%s'):
        self.formula = formula
        self.format = format
    
    def __repr__(self):
        return self.format % eval(self.formula)

print(Cell('123*2'))

class Calc:
    
    def __init__(self, formula, **args):
        self.formula = formula
        self.vars = vars
    
    def __recalc(self):
        self.__res = eval(self.formula, self.vars)
    
    def __repr__(self):
        self.__recalc()
        return str(self.__res)

formula = '2*x + 3*y +z**2'
cc = Calc(formula, x=2, y=3, z=1)
# c = cc.vars('x')
# print(c)
# print('x = ',cc.vars['x'],' calc =', calc)


class User():

    def __init__(self, name):
        self.name = name

def set_password(self, password):
    self.password = password

print('Classe original ',dir(User))

User.set_password = set_password
print('Classe modificada:', dir(User))
user = User('guest')
user.set_password('guest')

print('Objeto:', dir(User))
# print('Senha:', user.password)