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

# ### Exercise 1 (max 2 points)
#
# A recent exploration of Venus has discovered a new organism, now known as *Sarchiapus Examinis*. The data collected about *Sarchiapi E.* individuals are available in the file `data.csv`. For each individual the DNA, an age in days, and a length in centimeters were recorded. 
#
# Read the data in a Pandas DataFrame.
#

pass

# ### Exercise 2 (max 3 points)
#
# Plot the distribution of length.

pass

# ### Exercise 3 (max 5 points)
#
# Collect in a new Pandas DataFrame the mean and standard deviation of length for each age.

pass

# ### Exercise 4 (max 5 points)
#
# The gender of a *Sarchiapus E.* individual is defined by the first letter of its DNA: an `'A'` or a `'C'` is considered a male, otherwise is considered a female. Add a column to the data with the gender.

pass

# ### Exercise 5 (max 3 points)
#
# Plot the distribution of length for male *Sarchiapi E.*.
#

pass

# ### Exercise 6 (max 7 points)
#
#
# Define a function `count_twins` that takes a string and a character and returns how many times the substring composed by the character repeated twice can be found in the whole string. For example, if the string is `'ZXXZXXXZCCCX'`, and the character `'X'`, the result should be 3.
#
# To get the full marks, you should declare correctly the type hints (the *signature* of the function) and add a doctest string. 

pass

# ### Exercise 7 (max 5 points)
#
# Using the function defined in Exercise 5, add a column `a_twins` with the number of `'A'` twins in the DNA of each *Sarchiapus E.*.

pass

# ### Exercise 8 (max 3 points)
#
# Consider the hypothesis that the length of each *Sarchiapus E.* is normally distributed with a mean equal to the number of `'A'` twins in its DNA and a standard deviation that you assume to be uniformed distributed between 0 and 10. Code this statistical hypothesis as a PyMC3 model and plot the distribution of the standard deviation after having seen the collected data.

pass
