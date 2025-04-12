import numpy as np

# NUMPY ARRAYS VS PYTHON LISTS;;
# SPEED AND LIST TIME EXECUTION;;
# a=[i for i in range(100000)]
# b=[i for i in range(100000,200000)]
# c=[]
# import time
# start=time.time()
# for i in range(len(a)):
#     c.append(a[i]+b[i])
# print(time.time()-start)

# NUMPY EXECUTION ACCORDING TO TIME;;
# a=np.arange(100000)
# b=np.arange(100000,200000)
# start=time.time()
# c=a+b
# print(time.time()-start)

# IN TERMS OF MEMORY;;SPACE OCCUPIED
# a=[i for i in range(100000)]    #python list
# import sys
# print(sys.getsizeof(a))

# a=np.arange(100000)    #numpy
# print(sys.getsizeof(a))

# ADVANCED INDEXING;;FANCY INDEXING
# a1=(np.arange(24).reshape(6,4))
# print(a1)
# print(a1[[0,2,3]])
# print(a1[[0,2,3,4]])
# print(a1[:,[0,2,3]])

# BOOLEAN INDEXING;;
# a=np.random.randint(1,100,24).reshape(6,4)
# print(a)
# # FIND ALL NUMBERS GREATER THAN 50?
# print(a>50)
# print(a[a>50])   #given some conditions

# # FIND OUT EVEN NUMBERS?
# print(a%2==0)
# print(a[a%2==0])

# # FIND ALL NUMBERS GREATER THAN 50 AND ARE EVEN?
# print((a > 50) & (a % 2 == 0))
# print(a[(a > 50) & (a % 2 == 0)])

# # FIND ALL NUMBERS ARE DIVISIBLE BY 7?
# print(a%7==0)
# print(a[a%7==0])
# print(a[(a != 7) & (a == 0)])

# BROADCASTING;;SAME SHAPE;;
# a=np.arange(6).reshape(2,3)
# b=np.arange(6,12).reshape(2,3)
# print(a)
# print(b)
# print(a+b)

# DIFF SHAPE;;
# a=np.arange(6).reshape(2,3)
# b=np.arange(3).reshape(1,3)
# print(a)
# print(b)
# print(a+b)

# MORE EXAMPLES;;
# a=np.arange(12).reshape(4,3)
# b=np.arange(3)
# print(a)
# print(b)
# print(a+b)

# a=np.arange(12).reshape(3,4)
# b=np.arange(3)
# print(a)
# print(b)   
# print(a+b)    #this will give us error

# a=np.arange(3).reshape(1,3)
# b=np.arange(3).reshape(3,1)
# print(a)
# print(b)
# print(a+b)

# WORKING WITH MATHEMATICAL FORMULAS;;
# def sigmoid(array):
#     return 1/(1+np.exp(-(array)))      #sigmoid function
# a=np.arange(100)
# print(sigmoid(a))

# actual=np.random.randint(1,50,25)
# predicted=np.random.randint(1,50,25)
# def mse(actual,predicted):    
#     return np.mean(actual-predicted)**2   #mse function

# print(actual)
# print(predicted)
# print(mse(actual,predicted))

# WORKING WITH MISSING VALUES;;
# a=np.array([1,2,3,4,np.nan,6])
# print(a)
# print(np.isnan(a))
# print(a[~np.isnan(a)])    #to remove the missing values

# 1.PLOTTING GRAPHS;;;;PLOTTING A 2D PLOT X=Y STRAIGHT LINE GRAPH
import matplotlib.pyplot as plt
# x=np.linspace(-10,10,100)
# print(x)
# y=x
# print(y)
# print(plt.plot(x,y))
# plt.title("Simple Line Graph")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# print(plt.show())

# 2.y*x^2;;PARABOLA
# x=np.linspace(-10,10,100)
# y=x**2
# print(plt.plot(x,y))
# plt.title("Parabola Graph")
# plt.xlabel("x-axis")
# plt.ylabel("y-axis")
# print(plt.show())

# 3.y=sin(x)graph;;
# x=np.linspace(-10,10,100)
# y=np.sin(x)
# print(plt.plot(x,y))
# print(plt.show())

# 4.y=xlog(x) graph;;
# x=np.linspace(-10,10,100)
# y=x*np.log(x)
# print(plt.plot(x,y))
# print(plt.show())

# 5.SIGNOID GRAPH;;
# x=np.linspace(-10,10,100)
# y=1/(1+np.exp(-x))
# print(plt.plot(x,y))
# print(plt.show())

