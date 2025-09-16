import numpy as np
numbers=[3,13,14,6,7]
print(numbers)
print(type(numbers))

#change list to array
array=np.array(numbers)
print(array)
print(type(array))

#double the numbers in the list
double=[]
for number in numbers:
    d=number*2
    double.append(d)
print(double)

#double the numbers in the array
print(array*2)

#array of 0s
zero=np.zeros(10,int)
#default data type is float--np.zeros(10,int) the array is now a int
print(zero)

zero_2d=np.zeros((3,5),int)
print(zero_2d)

#arrays of 1s
ones=np.ones(((3,3,4)),int)
print(ones)

#finding dimensions
print(zero.ndim)
print(zero_2d.ndim)
print(ones.ndim)

#finding shape
print(zero.shape)
print(zero_2d.shape)
print(ones.shape)

#finding size
print(zero.size)
print(zero_2d.size)
print(ones.size)

#array with numbers in range
n=np.arange(0,41,2)
print(n)

#permuntation(differnt arrangments)
print(np.random.permutation(n))
print(np.random.permutation(n))
print(np.random.permutation(n))

#array of random numbers
print(np.random.randint(2,38,10))
print(np.random.randint(2,38,(3,3)))
