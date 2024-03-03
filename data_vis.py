import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
 # Assuming you have the dataset (CSV file) in the same directory as your notebook
titanic_data = pd.read_csv('titanic.csv')
print(titanic_data.head())

# Get a summary of the dataset
print(titanic_data.info())

# Check for missing values
print(titanic_data.isnull().sum())
# Handle missing values based on your analysis (e.g., fill with mean, median, or drop columns)
#titanic_data['Age'].fillna(titanic_data['Age'].median(), inplace=True)
titanic_data['Age'] = titanic_data['Age'].fillna(titanic_data['Age'].median())

# Explore relationships using visualizations
sns.countplot(x='Survived', hue='Pclass', data=titanic_data)
plt.show()

# Explore correlations
numeric_columns = titanic_data.select_dtypes(include=np.number)
correlation_matrix = numeric_columns.corr()
titanic_data_numeric = titanic_data.select_dtypes(include=np.number)
correlation_matrix = titanic_data_numeric.corr()
#correlation_matrix = titanic_data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.show()
# Save the cleaned data to a new CSV file
titanic_data.to_csv('cleaned_titanic_data.csv', index=False)