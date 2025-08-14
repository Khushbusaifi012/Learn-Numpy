import numpy as np
#SOME FUNCTIONS;;
a=np.random.randint(1,100,15)
b=np.random.randint(1,100,24).reshape(6,4)
print(a)
print(b)
print(np.sort(a))    #SORTED
print(np.sort(b))
print(np.sort(b,axis=0))
print(np.append(a,100))    #append in last 
print(np.append(b, np.ones((b.shape[0], 1)), axis=1))    #append in every column

# CONCATENATION;;
a=np.arange(6).reshape(2,3)
d=np.arange(6,12).reshape(2,3)
print(a)
print(d)
print(np.concatenate((a,d),axis=0))   #concatenation in vertically
print(np.concatenate((a,d),axis=1))   #concatenation in horizontally

# UNIQUE;;
a=np.array([1,1,2,2,3,3,4,4,5,5,6,6])
print(a)
print(np.unique(a))    #unique

# # EXPAND_DIMS;;
print(np.expand_dims(a,axis=0))    #expand_dims

# WHERE;;
a=np.array([1,50,70,46,78,90,100,23,26,78])
print(a)
print(np.where(a>50))    #find all numbers with value greater than 50
print(np.where(a>50,0,a))    #replace all values>50 with 0
print(np.where(a%2==0,0,a))

# ARGMAX;;
a=np.random.randint(1,100,15)
b=np.random.randint(1,100,24).reshape(6,4)
print(a)
print(b)
print(np.argmax(a))     #argmax
print(np.argmax(b,axis=0))
print(np.argmin(a))     #argmin

# CUMSUM;;
print(np.cumsum(a))    #cumpsum
print(np.cumprod(a))   #cumprod
 
# PERCENTILE AND HISTOGRAM;;
print(np.percentile(a,100))      #percentile
print(np.histogram(a,bins=[0,10,20,30,40,50,60,70,80,90]))     #histogram

# CORRELATION;;
salary=np.array([20000,40000,25000,35000,60000])
experience=np.array([1,3,2,4,2])
print(np.corrcoef(salary,experience))       #corrcoef

# ISIN;;
items=[10,20,30,40,50,60,70,80,90]
print(np.isin(a,items))
print(np.flip(a))      #flip

# PUT AND DELETE;;
print(np.put(a,[0,1],[110,530]))
print(a)
print(np.delete(a,0))     #delete

# SET FUNCTIONS;;np.union
m=np.array([1,2,3,4,5])
n=np.array([3,4,5,6,7])
print(np.union1d(m,n))      #union1d      
print(np.intersect1d(m,n))    #intersect1d
print(np.setdiff1d(m,n))    #setdiff1d
print(np.setxor1d(m,n))      #setoxr1

# CLIP;;
print(np.clip(a,a_min=25,a_max=75))
print(np.clip(a,a_min=78,a_max=90))
import numpy as np
#SOME FUNCTIONS;;
a=np.random.randint(1,100,15)
b=np.random.randint(1,100,24).reshape(6,4)
print(a)
print(b)
print(np.sort(a))    #SORTED
print(np.sort(b))
print(np.sort(b,axis=0))
print(np.append(a,100))    #append in last 
print(np.append(b, np.ones((b.shape[0], 1)), axis=1))    #append in every column

# CONCATENATION;;
a=np.arange(6).reshape(2,3)
d=np.arange(6,12).reshape(2,3)
print(a)
print(d)
print(np.concatenate((a,d),axis=0))   #concatenation in vertically
print(np.concatenate((a,d),axis=1))   #concatenation in horizontally

# UNIQUE;;
a=np.array([1,1,2,2,3,3,4,4,5,5,6,6])
print(a)
print(np.unique(a))    #unique

# # EXPAND_DIMS;;
print(np.expand_dims(a,axis=0))    #expand_dims

# WHERE;;
a=np.array([1,50,70,46,78,90,100,23,26,78])
print(a)
print(np.where(a>50))    #find all numbers with value greater than 50
print(np.where(a>50,0,a))    #replace all values>50 with 0
print(np.where(a%2==0,0,a))

# ARGMAX;;
a=np.random.randint(1,100,15)
b=np.random.randint(1,100,24).reshape(6,4)
print(a)
print(b)
print(np.argmax(a))     #argmax
print(np.argmax(b,axis=0))
print(np.argmin(a))     #argmin

# CUMSUM;;
print(np.cumsum(a))    #cumpsum
print(np.cumprod(a))   #cumprod
 
# PERCENTILE AND HISTOGRAM;;
print(np.percentile(a,100))      #percentile
print(np.histogram(a,bins=[0,10,20,30,40,50,60,70,80,90]))     #histogram

# CORRELATION;;
salary=np.array([20000,40000,25000,35000,60000])
experience=np.array([1,3,2,4,2])
print(np.corrcoef(salary,experience))       #corrcoef

# ISIN;;
items=[10,20,30,40,50,60,70,80,90]
print(np.isin(a,items))
print(np.flip(a))      #flip

# PUT AND DELETE;;
print(np.put(a,[0,1],[110,530]))
print(a)
print(np.delete(a,0))     #delete

# SET FUNCTIONS;;np.union
m=np.array([1,2,3,4,5])
n=np.array([3,4,5,6,7])
print(np.union1d(m,n))      #union1d      
print(np.intersect1d(m,n))    #intersect1d
print(np.setdiff1d(m,n))    #setdiff1d
print(np.setxor1d(m,n))      #setoxr1

# CLIP;;
print(np.clip(a,a_min=25,a_max=75))
print(np.clip(a,a_min=78,a_max=90))