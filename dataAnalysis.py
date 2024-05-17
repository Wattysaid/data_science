import seaborn as sns
import matplotlib.pyplot as plt

# Descriptive statistics
print(df.describe())

# Correlation matrix
print(df.corr())

# Visualisation
sns.heatmap(df.corr(), annot=True)
plt.show()

# Machine Learning
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = df[['feature1', 'feature2']]
y = df['target']

# Splitting data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Training a model
model = LinearRegression()
model.fit(X_train, y_train)

# Making predictions
predictions = model.predict(X_test)
