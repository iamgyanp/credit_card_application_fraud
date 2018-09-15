# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 20:31:09 2018

@author: Gyan Prakash
"""
#Set observations aside for out of time testing (say, Oct-Dec)
#Separate the rest of data into training and testing
#Once model is built, test its robustness on the first dataset
#Find KS (measure of goodness) - take cumulative distribution and calculate the difference
#Fraud detection rate - Population penetration v % of fraud found
#Catch half the fraud in 3% of the population
#Create name_dob by concatenation for unique identifier
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import os
import seaborn as sns
import re
import datetime as dt

path = "C:/Users/Gyan Prakash/OneDrive - USC Marshall School of Business/Spring 2018/DSO 562/Project 2"
os.chdir(path)

data = pd.read_csv("applications.csv")

data.dtypes

data.describe()

data.count()*100/data.shape[0]

data.shape[1]

data.head(5)

data['appdate']

data[['date_month','date_day','date_year']] = data['date'].str.split('-|\\/',expand=True)
data[['dob_month','dob_day','dob_year']] = data['dob'].str.split('-|\\/',expand=True)

data['date_year'] = 2016

data['dob_dummy'] = 19

data['dob_year'] = data['dob_dummy'].astype(str)+data['dob_year'].astype(str)

data['newdob'].head(10)

data['dob'] = data['dob_month'].astype(str)+'/'+data['dob_day'].astype(str)+'/'+data['dob_year'].astype(str)

data['date']=data['date_month'].astype(str)+'/'+data['date_day'].astype(str)+'/'+data['date_year'].astype(str)

del data['dob_dummy'], data['dob_year'], data['dob_month'], data['dob_day'], data['date_day'], data['date_month'], data['date_year']

data['ssn'].head(10)

data['ssn'] = data['ssn'].apply(lambda x: '{0:0>9}'.format(x))
data['homephone'] = data['homephone'].apply(lambda x: '{0:0>10}'.format(x))
data['zip5'] = data['zip5'].apply(lambda x: '{0:0>5}'.format(x))

data.to_csv("new_applications.csv", encoding = 'utf-8')

data['ssn'].value_counts()

data['ssn'].count

data['appdate'].unique

len(data['appdate'].unique())

data['ssn'].values

plt.plot(data['newssn'])

sns.distplot(data['date'].astype(int))

np.split(data['date'], "/")

df = pd.read_csv("new_applications.csv")
df.dtypes

df.head(5)

sns.distplot(df['date'])

df.groupby(df['ssn']).head(1)

pd.to_datetime?

df_date = pd.to_datetime(df['date']) #format='%m/%d/%Y'

df_date.dt.month

df_date.dt.week

df_date.dt.year

date = pd.crosstab(index = df['date'], columns = 'count')
date = pd.crosstab(index = df_date, columns = 'count') #Works
date
plt.plot?
plt.plot(date) #
plt.ylim(0,340)
plt.xticks(rotation=90)
#plt.figure(figsize=(20,5))
plt.tight_layout()

df_dob = pd.to_datetime(df['dob'], errors = 'coerce') #format='%m/%d/%Y'
dob = pd.crosstab(index = df_dob, columns = 'count') #Works
plt.plot(dob) 
plt.ylim(0,340)
plt.xticks(rotation=90)

df.assign(trx = np.ones(len(df.index)))\
.set_index(df_date)\
.resample(dt.timedelta(days = 7))\
.count()\
.trx\
.plot()

plt.plot(x = df_date.dt.week, y = date)

df_date = df_date.sort_values()

sns.distplot(df['ssn'], axlabel = "SSN")

sns.distplot?

plt.plot_date(df['appdate'], enter y)

df.groupby(['newssn'])

df.dtypes

pd.to_datetime(df['appdate'])

pd.pivot_table(df, index=["newssn"])


date.to_csv("appdate_count.csv")

date = pd.read_csv("appdate_count.csv")

pd.to_datetime(df['newdob'])

plt.plot_date(x=date['appdate'], y=date['count'])
sns.distplot(date['appdate'])

ssn = pd.crosstab(index = df['newssn'], columns = 'count')

ssn.to_csv("ssn_count.csv")

ssn = pd.read_csv("ssn_count.csv")

ssn['newssn'].astype(str)

plt.plot(ssn['newssn'], ssn['count']>9, linewidth = 5.0)

plt.hist(df['fraud'], bins = 2)

sns.distplot(df['fraud'])
plt.hist?

sns.distplot(df['homephone'], axlabel = "Home Phone")






