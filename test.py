import pandas as pd

data = pd.read_csv('Temperatures.csv')
print(data.head().to_string(index=False))
data['Temperature'] = data['Temperature'].convert_objects(convert_numeric=True)
print(data['Temperature'].describe())
print(data['Temperature'].mean())

rslt_df = data.loc[data['Date'].str.contains('Mar-2012')]
print(rslt_df.head())
print(rslt_df.describe())