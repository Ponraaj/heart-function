import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5,5,400)
y = np.linspace(-5,5,400)

# NOTE: Equation to form heart
def get_equation(x,y):
    return ((x**2 + y**2 - 1) ** 3) - x**2 * y**3

# NOTE: Function to Plot the Heart ❤️
def plot_heart():
    X, Y = np.meshgrid(x, y)  # Create a grid of (X, Y) values
    Z = get_equation(X, Y)  # Compute the function values over the grid

    plt.figure(figsize=(6, 6))  # Set figure size
    plt.contour(X, Y, Z, levels=[0], colors='red')  # Plot the heart shape
    plt.xlabel('X Values')
    plt.ylabel('Y Values')
    plt.title('Heart Function')
    plt.show()


def main():
    plot_heart()



if __name__=="__main__":
    main()
