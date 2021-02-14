# -*- coding: utf-8 -*-
"""
Homework 3 - Question 5. Sampling (Family of Bernoulli trials)

@Student_name: Thaneat Saithong
@Student_ID: 610610587

"""

import numpy as np
import math

def sampling_bernoulli(p):
    ##########################
    # Complete this function
    # You have to use np.random.rand()
    res = np.random.rand()
    if res < p:
        return 1
    else:
        return 0
    
def sampling_binomial(n, p):
    ##########################
    # Complete this function
    # You have to call sampling_bernoulli()
    res = 0
    for _ in range(n):
        if sampling_bernoulli(p) == 1:
            res += 1
    return res
    
def sampling_geometric(p):
    ##########################
    # Complete this function
    # You have to call sampling_bernoulli()
    res = 1
    while sampling_bernoulli(p) != 1:
        res += 1
    return res
        
def sampling_negbinomial(n, p):
    ##########################
    # Complete this function
    # You have to call sampling_bernoulli()    
    cnt = 0
    res = 0
    while cnt < n:
        if sampling_bernoulli(p) == 1:
            cnt += 1
        res += 1
    return res
        
def sampling_poisson(lambd):
    ##########################
    # Complete this function
    # You have to call sampling_binomial() 
    return sampling_binomial(300, lambd / 300)
        
def sampling_exponential(lambd):
    ##########################
    # Complete this function
    # You have to call sampling_geometric()
    return 0.001 * sampling_geometric(lambd * 0.001)

#-----------------------------------------------
#-----------------------------------------------
# You may not have to change the code below.

#------------------
#  Check Bernoulli distribution
#------------------
def bernoulli_check(p):
    
    import matplotlib.pyplot as plt
    from collections import Counter        
    from scipy.stats import bernoulli    

    n_sim = 100000

    # Compare binomial distribution
    plt.figure()      
    plt.title('Bernoulli distribution')
    
    # Simulation    
    x = [sampling_bernoulli(p) for _ in range(n_sim)] 
    count = Counter(x)
    count = np.array(sorted(count.items()))
    plt.stem(count[:,0], count[:,1]/n_sim, use_line_collection=True, label='Sim PMF')    
    plt.ylabel('PMF')
        
    # True PMF    
    true_pmf = np.array([(i,bernoulli.pmf(i,p)) for i in [0,1]])
    plt.plot(true_pmf[:,0], true_pmf[:,1],'g-x', label='True PMF')

    plt.xlabel('$x$')    
    plt.legend()
    plt.savefig('hw3_bernoulli.png', dpi=150)

#------------------
#  Check Binomial distribution
#------------------
def binomial_check(n,p):
    
    import matplotlib.pyplot as plt
    from collections import Counter        
    from scipy.stats import binom    

    n_sim = 100000

    # Compare binomial distribution
    plt.figure()      
    plt.title('Binomial distribution')
    
    # Simulation    
    x = [sampling_binomial(n,p) for _ in range(n_sim)] 
    count = Counter(x)
    count = np.array(sorted(count.items()))
    plt.stem(count[:,0], count[:,1]/n_sim, use_line_collection=True, label='Sim PMF')    
    plt.ylabel('PMF')
        
    # True PMF    
    true_pmf = np.array([(i,binom.pmf(i,n,p)) for i in range(n+1)])
    plt.plot(true_pmf[:,0], true_pmf[:,1],'g-x', label='True PMF')

    plt.xlabel('$x$')
    plt.xticks(range(0,n+1))
    plt.legend()
    plt.savefig('hw3_binomial.png', dpi=150)


#------------------
#  Check Geometric distribution
#------------------
def geometric_check(p):
    
    import matplotlib.pyplot as plt
    from collections import Counter        
    from scipy.stats import geom

    n_sim = 100000
    max_display = 20

    # Compare geometric distribution
    plt.figure()      
    plt.title(f'Geometric distribution (show up to x={max_display})')
    
    # Simulation    
    x = [sampling_geometric(p) for _ in range(n_sim)] 
    count = Counter(x)
    count = np.array(sorted(count.items()))
    plt.stem(count[:,0], count[:,1]/n_sim, use_line_collection=True, label='Sim PMF')    
    plt.ylabel('PMF')
        
    # True PMF    
    true_pmf = np.array([(i,geom.pmf(i,p)) for i in range(1,max_display+1)])
    plt.plot(true_pmf[:,0], true_pmf[:,1],'g-x', label='True PMF')

    plt.xlabel('$x$')
    plt.xlim(0,max_display)
    plt.xticks(range(1,max_display+2))
    plt.legend()
    plt.savefig('hw3_geometric.png', dpi=150)


#------------------
#  Check negative binomial distribution
#------------------
def negative_binomial_check(n,p):
    
    import matplotlib.pyplot as plt
    from collections import Counter        
    from scipy.stats import nbinom

    n_sim = 200000
    max_display = 50

    # Compare negative binomial distribution
    plt.figure()      
    plt.title(f'Negative binomial distribution (show up to x={max_display})')
    
    # Simulation    
    x = [sampling_negbinomial(n,p) for _ in range(n_sim)] 
    count = Counter(x)
    count = np.array(sorted(count.items()))
    plt.stem(count[:,0], count[:,1]/n_sim, use_line_collection=True, label='Sim PMF')    
    plt.ylabel('PMF')
        
    # True PMF    
    true_pmf = np.array([(i,nbinom.pmf(i,n,p)) for i in range(1,max_display+1)])
    true_pmf[:,0] = n + true_pmf[:,0] # Change support from the number of failures to the number of trials
    plt.plot(true_pmf[:,0], true_pmf[:,1],'g-x', label='True PMF')

    plt.xlabel('$x$')
    plt.xlim(0,max_display)
    plt.xticks(range(5,max_display+1,5))
    plt.legend()
    plt.savefig('hw3_negbinomial.png', dpi=150)


#------------------
#  Check Poisson distribution
#------------------
def poisson_check(lambd):
    
    import matplotlib.pyplot as plt
    from collections import Counter        
    from scipy.stats import poisson    

    n_sim = 100000

    # Compare poisson distribution
    plt.figure()      
    plt.title(f'Poisson distribution $\lambda$ = {lambd}')
    
    # Simulation    
    x = [sampling_poisson(lambd) for _ in range(n_sim)] 
    count = Counter(x)
    count = np.array(sorted(count.items()))
    plt.stem(count[:,0], count[:,1]/n_sim, use_line_collection=True, label='Sim PMF')    
    plt.ylabel('PMF')
    x_max = count[:,0].max()+1
        
    # True PMF        
    true_pmf = np.array([(i,poisson.pmf(i,lambd)) for i in range(x_max)])
    plt.plot(true_pmf[:,0], true_pmf[:,1],'g-x', label='True PMF')

    plt.xlabel('$x$')
    plt.xticks(range(0,x_max))
    plt.legend()
    plt.savefig('hw3_poisson.png', dpi=150)


#------------------
#  Check Exponential distribution
#------------------
def exponential_check(lambd):
    
    import matplotlib.pyplot as plt
    from collections import Counter        
    from scipy.stats import expon   

    n_sim = 100000

    # Compare exponential distribution
    plt.figure()      
    plt.title(f'Exponential distribution $\lambda$ = {lambd}')
    
    # Simulation    
    x = [sampling_exponential(lambd) for _ in range(n_sim)] 
    plt.hist(x, bins=200, density=True, label='Sim PDF')    
    plt.ylabel('PDF')    
    x_max = np.max(x)
        
    # True PDF        
    x = np.arange(0,x_max,0.01)
    true_pdf = expon.pdf(x,scale=1/lambd)
    plt.plot(x, true_pdf,'r-', label='True PDF')

    plt.xlabel('$x$')    
    plt.legend()
    plt.savefig('hw3_exponential.png', dpi=150)


#---------------------------------------------
# Function call:
# Comparison of probability distribution
bernoulli_check(0.3)
binomial_check(10, 0.3)
geometric_check(0.3)
negative_binomial_check(10, 0.3)
poisson_check(5)
exponential_check(5)

