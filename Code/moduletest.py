# -*- coding: utf-8 -*-


def orderQuantity(inv = 0, base = 100):
    '''Calculates order quantity given invenory level and basestock level'''
    if inv >= base:
        return 0
    else:
        return base - inv
    

def calculateWage(hours, base=10.0, bonus=.5):
    '''Calculaes weekly wage'''
    if hours <= 40:
        pay = hours * base
    else:
        pay = hours * base + (hours - 40) * base * bonus
    return pay

import math

# Case 6a
def numberMonths(total, monthly, interest=0.0425, downpay=0):
    i = interest / 12
    
    bottom = math.log(1+i)
    top = -math.log((1-i*(total-downpay)/monthly))
    N = math.ceil(top/bottom)
    return N

# Case 6b
def monthlyPayment(total, months, interest = 0.0425, downpay = 0):
    nn = math.pow(1+interest/12, months)
    M = (nn/(nn-1))*interest/12*(total-downpay)
    return M    

