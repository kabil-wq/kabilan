#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
train_df = pd.read_csv(r"C:\Users\kabil\Downloads\train.csv")


# In[2]:


# Check for missing values
print("Missing values before cleaning:")
print(train_df.isnull().sum())

# Fill missing values for numeric columns with the mean
train_df['Age'].fillna(train_df['Age'].mean(), inplace=True)
train_df['Fare'].fillna(train_df['Fare'].mean(), inplace=True)

# Fill missing values for categorical columns with the mode
train_df['Embarked'].fillna(train_df['Embarked'].mode()[0], inplace=True)

# Optionally, drop rows with missing values if necessary
# train_df.dropna(inplace=True)

# Check data types
print("\nData types:")
print(train_df.dtypes)


# In[4]:


# Inspect missing values
print("Missing values before handling:")
print(train_df.isnull().sum())

# Fill missing values for 'Age' and 'Fare' with mean (or use other strategies if preferred)
train_df['Age'].fillna(train_df['Age'].mean(), inplace=True)
train_df['Fare'].fillna(train_df['Fare'].mean(), inplace=True)

# Check missing values again
print("\nMissing values after handling:")
print(train_df.isnull().sum())


# In[5]:


# Calculate summary statistics for numeric columns
numeric_cols = ['Age', 'Fare']

# Mean
mean_values = train_df[numeric_cols].mean()
print("\nMean values:\n", mean_values)

# Median
median_values = train_df[numeric_cols].median()
print("\nMedian values:\n", median_values)

# Mode
mode_values = train_df[numeric_cols].mode().iloc[0]
print("\nMode values:\n", mode_values)

# Standard Deviation
std_dev_values = train_df[numeric_cols].std()
print("\nStandard deviation values:\n", std_dev_values)


# In[6]:


# Inspect data types and summary statistics for all columns
print("\nData types:")
print(train_df.dtypes)

print("\nSummary of data:")
print(train_df.describe(include='all'))  # Comprehensive overview


# In[ ]:




