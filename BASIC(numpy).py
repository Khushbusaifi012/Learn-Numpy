# CREATING NUMPY ARRAYS;;
import numpy as np   #np.array
a=np.array([1,2,3])
print(a)
print(type(a))

# # 2D AND 3D ARRAYS;;
b=np.array([[1,2,3],[4,5,6]])
print(b)

c=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(c)

# DTYPE;;
d=np.array([1,2,3],dtype=float)
e=np.array([1,0,3],dtype=bool)
s=np.array([10,11,21],dtype=str)
print(d)
print(e)
print(s)

# # NP.ARANGE;;
print(np.arange(1,11))
print(np.arange(1,11,2))

# # WITH RESHAPE;;
print(np.arange(1,17).reshape(2,8))
print(np.arange(1,19).reshape(2,9))

# NP.ONES AND NP.ZEROES;;;
print(np.ones((2,4)))
print(np.zeros((2,4)))

# NP.RANDOM;;
print(np.random.random((2,3)))

# NP.LINSPACE;;;
print(np.linspace(-10,10,10))

# NP.IDENTIFY;;;;
print(np.identity(4))   #diagonal items will be 1 and other items will be 0

# ARRAY ATTRIBUTES;;
a1=np.arange(10)   #1d array called vector
a2=np.arange(12,dtype=float).reshape(3,4)    #matrix
a3=np.arange(8).reshape(2,2,2)   #3d tensor
print(a1)
print(a2)
print(a3)

# NDIM (NO OF DIMENSIONS);;
print(a1.ndim)
print(a2.ndim)
print(a3.ndim)

# SHAPE;;  (TELL US ITEMS IN DIMENSIONS);;
print(a1.shape)
print(a2.shape)
print(a3.shape)

# SIZE(NO OF ITEMS);;
print(a1.size)
print(a2.size)
print(a3.size)

# ITEMSIZE(EVERY ITEMS TELL US MEMORY SPACE);;
print(a1.itemsize)
print(a2.itemsize)
print(a3.itemsize)

# DTYPE;;
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)

# CHANGING DATATYPE;;ASTYPE
print(a3.astype(np.int32))

arr=np.array([1.5,2.8])
new_arr=arr.astype(int)    #convert float into int
print(new_arr)

# ARRAY OPERATIONS;;
a1=np.arange(12).reshape(3,4)
a2=np.arange(12,24).reshape(3,4)
print(a1)
print(a2)

# SCALAR OPERATIONS;;ARITHMETIC
print(a1*2)     #multiplication
print(a1+2)     #addition

# # RELATIONAL;;
print(a2>25)
print(a2==15)

# # VECTOR OPERATIONS;;ARITHMETIC
print(a1+a2)
print(a1*a2)

# ARRAY FUNCTIONS;;
a1=np.random.random((3,3))
a1=np.round(a1*100)
print(a1)
print(np.max(a1))    #max
print(np.min(a1))    #min
print(np.sum(a1))    #sum
print(np.prod(a1))   #prod
print(np.max(a1,axis=1))      #0->col and 1->row
print(np.min(a1,axis=0))
print(np.mean(a1))     #mean
print(np.median(a1))    #median
print(np.std(a1))       #std
print(np.var(a1))       #var

# # TRIGNOMETRIC FUNCTIONS;;
print(np.sin(a1))   #sin
print(np.cos(a1))    #cos
print(np.tan(a1))    #tan

# DOT PRODUCT;;
a2=np.arange(12).reshape(3,4)
a3=np.arange(12,24).reshape(4,3)
print(np.dot(a2,a3))    #dot
print(np.log(a3))       #log
print(np.exp(a2))       #exp
print(np.round(np.random.random((2,3))*100)) #round
print(np.floor(np.random.random((2,3))*100))  #floor
print(np.ceil(np.random.random((2,3))*100))  #ceil

# INDEXING AND SLICING;;
a1=np.arange(10)
a2=np.arange(12).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)
print(a1)
print(a2)
print(a3)
print(a1[-1])    #indexing
print(a2[0])
print(a3[1])
print(a2[1,2])    
print(a2[2,3])
print(a3[1,0,1])
print(a3[0,0,0])
print(a3[1,1,0])
print(a1[2:5])    #slicing
print(a2[0,:])
print(a2[:,2])
print(a2[::2,1::2])
print(a2[1,::3])
print(a2[0:2,1::2])

# ITERATING;;
a1=np.arange(10)
a2=np.arange(12).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)
for i in a1:
    print(i)
for i in a2:
    print(i)
for i in a3:
    print(i)
for i in np.nditer(a3):    #this will give element by element object
    print(i)
for i in np.nditer(a2):
    print(i)

# RESHAPING;;
a1=np.arange(10)
a2=np.arange(12).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)
print(np.transpose(a2))   #transpose
print(np.ravel(a2))        #ravel
print(np.ravel(a3))

# STACKING;;HORIZONTAL
a4=np.arange(12).reshape(3,4)
a5=np.arange(12,24).reshape(3,4)
print(a4)
print(a5)
print(np.hstack((a4,a5)))    #it will combines aall arrays in 1d array

# VERTICAL;;;
print(np.vstack((a4,a5)))

# SPLITTING;;HORIZONTAL;;
print(np.hsplit(a4,2))

# VERTICAL;;;
print(np.vsplit(a5,3))