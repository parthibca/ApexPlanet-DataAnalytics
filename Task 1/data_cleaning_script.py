import pandas as pd

df = pd.read_excel("Sales Transaction Dataset.xlsx")

# Missing Value Treatment

df['Age'].fillna(df['Age'].median(), inplace=True)

df['City'].fillna(df['City'].mode()[0], inplace=True)

# Date Conversion

df['Order_Date'] = pd.to_datetime(df['Order_Date'])

# Verify Sales

df['Calculated_Sales'] = df['Quantity'] * df['Unit_Price']

# Feature Engineering

df['Order_Month'] = df['Order_Date'].dt.month_name()

df['Age_Group'] = pd.cut(
    df['Age'],
    bins=[18,30,45,60,100],
    labels=['Young','Adult','Middle Age','Senior']
)

df['Revenue_Group'] = pd.cut(
    df['Total_Sales'],
    bins=[0,50000,150000,500000],
    labels=['Low','Medium','High']
)

# Save Cleaned Dataset

df.to_csv("Cleaned_Sales_Dataset.csv", index=False)

print("Data Cleaning Completed Successfully")
print(df.info())