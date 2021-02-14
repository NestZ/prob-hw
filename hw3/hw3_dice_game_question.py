# -*- coding: utf-8 -*-
"""
Homework 3 - Question 6. Dice game 

@Student_name: Thaneat Saithong
@Student_ID: 610610587

"""

import numpy as np

# Write your code below
def dice():
    return 1 + np.random.choice(6, size=(2, int(1e7)))

p1 = np.sum(dice(), axis=0)
p2 = np.sum(dice(), axis=0)

p1_w = (p1 >= 2 * p2).sum() / int(1e7)
p2_w = (p2 >= 2 * p1).sum() / int(1e7)

print(1 - p1_w - p2_w)