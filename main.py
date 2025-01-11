import sea_level_predictor

if __name__ == "__main__":
    # Generate and display the plot
    ax = sea_level_predictor.draw_plot()

    # Show the plot (optional, for manual testing)
    print("Plot generated successfully. Displaying the plot...")
    import matplotlib.pyplot as plt
    plt.show()
