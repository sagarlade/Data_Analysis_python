import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Call CSV File #

df = pd.read_csv("student_exam_score.csv")


print(df.head())

#showing info about dataset
df.info()

df.isnull().sum()

#Drop unnamed column

df=df.drop("Unnamed: 0", axis=1)
print(df.head())

#change weekly study hours column

df["WklyStudyHours"] = df["WklyStudyHours"].str.replace("05-Oct", "5-10")
df.head()

#gender distribution showing in plot
plt.figure(figsize=(5,5))
ax= sns.countplot(data=df, x="Gender")
ax.bar_label(ax.containers[0])
plt.show()

# From above chart we have analysed that 
# the number of females in the data is more than the male

gb=df.groupby("ParentEduc").agg({"MathScore":"mean", "ReadingScore":"mean", "WritingScore":"mean"})
print(gb)
plt.figure(figsize=(5,5))
sns.heatmap(gb, annot=True)
plt.title("Relationship between Parent's Eduction and Student's Score")
plt.show()

#From above chart we have  concluded that the education of the parents have a good impact

gb1=df.groupby("ParentMaritalStatus").agg({"MathScore":"mean", "ReadingScore":"mean", "WritingScore":"mean"})
print(gb1)
plt.figure(figsize=(5,5))
sns.heatmap(gb1, annot=True)
plt.title("Relationship between Parent's Marital Status and Student's Score")
plt.show()


# Box plot MathScore

sns.boxenplot(data=df, x="MathScore")
plt.show()

print(df['EthnicGroup'].unique())

groupA=df.loc[(df["EthnicGroup"]=="group A")].count()
print(groupA)