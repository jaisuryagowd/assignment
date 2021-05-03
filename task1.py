#!/usr/bin/env python
# coding: utf-8

# ![logo.jpg](attachment:logo.jpg)

# # Nunam - Assessment task

# ## Creating csv files from excel sheets

# ## Task1
# ### 1. Create 3 separate *'*.csv'* files named 'detail.csv', 'detailVol.csv' and 'detailTemp.csv'.
# #### 1. Combine all the data in sheets named like "Detail_67_" only, among the two data files provided, and save into 'detail.csv'
# #### 2. Combine all the data in sheets named like "DetailVol_67_" only, among the two data files provided, and save into'detailVol.csv' 
# #### 3. Combine all the data in sheets named like "DetailTemp_67_" only, among the two data files provided, and save into 'detailTemp.csv'

# ### Installing xlrd package
# #### xlrd package is used to retrieve information from spreadsheet

# In[6]:


pip install xlrd


# ### Creating csv files
# #### Reading corresponding sheets from the given excel files and writing it into dataframes. All the dataframes, each containing a sheet information, are concatenated into a single dataframe. Using 'to_csv' function, the resultant dataframe is converted into corresponding csv file.

# In[7]:


import pandas as pd
df1 = pd.read_excel('data.xls', sheet_name ='Detail_67_1_1')
df2 = pd.read_excel('data.xls', sheet_name ='Detail_67_1_1_1')
df3 = pd.read_excel('data.xls', sheet_name ='Detail_67_1_1_2')
df4 = pd.read_excel('data.xls', sheet_name ='Detail_67_1_1_3')
df5 = pd.read_excel('data.xls', sheet_name ='Detail_67_1_1_4')
df6 = pd.read_excel('data.xls', sheet_name ='Detail_67_1_1_5')
df7 = pd.read_excel('data.xls', sheet_name ='Detail_67_1_1_6')
frames1 = [df1, df2, df3, df4, df5, df6, df7]
final_df = pd.concat(frames1)
final_df.to_csv('detail.csv')
print("CSV file :'detail.csv' created")


# In[8]:


import pandas as pd
df1 = pd.read_excel('data.xls', sheet_name ='DetailVol_67_1_1')
df2 = pd.read_excel('data.xls', sheet_name ='DetailVol_67_1_1_1')
df3 = pd.read_excel('data.xls', sheet_name ='DetailVol_67_1_1_2')
df4 = pd.read_excel('data.xls', sheet_name ='DetailVol_67_1_1_3')
df5 = pd.read_excel('data.xls', sheet_name ='DetailVol_67_1_1_4')
df6 = pd.read_excel('data.xls', sheet_name ='DetailVol_67_1_1_5')
df7 = pd.read_excel('data.xls', sheet_name ='DetailVol_67_1_1_6')
frames2 = [df1, df2, df3, df4, df5, df6, df7]
final_df = pd.concat(frames2)
final_df.to_csv('detailvol.csv')
print("CSV file :'detailvol.csv' created")


# In[9]:


import pandas as pd
df1 = pd.read_excel('data.xls', sheet_name ='DetailTemp_67_1_1')
df2 = pd.read_excel('data.xls', sheet_name ='DetailTemp_67_1_1_1')
df3 = pd.read_excel('data.xls', sheet_name ='DetailTemp_67_1_1_2')
df4 = pd.read_excel('data_1.xls', sheet_name ='DetailTemp_67_1_1_3')
df5 = pd.read_excel('data_1.xls', sheet_name ='DetailTemp_67_1_1_4')
df6 = pd.read_excel('data_1.xls', sheet_name ='DetailTemp_67_1_1_5')
df7 = pd.read_excel('data_1.xls', sheet_name ='DetailTemp_67_1_1_6')
frames3 = [df1, df2, df3, df4, df5, df6, df7]
final_df = pd.concat(frames3)
final_df.to_csv('detailtemp.csv')
print("CSV file :'detailtemp.csv' created")

