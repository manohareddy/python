
# coding: utf-8

# In[20]:

def egyptian(a,b):
    y={a:b}
    while a>=1:
        c=a
        a = a//2
        if a>0:
            y[a]=y[c]*2
    sum=0        
    for key, value in y.items():
        if key%2 != 0:
            sum = sum+value
    return sum           


# In[21]:

egyptian(21,30)


# In[ ]:



