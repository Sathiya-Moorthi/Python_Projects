import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame
data = {
    'Date': pd.date_range(start='1/1/2023', periods=10),
    'Value': [10, 15, 12, 17, 19, 21, 22, 24, 23, 25]
}
df = pd.DataFrame(data)

# Plotting a line plot
df.plot(x='Date', y='Value', kind='line', title='Custom Line Plot')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()
