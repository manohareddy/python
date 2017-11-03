
# coding: utf-8

# In[81]:

def latin(num):
    lst =[]                                      #initiate list
    for n in range(1,num+1):                     #n in range of 1 to input number
        sublst = [n]                             #initiate sublist
        for i in range(n,num+1):                 #i in range of 1 to input number
            if i != n:                           #making sure number isnt repeated
                sublst.append(i)                 #add number to sublist
        lst.append(sublst)                       #add sublist to main list  
        for j in range(1, n):
            if j != n:                           #making sure number isnt repeated
                sublst.append(j)
    for sub in lst:                              #for each sublist in list
        x = ''                                   #initiate variable 
        for g in sub:                            #for each element of sublist
            x = x + ' ' + str(g)                 #add the element to a string
        print(x)                                 #print string


# In[82]:

latin(3)


# In[ ]:



