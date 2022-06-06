#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install re')
import re

# Tests
data = [
    "enter SSN (989-45-8524):",
    "456748965", 
    "e43-45-7845", 
    "***-**-4598", 
    "4-98-4589", 
    "Social security Number is: [783-65-7485]", 
    458859635, 
    " Some text"
]

for ssn in data:
    # Grab only digit and check length of string. 
    # This line is the magik
    _ssn = "".join(re.findall(r"[\d]+", str(ssn)))

    if len(_ssn) == 9:
        print(ssn, f"{_ssn} is valid!")


# In[ ]:




