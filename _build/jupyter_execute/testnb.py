#!/usr/bin/env python
# coding: utf-8

# ## Finding the Root (Zero) of a Function
# 
# Finding the root, or zero, of a function is a very common task in exploratory computing. This Notebook presents the Bisection method and Newton's method for finding the root, or 0, of a function. 

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
plt.ion()


# In[2]:


def f(x):
    return x**3

x = np.linspace(-2, 2, 100)
y = f(x)
plt.axhline(0, ls='--', c='r')
plt.plot(x, y)
plt.show()


# ### Bisection method
# Given a continuous function $f(x)$ and two values of $x_1$, $x_2$ such that $f(x_1)$ and $f(x_2)$ have opposite signs the Bisection method is a root-finding method that repeatedly bisects the interval $[x_1, x_2]$ and then selects a subinterval (in which a root must be) for further processing. (Since $f(x_1)$ and $f(x_2)$ have opposite signs, it follows that $f(x)$ is zero somewhere between $x_1$ and $x_2$.) The Bisection method iterate towards the zero of the function by cutting the root search interval in half at every iteration. The method calculates the middle point $x_m$ between $x_1$ and $x_2$ and compute $f(x_m)$ and then replaces either $x_1$ or $x_2$ by $x_m$ such the values of $f$ at the end points of the interval are of opposite signs. The process is repeated until the interval is small enough that its middle point can be considered a good approximation of the root of the function. In summary, the algorithm works as follows:
# 
# 1. Compute $f(x_1)$ and $f(x_2)$ 
# 2. Compute $x_m = \frac{1}{2}(x_1 + x_2)$.
# 3. Compute $f(x_m)$.
# 4. If $f(x_m)f(x_2) < 0$, replace $x_1$ by $x_m$, otherwise, replace $x_2$ by $x_m$.
# 5. If $|x_1 - x_2|<\varepsilon$, where $\varepsilon$ is a user-specified tolerance, return $\frac{1}{2}(x_1 + x_2)$, otherwise return to step 2.
