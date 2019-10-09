import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

#  Cleaning up raw data (Removing commas, breaking down tabular data, changing data type)
data = pd.read_csv("/Users/ZafirKhalid/PycharmProjects/PropertyFinder/properties.csv", thousands=",")
data["Square Feet"] = data["Square Feet"].str.replace("sqft", "")
data["Square Feet"] = data["Square Feet"].str.replace(",", "").astype(int)

df = data[["Rent Price (Yearly)", "Square Feet"]]

area_x = df["Square Feet"].to_numpy()
rent_y = df["Rent Price (Yearly)"].to_numpy()

#  Splitting data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(area_x, rent_y, train_size=0.33, shuffle=True)

coefficients = np.polyfit(x_train, y_train, 1)  # Returns coefficients of best fit line as a numpy array
p4 = np.poly1d(coefficients)  # Returns best fit line equation as poly1d data type

xp = np.linspace(0, 16000, 100)
axes = plt.axes()

# Calculating r2 score to see how well line fits training and testing data sets
r2_train = r2_score(y_train, p4(x_train))
r2_test = r2_score(y_test, p4(x_test))

# Setting up scatter plots
plt.figure(1)
plt.xlabel("Area")
plt.ylabel("Rent / Yearly")
plt.title("Train Data")
plt.text(0.02, 0.9, "R2 score:" + str(r2_train), fontsize=9, transform=plt.gcf().transFigure)
plt.scatter(x_train, y_train)
plt.plot(xp, p4(xp), c="r")

plt.figure(2)
plt.xlabel("Area")
plt.ylabel("Rent / Yearly")
plt.title("Test Data")
plt.text(0.02, 0.9, "R2 score:" + str(r2_test), fontsize=9, transform=plt.gcf().transFigure)
plt.scatter(x_test, y_test)
plt.plot(xp, p4(xp), c="r")


plt.show()

