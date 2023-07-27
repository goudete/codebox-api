import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("iris.csv", header=None)
df.columns = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]

# Create a color dictionary for each class label
color_dict = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}

# Map the class labels to numbers
df['color'] = df['class'].map(color_dict)

df.plot.scatter(x="sepal_length", y="sepal_width", c="color", colormap="viridis")
plt.show()