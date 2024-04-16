import math

def bisection_method(f, a, b, tolerance):
    iterations = 0
    while abs(b - a) > tolerance:
        c = (a + b) / 2
        if f(c) == 0:
            return c, iterations
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterations += 1
    return (a + b) / 2, iterations

def secant_method(f, x0, x1, tolerance):
    iterations = 0
    while abs(x1 - x0) > tolerance:
        x2 = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
        iterations += 1
    return x1, iterations

def newton_raphson_method(f, f_prime, x0, tolerance):
    iterations = 0
    while abs(f(x0)) > tolerance:
        x0 = x0 - f(x0) / f_prime(x0)
        iterations += 1
    return x0, iterations

# Define the equation and its derivative
def f(x):
    return x**2 - 4

def f_prime(x):
    return 2 * x

# Set the initial values and tolerance
a = 0
b = 5
x0 = 2
x1 = 3
tolerance = 1e-6

# Apply the methods
bisection_root, bisection_iterations = bisection_method(f, a, b, tolerance)
secant_root, secant_iterations = secant_method(f, x0, x1, tolerance)
newton_raphson_root, newton_raphson_iterations = newton_raphson_method(f, f_prime, x0, tolerance)

# Print the results
print("Bisection Method:")
print("Root:", bisection_root)
print("Iterations:", bisection_iterations)

print("\nSecant Method:")
print("Root:", secant_root)
print("Iterations:", secant_iterations)

print("\nNewton-Raphson Method:")
print("Root:", newton_raphson_root)
print("Iterations:", newton_raphson_iterations)
