import numpy as np

# Creating numpy array
''' Numpy array is similar to python list
but has additional information about shape and
dimension of the array'''

a = np.array([0, 1, 2, 3, 4, 5])

print(a)
print(a.ndim) # dimension of array
print(a.shape) # row X column

# Transforming the 1D numpy array into 2D

b = a.reshape(3,2)

print(b)
print('Dimension of b', b.ndim) # dimension
print('Shape of b ', b.shape) # row X column

'''Changing the values of the b array also changes
the value of a array as it is mutable '''
b[1][0] = 77

print(b)
print(a)

"""In case we don't want to reflect the change in the orignal array (a in this case),
we could use copy """

c = a.reshape(3, 2).copy()
c[1][0] = 88

print(c)
print(a)

''' We could also create the new array as
    which python list don't support
'''
d = np.array([0, 1, 2, 3, 4, 5])

print(d*2)
print(d**2)

# Ordinary python list
print([1, 2, 3, 4]*2)

#Indexing
'''We could access the numpy array as '''
print(a[np.array([2, 3, 4])])

''' Condition check '''
# checking whether the elements are greater than 4 or not
print(a>4)

# accessing the elements of numpy array 'a' which are greater than 4
print(a[a>4])

# Trimming the greater than 4 value
a[a>4]  = 4
print(a)

# Trimming could be also done as
print(a.clip(0, 3))

# Handling Non Existing Values

e = np.array([1, 2, np.NAN, 3, 4])

print(e)
print(np.isnan(e)) # checking whether the elements are non-existent or not

print(e[~np.isnan(e)]) # Clipping out the non-existent elements

print(np.mean(e[~np.isnan(e)])) # finding the mean of the elements

'''
    Usually NumPy array has no flexiblity as that of python lists, which can hold basically any thing.
    NumPy array always have only one datatype
'''

print(a.dtype) #data type

f = np.array([1 , "Text"])
print(f.dtype)

g = np.array([1, "Text", set([1, 2, 3, 4, 3])])
print(g)
print(g.dtype)

# Arange
print(np.arange(4)) # list of number up to 4
print(np.arange(5, 10)) # list of number from 5 to 9
print(np.arange(5, 10 , 2)) # The third parameter specifies step size

# Linspace
'''
    Returns list equally spaced number
    It is closed closed interval. Both the starting and ending numbers are included in list
    while arange() is not close interval. it is closed open interval, the first starting parameter is included while the end number is not
'''
print(np.linspace(0, 25, 9)) # Returns list of numbers including 0 and 25 containing 9 numbers in between
print(np.linspace(0, 25, 9, retstep=True)) # Returns list of numbers including 0 and 25 containing 9 numbers in between and stepsize

''' Multi dimensional array '''
# One Dimensional One Matrix
print(np.ones(5))

# Two Dimensional Zero Matrix
print(np.zeros((5,2))) # 5 rows X 2 Columns

# Three Dimensional Matrix
print(np.ones((5,4,3))) # 5 Group of matrices each of 4 row and 3 columns

