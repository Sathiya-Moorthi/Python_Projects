import pandas as pd
from runtime import runtime

file_path = r"D:\Gayu's Project\titanic_dataset.csv"
df = pd.read_csv(file_path)
# print(df)
# print(df.info())
# print(df.describe())
# print(df.columns)
# print(df.shape)
# print(f"ROWS:{df.shape[0]} Columns: {df.shape[1]}")
# print("ROWS:{} Columns: {}".format(df.shape[0],df.shape[1]))
# print(df.at[890, "PassengerId"])
# print(type(df["PassengerId"]))
# print(df.loc[99])
# print(df.sample(5))
df1 = df.PassengerId > 5
# print(df[df1].Fare)
df_copy = df.copy()
# print(df_copy.drop("Fare", axis=1, inplace=True))


# print(df_copy.drop("Sex", axis=1, inplace=True))
# print(df_copy.columns)


df = df.groupby('Sex')[['Survived', 'Pclass']].sum()
print(df)

runtime()
