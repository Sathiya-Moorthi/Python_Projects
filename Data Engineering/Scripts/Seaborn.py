import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
# Sample DataFrame
data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [4, 7, 1, 8]
}
df = pd.DataFrame(data)

# Plotting a bar plot with Seaborn
sns.barplot(x='Category', y='Values', data=df)
plt.title('Seaborn Bar Plot')
plt.show()
