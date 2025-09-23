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
n=np.arange(1,41,2)
print(n)

#permuntation(differnt arrangments)
print(np.random.permutation(n))
print(np.random.permutation(n))
print(np.random.permutation(n))

#array of random numbers
print(np.random.randint(2,38,10))
print(np.random.randint(2,38,(3,3)))

#reshaping the array
raw=n.reshape(4,5)
print(raw)

#sorting array
random_array=np.random.randint(1,50,10)
print(random_array)
print(np.sort(random_array))

#slicing and array
print(random_array[2:7])

print(random_array[:7])
print(random_array[2:])
print(random_array[::2])
print(random_array[7:2:-1])
print(random_array[::-1])

#slicing 2D array
print(raw)
print(raw[1:3,1:4])

#selecting multiple index
print(random_array)
print(random_array[[5,6,3,4,2]])

#conditional slicing
print(random_array[random_array % 2 == 0])
print(random_array[random_array >= 20])

#evaluating expressions 
r=np.random.randint(5,15,15)
h=np.random.randint(15,20,15)
v=np.pi*r**2*h
print(r)
print(h)
print(v)
