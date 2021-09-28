from matplotlib.collections import LineCollection
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    x = df["Year"]
    y = df["CSIRO Adjusted Sea Level"]

    # Create scatter plot
    fig, ax = plt.subplots()
    plt.scatter(x,y)

    # This block of commented out code(lines 18 - 23) also works, but not with respect to the included test cases. Use Jupyter notebook 
    # or any other IDE to visualize the bar plot.
    #x = df["Year"]
    #y = df["CSIRO Adjusted Sea Level"]
    #colors = df["CSIRO Adjusted Sea Level"]

    #plt.scatter(x,y,c=colors,figsize=(10,8))
    #plt.show()

    # Create first line of best fit
    slope, intercept, r, p, se = linregress(x, y)
    x_pred = pd.Series([i for i in range(1880,2050)])
    y_pred = slope*x_pred + intercept
    plt.plot(x_pred, y_pred, 'r')

    # This block of commented out code(lines 33 - 38) also works, but not with respect to the included test cases. Use Jupyter notebook 
    # or any other IDE to visualize the bar plot.
    #slope, intercept, r, p, se = linregress(x, y)

    #fig, ax = plt.subplots()
    #plt.plot(x, y, 'o', label='original data')
    #plt.plot(x, intercept + slope*x, 'r', label='fitted line')
    #plt.legend()

    # Create second line of best fit
    new_df = df.loc[df["Year"] >= 2000]
    new_x = new_df["Year"]
    new_y = new_df["CSIRO Adjusted Sea Level"]
    slope, intercept, r, p, se = linregress(new_x, new_y)
    x_pred2 = pd.Series([i for i in range(2000,2050)])
    y_pred2 = slope*x_pred2 + intercept
    plt.plot(x_pred2, y_pred2, 'y')

    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()