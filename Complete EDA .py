#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


pd.read_csv("diabetes.csv")


# In[3]:


df=pd.read_csv("diabetes.csv")


# In[4]:


pip install dtale


# In[5]:


import dtale

import dtale.app as dtale_app


# In[6]:


dtale.show(df, ignore_duplicate=True)


# In[7]:


pip install pandas-profiling


# In[8]:


import sys
get_ipython().system('{sys.executable} -m pip install pandas-profiling')


# In[9]:


from markupsafe import escape


# In[10]:


pip install Jinja2==3.0.3


# In[11]:


import pandas as pd
import pandas_profiling
from pandas_profiling import ProfileReport
from pandas_profiling.utils.cache import cache_file


# In[12]:


pandas_profiling.__version__


# In[13]:


import pandas_profiling as pp


# In[14]:


profile = ProfileReport(df)


# In[15]:


profile


# In[16]:


# import libraries
import sweetviz as sv
import numpy as np
import pandas as pd


# randomly shuffle dataframe then split into two
shuffled = df.sample(frac=1)
df_train, df_test = np.array_split(shuffled, 2) 

# generate the report with sweetviz
report = sv.compare(df_train, df_test)

# this function will pop-up the report in browser, and also save it
report.show_html()


# In[17]:


from dataprep.datasets import load_dataset
from dataprep.eda import create_report
create_report(df).show()


# In[18]:


import klib
import pandas as pd
klib.missingval_plot(df)


# In[19]:


df_cleaned = klib.data_cleaning(df)
df_cleaned


# In[ ]:




