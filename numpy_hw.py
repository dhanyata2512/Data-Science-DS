import numpy as np

array=np.arange(5,16)
print(array)

sevens = np.full((3, 3), 7)
print(sevens)

ones=np.ones((3,3),int)
print(ones*7)

n=np.arange(2,26,2)
print(n)

random_array = np.random.randint(10, 50, size=(3, 5))
print(random_array)

numbers = np.arange(1, 11)
np.random.shuffle(numbers)
print(numbers)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.ndim)
print(arr.shape)
print(arr.size)

x=np.arange(0,11)
ask=int(input("1.Linear Equation\n2.Quadratic Equation\n What type of expression do you want to evaluate ---> "))
if ask == 1:
    print("ax + b")
    a=int(input("value of a --->"))
    b=int(input("value of b--->"))
    formula=a*x+b
    print(a,"x +",b,"for x = 0 to 10 is:\n",formula)

elif ask == 2:
    print("ax^2 + bx + c")
    a=int(input("value of a --->"))
    b=int(input("value of b --->"))
    c=int(input("value of c --->"))
    formula=a*(x*x)+b*x+c
    print(a,"x^2 +",b,"x +",c,"for x = 0 to 10 is:\n",formula)

else:
    print("Try again later...")  
