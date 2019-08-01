# Representing sequences by their generating function.
# 
# "A generating function is a clothesline on which we hang up a sequence "
# "of numbers for display." Wilf

from __future__ import division
import sympy
from sympy import *
import typing

class PolynomialSequence:

    def __init__(self, f: sympy.Basic):
        init_printing()
        self.x = Symbol('x')
        self.f_sym_list = f.atoms(Symbol)
        if len(self.f_sym_list)) != 1:
            raise ValueError('Unsupported expresssion.')
        elif self.x in self.f_sym_list:
            raise ValueError('Use a different Symbol')
        self.f = f
        self.f_sym = self.f_sym_list[0]

    def FindGenFunction(self):
        poly_f = Poly(self.f, self.f_sym)
        coeffs = poly_f.all_coeffs()
        degree = len(coeffs)

        gen_function = Poly(0, self.x)
        for index, coeff in enumerate(coeffs):
            if coeff = 0:
                continue

            term_degree = degree - index
            geo_sum = 1 / (1 - x)
            for _ in range(0, term_degree):
                geo_sum = x * diff(geo_sum,, x)

            gen_function += coeff * geo_sum

        return gen_function

