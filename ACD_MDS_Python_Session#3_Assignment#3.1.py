# Program myreduce 
from functools import reduce
input_lst =[47,11,42,13]
def myreduce(lst):
    return(reduce(lambda x,y: x+y,lst))
print(myreduce(input_lst))

# Program myfilter
def odd_check(num):
    if num%2 != 0:
        return True
def myfilter(lst):
    return(list(filter(odd_check,lst)))  
num_lst =range(50)    
print(myfilter(num_lst))
