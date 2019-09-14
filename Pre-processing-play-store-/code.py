# --------------
#Importing header files
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv(path)
# print(data['Rating'].value_counts())
data.hist(column = 'Rating')

data = data[data['Rating'] <= 5]
data.hist(column = 'Rating')

#Code starts here


#Code ends here


# --------------
# code starts here
total_null = data.isnull().sum()
percent_null = (total_null/data.isnull().count())



missing_data = pd.concat([total_null,percent_null],axis=1,keys=['Total','Percent'])
print(missing_data)

data = data.dropna()

total_null_1 = data.isnull().sum()
percent_null_1 = (total_null_1/data.isnull().count())

missing_data_1 = pd.concat([total_null_1,percent_null_1],axis=1,keys=['Total','Percent'])
print(missing_data_1)

# code ends here


# --------------

#Code starts here


sns.catplot(x="Category",y="Rating",data=data, kind="box" , height = 10)
plt.xticks(rotation=90)
plt.title('Rating vs Category [BoxPlot]')

#Code ends here


# --------------
#Importing header files
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

#Code starts here

#Removing `,` from the column
data['Installs']=data['Installs'].str.replace(',','')

#Removing `+` from the column
data['Installs']=data['Installs'].str.replace('+','')

#Converting the column to `int` datatype
data['Installs'] = data['Installs'].astype(int)

#Creating a label encoder object
le=LabelEncoder()

#Label encoding the column to reduce the effect of a large range of values
data['Installs']=le.fit_transform(data['Installs'])

#Setting figure size
plt.figure(figsize = (10,10))

#Plotting Regression plot between Rating and Installs
sns.regplot(x="Installs", y="Rating", color = 'teal',data=data)

#Setting the title of the plot
plt.title('Rating vs Installs[RegPlot]',size = 20)

#Code ends here



# --------------
#Code starts here
print(data['Price'])

data['Price'] = data['Price'].str.replace('$','')
# data['Installs']=data['Installs'].str.replace('+','')

data['Price'] = data['Price'].astype(float)

f = sns.regplot(x="Price", y="Rating" , data=data)

plt.title('Rating vs Price [RegPlot]')

#Code ends here


# --------------

#Code starts here
print(data['Genres'].unique())
data['Genres'] = data['Genres'].str.split(';').str[0]

gr_mean=data[['Genres', 'Rating']].groupby(['Genres'], as_index=False).mean()

print(gr_mean.describe())

#Sorting the grouped dataframe by Rating
gr_mean=gr_mean.sort_values('Rating')

print(gr_mean.head(1))

print(gr_mean.tail(1))

#Code ends here


# --------------

#Code starts here

data['Last Updated']=pd.to_datetime(data['Last Updated'])
print(data['Last Updated'])

max_date = max(data['Last Updated'])

data['Last Updated Days'] = (max_date - data['Last Updated']).dt.days

print(data['Last Updated Days'])

sns.regplot(x="Last Updated Days", y="Rating", data=data)

plt.title('Rating vs Last Updated [RegPlot]')
#Code ends here


