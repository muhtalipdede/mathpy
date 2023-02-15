def fixed_point_iteration(g, x0, tol=1e-6, max_iter=100):
    """
    Fixed point iteration method to find the roots of a function g.

    Args:
    g (function): Iteration function.
    x0 (float): Initial guess.
    tol (float): Tolerance for stopping criterion.
    max_iter (int): Maximum number of iterations.

    Returns:
    float: Root of the function g.
    """
    x = x0
    for i in range(max_iter):
        x1 = g(x)
        if abs(x1 - x) < tol:
            return x1
        x = x1
    raise Exception(f"Fixed point iteration did not converge after {max_iter} iterations")

def g(x):
    return x - (x**2 - x - 1) / (2*x - 1)

root = fixed_point_iteration(g, x0=2)
print(f"The root of the function is approximately {root:.6f}")
