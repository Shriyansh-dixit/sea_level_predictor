import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Load data
    data = pd.read_csv("C:/Users/dixit/Desktop/Project 2025/Github/sea level predictor/epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'], label="Original Data", alpha=0.7)

    # First line of best fit (all data)
    slope_all, intercept_all, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))
    sea_level_all = slope_all * years_extended + intercept_all
    plt.plot(years_extended, sea_level_all, 'r', label="Best Fit (All Data)")

    # Second line of best fit (from 2000 onwards)
    recent_data = data[data['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))
    sea_level_recent = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent, sea_level_recent, 'g', label="Best Fit (2000 Onward)")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.grid(True)

    # Save plot and return for testing
    plt.savefig('sea_level_plot.png')
    return plt.gca()
