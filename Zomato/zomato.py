import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("Zomato\Zomatodata.csv")
print(df.head())

# Let's convert the data type of the "rate" column to float and remove the denominator.

def handelRate(value): # User def function
    value=str(value).split('/')
    value=value[0]
    return float(value)
df['rate']=df['rate'].apply(handelRate)
print(df.head())

# Summary of the data frame 

df.info()

# Conclusion - There is no null value in df

# Q1:
# Type of Resturant

sns.countplot(x=df['listed_in(type)'])
plt.xlabel("Type of restaurant") 
plt.show()

# Conclusion: The majority of the restaurants fall into the dinig category


# Q2:
# Dining restaurants are preferred by a larger number of individuals

grouped_data=df.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes': grouped_data})
plt.plot(result, c='green', marker="o")
plt.xlabel("type of restaurant", c="red", size=20)
plt.ylabel("Votes", c="red", size=20)
plt.show()

# Q3:

plt.hist(df['rate'],bins=5)
plt.title("Rating Distribution")
plt.show()

#Conclusion: The majority of restaurants received ratings ranging from 3.5 to 4

# Q4:
# THe Majority of couples prefer restaurants with an approximate cost of 300 rupees.

couple_df=df['approx_cost(for two people)']
sns.countplot(x=couple_df)
plt.show()

# Q5:
# Whether online orders recive higher ratings than offline orders

plt.figure(figsize=(5,5))
sns.boxplot(x = 'online_order', y='rate', data=df)
plt.show()


# Q6:
# Conclusion: offline orders recevied lower rating in comparison to online orders, which obtained excellent ratings.


pivot_table=df.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt="d")
plt.title("HeatMap")
plt.xlabel("Online Orders")
plt.ylabel("Listed In (Type)")
plt.show()