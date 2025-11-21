import matplotlib.pyplot as plt
import numpy as np
import random as r
from sklearn.linear_model import LinearRegression as LR

number_of_data_points = 100
max_x_value = 50
max_y_value = 40
exact_slope = 2
exact_intercept = 3
noise_range = 20
random_noise = 0
x_value_list = []
y_value_list = []


while True:
    # GENERATE X AND Y VALUES AT RANDOM
    for i in range(number_of_data_points):

        xtemp = r.randint(0, max_x_value)

        random_noise = r.uniform(-noise_range, noise_range)
        x_value_list.append(xtemp)
        y_value_list.append( exact_slope * int(xtemp) + exact_intercept + random_noise)


    # Check values
    #print(f"X Values: {x_value_list}\nY Values: {y_value_list}")

    # PLOTTING
    plt.figure(figsize=(20, 10))
    plt.scatter(x_value_list, y_value_list, s=25, alpha=0.7, label="Data Points")


    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.title("Generated Training Data")


    # From here, the ML model creation begins.
    X = np.array(x_value_list).reshape(-1, 1)
    y = np.array(y_value_list)

    model = LR()
    model.fit(X, y)

    slope = model.coef_[0]
    intercept = model.intercept_

    y_pred = model.predict(X)

    plt.plot([0, max_x_value], [exact_intercept, exact_slope*max_x_value+exact_intercept], linewidth=5, label='"Exact" Regression Line', color="green")
    plt.plot(X, y_pred, linewidth=3, label="ML Regression Line", color="red")


    plt.legend()
    plt.show()
