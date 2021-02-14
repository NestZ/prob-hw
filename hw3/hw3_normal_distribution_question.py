# -*- coding: utf-8 -*-
"""
Homework 3 - Question 2. Normal distribution

@Student_name: Thaneat Saithong
@Student_ID: 610610587

"""

import numpy as np
from scipy.stats import norm

# Write your code below

# Problem A
# find px(1.8 <= x <= 2.75)
# p1 = px1(x1 <= 2.75)
# p2 = px2(x2 <= 1.8)
# ans = p2 - p1
p1 = norm.cdf(1.8, loc=2, scale=0.5)
p2 = norm.cdf(2.75, loc=2, scale=0.5)
print(p2 - p1)

# Problem B
# find x for q1
ans =norm.ppf(0.25, loc=2, scale=0.5)
print(ans)