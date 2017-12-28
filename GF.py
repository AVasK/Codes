from euclid import euclid

import numpy as np
from numpy.polynomial.polynomial import *

"""
Pretty good thing to remember: numpy polynomials are [a_0, a_1, ..., a_n] <!>
"""

"""
Realization of F2 class:
    
"""
def value(obj):
    return int(obj)

class F2:
    # consists of : value (0, 1) + operations

    def __init__(self, value):
        self.value = value % 2

    def __neg__(self):
        return F2(-self.value)

    def __int__(self):
        return self.value

    def __repr__(self):
        return str(self.value)

    def __eq__(self, other):
        if value(self) == value(other):
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other : int):
        return F2((value(self) + value(other)) % 2)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return F2((value(self) - value(other)) % 2)

    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        return F2((value(self) * value(other)) % 2)

    def __rmul__(self, other):
        return F2((value(self) * value(other)) % 2)

    def __rtruediv__(self, other):
        return self.__truediv(other)

    def __truediv__(self, other):
        if other == 0:
            raise RuntimeError("Don't divide by zero, please")
        return self



class Poly(Polynomial):
    def notNull(self):
        if self.degree() == 0 and self.coef[0] == 0:
            return False
        return True
    

class F2q(Poly):
    P = []
    
    def __mul__(self, other):
        res = self.Poly.__mul__(other)
        res = res % P

    """ This method is for setting P """
    def setP(self, value):
        type(self).P = value
    
    """ This method is for getting P """
    def getP(self):
        return type(self).P


a_args = [1, 0, 1] # x^2 + 1
b_args = [0, 1] # x 

a_args = [F2(x) for x in a_args]
b_args = [F2(x) for x in b_args]

poly_a = Poly(a_args)
poly_b = Poly(b_args)

F2q_1 = F2q(a_args)
F2q_2 = F2q(b_args)
p_x = F2q(b_args)

p_x.setP(Poly([1,0,1]))

#F2q.P = Poly([0,1,1])
print("P:",F2q_1.P)
print(F2q_1.getP())

def Testing(poly_a, poly_b):
    res = euclid(poly_a, poly_b)
    for x in res:
        print(x)

    print('---')
    print("{0} = {1} * {2} + {3} * {4} = {5}".format(res[0], poly_a, res[1], poly_b, res[2], res[1] * poly_a + res[2] * poly_b))

Testing(poly_a, poly_b) # Success!
Testing(poly_b, poly_a) # Success!










