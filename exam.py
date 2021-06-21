# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # Programming in Python
# ## Exam: June 21, 2021
#
#
# You can solve the exercises below by using standard Python 3.9 libraries, NumPy, Matplotlib, Pandas, PyMC3.
# You can browse the documentation: [Python](https://docs.python.org/3.9/), [NumPy](https://numpy.org/doc/stable/user/index.html), [Matplotlib](https://matplotlib.org/stable/contents.html), [Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html), [PyMC3](https://docs.pymc.io/).
# You can also look at the [slides of the course](https://homes.di.unimi.it/monga/lucidi2021/pyqb00.pdf) or your code on [GitHub](https://github.com).
#
# **It is forbidden to communicate with others.** 
#

# %matplotlib inline
import numpy as np   # type: ignore
import pandas as pd  # type: ignore
import matplotlib.pyplot as plt # type: ignore
import pymc3 as pm   # type: ignore

# ### Exercise 1 (max 2 points)
#
# A recent exploration of Venus has discovered a new organism, now known as *Sarchiapus Examinis*. The data collected about *Sarchiapi E.* individuals are available in the file `data.csv`. For each individual the DNA, an age in days, and a length in centimeters were recorded. 
#
# Read the data in a Pandas DataFrame.
#

df = pd.read_csv('data.csv', index_col=0)

df.head()

# ### Exercise 2 (max 3 points)
#
# Plot the distribution of length.

# +
fig, ax = plt.subplots()

_ = ax.hist(df['length'], bins='auto', density=True)
# -

# ### Exercise 3 (max 5 points)
#
# Collect in a new Pandas DataFrame the mean and standard deviation of length for each age.

ldf = pd.DataFrame({'mean length': df.groupby('age').mean()['length'], 
                    'std length': df.groupby('age').std()['length']})
ldf

# ### Exercise 4 (max 5 points)
#
# The gender of a *Sarchiapus E.* individual is defined by the first letter of its DNA: an `'A'` or a `'C'` is considered a male, otherwise is considered a female. Add a column to the data with the gender.

df['gender'] = (df['dna'].str.startswith('A') | df['dna'].str.startswith('C')).map(lambda x: 'M' if x else 'F') 

df.head()

# ### Exercise 5 (max 3 points)
#
# Plot the distribution of length for male *Sarchiapi E.*.
#

fig, ax = plt.subplots()
_ = ax.hist(df[df['gender'] == 'M']['length'], bins='auto', density=True)


# ### Exercise 6 (max 7 points)
#
#
# Define a function `count_twins` that takes a string and a character and returns how many times the substring composed by the character repeated twice can be found in the whole string. For example, if the string is `'ZXXZXXXZCCCX'`, and the character `'X'`, the result should be 3.
#
# To get the full marks, you should declare correctly the type hints (the *signature* of the function) and add a doctest string. 

def count_twins(s: str, c: str) -> int:
    """Return how many times c*2 can be found in s.
    >>> count_twins('ZXXZXXXZCCCX', 'X')
    3
    """
    if len(s) < 2:
        return 0
    sub = count_twins(s[1:], c)
    if s[0] == s[1] and s[0] == c:
        return 1 + sub
    return sub


count_twins('ZXXZXXXZCCCX', 'X')

# ### Exercise 7 (max 5 points)
#
# Using the function defined in Exercise 5, add a column `a_twins` with the number of `'A'` twins in the DNA of each *Sarchiapus E.*.

df['a_twins'] = df['dna'].map(lambda x: count_twins(x, 'A'))

df.head()

# ### Exercise 8 (max 3 points)
#
# Consider the hypothesis that the length of each *Sarchiapus E.* is normally distributed with a mean equal to the number of `'A'` twins in its DNA and a standard deviation that you assume to be uniformed distributed between 0 and 10. Code this statistical hypothesis as a PyMC3 model and plot the distribution of the standard deviation after having seen the collected data.

# +
mymodel = pm.Model()

with mymodel:
    sigma = pm.Uniform('sigma', 0, 10)
    slen = pm.Normal('length', df['a_twins'], sigma, observed=df['length'])
    post = pm.sample()
# -

with mymodel:
    pm.plot_posterior(post)
