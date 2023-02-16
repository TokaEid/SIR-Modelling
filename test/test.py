import unittest
import numpy as np

from sir.odeSim import odeSim
from sir.discreteSim import simulateSIR

'''
Ref:
assertAlmostEqual(): https://docs.pytest.org/en/6.2.x/reference.html
'''


class TestOde(unittest.TestCase):
    '''
    Test if the result of sir.odeSim.odeSim is correct under different parameters.

    Params to be tested:
    n is the population number
    b is the number of contacts per day that are sufficient to spread the disease
    k is the fraction of the infected group that will recover during any given day 
    t is the amount of time we want to run the simulation for        
    '''
    def test_solveode_n(self):
        '''
        Test n: the population number   
        '''
        n_params = [50, 100]
        b = 0.5
        k = 1/3
        t = 200
        for n in n_params:
            sol = odeSim(n, b, k, t).solve_odes()
            s, i, r = sol.y
            for t in range(len(s)):
                sir_sum = s[t]+i[t]+r[t]
                self.assertTrue(np.isclose(sir_sum, 1, rtol=1e-4, atol=1e-6), msg=f'sum of sir = {sir_sum} is not 1 when t = {t}')

    def test_solveode_b(self):
        '''
        Test b: the number of contacts per day that are sufficient to spread the disease
        '''
        b_params = [0.25, 0.5, 0.75]
        n = 100
        k = 1/3
        t = 200       
        for b in b_params:
            sol = odeSim(n, b, k, t).solve_odes()
            s, i, r = sol.y
            for t in range(len(s)):
                sir_sum = s[t]+i[t]+r[t]
                self.assertTrue(np.isclose(sir_sum, 1, rtol=1e-4, atol=1e-6), msg=f'sum of sir = {sir_sum} is not 1 when t = {t}')

    def test_solveode_k(self):
        '''
        Test k: the fraction of the infected group that will recover during any given day 
        '''
        n = 100
        b = 0.5
        k_params = [1/3, 2/3]
        t = 200 

        for k in k_params:
            sol = odeSim(n, b, k, t).solve_odes()
            s, i, r = sol.y
            for t in range(len(s)):
                sir_sum = s[t]+i[t]+r[t]
                self.assertTrue(np.isclose(sir_sum, 1, rtol=1e-4, atol=1e-6), msg=f'sum of sir = {sir_sum} is not 1 when t = {t}')

    def test_solveode_t(self):
        '''
        Test t: the amount of time we want to run the simulation for  
        '''
        n = 100
        b = 0.5
        k = 1/3
        t_params = [100, 200]

        for T in t_params:
            sol = odeSim(n, b, k, T).solve_odes()
            s, i, r = sol.y
            for t in range(len(s)):
                sir_sum = s[t]+i[t]+r[t]
                self.assertTrue(np.isclose(sir_sum, 1, rtol=1e-4, atol=1e-6), msg=f'sum of sir = {sir_sum} is not 1 when t = {t}')

class TestDiscreteSim(unittest.TestCase):
    '''
    Test simulateSIR(n, b, k, t) in the discreteSim.py file
    '''
    def testDiscrete_n(self):
        '''
        Test n: the population number   
        '''
        n_params = [50, 100]
        b = 0.5
        k = 1/3
        t = 200
        for n in n_params:
            s, i, r = simulateSIR(n, int(n*b), k, t) # 
            for t in range(len(s)):
                sir_sum = s[t]+i[t]+r[t]
                self.assertAlmostEqual(sir_sum, n, msg=f'sum of sir = {sir_sum} is not {n} when t = {t}')


    def testDiscrete_b(self):
        '''
        Test b: the number of contacts per day that are sufficient to spread the disease
        '''
        b_params = [0.25, 0.5, 0.75]
        n = 100
        k = 1/3
        t = 200 
        for b in b_params:
            s, i, r = simulateSIR(n, int(n*b), k, t) # 
            for t in range(len(s)):
                sir_sum = s[t]+i[t]+r[t]
                self.assertAlmostEqual(sir_sum, n, msg=f'sum of sir = {sir_sum} is not {n} when t = {t}')


    def testDiscrete_k(self):
        '''
        Test k: the fraction of the infected group that will recover during any given day   
        '''
        n = 100
        b = 0.5
        k_params = [1/3, 2/3]
        t = 200 
        for k in k_params:
            s, i, r = simulateSIR(n, int(n*b), k, t) # 
            for t in range(len(s)):
                sir_sum = s[t]+i[t]+r[t]
                self.assertAlmostEqual(sir_sum, n, msg=f'sum of sir = {sir_sum} is not {n} when t = {t}')

    def testDiscrete_t(self):
        '''
        Test t: the amount of time we want to run the simulation for     
        '''
        n = 100
        b = 0.5
        k = 1/3
        t_params = [100, 200]
        for t in t_params:
            s, i, r = simulateSIR(n, int(n*b), k, t) # 
            for t in range(len(s)):
                sir_sum = s[t]+i[t]+r[t]
                self.assertAlmostEqual(sir_sum, n, msg=f'sum of sir = {sir_sum} is not {n} when t = {t}')