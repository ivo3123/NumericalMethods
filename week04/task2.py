'''
Задача 2

Един възможен подход за ефективно пресмятане на стойност на функция в точка е т.нар. lookup table
    (вж.https://en.wikipedia.org/wiki/Lookup_table).

Да се напише фунцкия lookup_table_f(x_val), която пресмята приближено стойността на функцията 𝑓(𝑥)=sin(sqrt(x))
    в интервала [0,2𝜋], като използва 2 предварително генерирани масива - f_nodes,
        съдържащ равноотдалечени на разстояние ℎ=0.01 точки в интервала [0,2𝜋] и f_values - масив от стойности на фунцкията f,
            пресметнати в точките f_nodes.
Функцията трябва да пресмята приближено стойността на 𝑓(𝑥)
    като използва кубична интерполация в най-близките до x_val възли от списъка f_nodes. За стойности на x_val,
        които принадлежат на интервалите [0,0.01] и [2𝜋−0.01,2𝜋] да се построява интерполационен полином от 𝜋2.
В случай, че подаденият аргумент x_val лежи извън интервала [0,2𝜋], да се извежда подходящо съобщение.
'''

import numpy as np

from util.lagrange_poly import lagrange_poly

def look_up_table_f(x_val, function=lambda x: np.sin(np.sqrt(x)), interval_begin=0, interval_end=2*np.pi, h=0.01):
    if x_val < interval_begin or x_val > interval_end:
        return None
    
    temp = interval_begin
    f_nodes = []
    while temp < interval_end:
        f_nodes.append(temp)
        temp += h

    offset = (interval_end - f_nodes[-1])/2

    f_nodes = [x + offset for x in f_nodes]
    f_values = function(f_nodes)

    closest_x = min(f_nodes, key = lambda curr_x: abs(curr_x - x_val))

    return lagrange_poly(np.array(f_nodes), np.array(f_values), closest_x)

print(look_up_table_f(0.02))