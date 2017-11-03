
# coding: utf-8

# In[ ]:


def anagram(a):
    list=[]
    for i in range(len(a)):
        word = a[i]
        for j in range(len(a)-1):
            for k in range(len(a)):
                if a[i] != a[k]:
                    word += a[k+j]# i am missing something near this block.
        list.append(word)
    return list 

anagram('sad')

