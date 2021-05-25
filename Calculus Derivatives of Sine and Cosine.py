#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sympy as sym
from IPython.display import display,Math


# In[3]:


q = sym.symbols('q')

print(sym.diff( sym.cos(q) ))
print(sym.diff( sym.sin(q) ))


# In[4]:


f = sym.cos(q)

for i in range(0,8):
    display(Math('\\frac{d}{dx}%s = %s' %(sym.latex(f),sym.latex(sym.diff(f)))))
    f = sym.diff(f)


# In[6]:


import sympy.plotting.plot as symplot

f = sym.cos(q)
clrs = 'krbg'

for i in range(0,4):
   
    if i==0:
        p = symplot(f,show=False,label=sym.latex(f),line_color=(i/5,i/3,i/5))

    else:
        p.extend( symplot(f,show=False,label=sym.latex(f),line_color=(i/5,i/3,i/5) ))
    f = sym.diff(f)
p.legend = True
p.xlim = (-3,3)
p.show()


# In[ ]:




