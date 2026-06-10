import pandas as pd
df=pd.read_excel('ApexPlanet_DataAnalytics_Dataset.xlsx')
df['Order_Date']=pd.to_datetime(df['Order_Date'])
df['Age']=df['Age'].fillna(df['Age'].median())
df['City']=df['City'].fillna(df['City'].mode()[0])
df.to_excel('Cleaned_ApexPlanet_Dataset.xlsx',index=False)
print('Cleaning completed')
