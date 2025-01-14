import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('CarPrice_Assignment.csv')
print(df)
x = df[['horsepower']]
y = df['price']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(x_train, y_train)

score = model.score(x_test, y_test)
print('R^2 Score:', score)