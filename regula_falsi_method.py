import math

def regula_falsi_method(f_str, a, b, tol, show_steps, max_iter=100):
    # Safely evaluate f(x)
    def f(x):
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        allowed_names['x'] = x
        return eval(f_str, {"__builtins__": {}}, allowed_names)

    # Step 1: Verify that the root is bracketed
    fa = f(a)
    fb = f(b)
    if fa * fb >= 0:
        print("\nERROR: f(a) and f(b) must have opposite signs. The root is not bracketed.")
        return None

    if show_steps:
        print("\n--- Iteration Steps ---")

    xr_prev = a  # Variable to store previous x_r for relative error calculation
    
    # Regula Falsi iteration process
    for i in range(1, max_iter + 1):
        fa = f(a)
        fb = f(b)

        # Prevent division by zero just in case f(a) exactly equals f(b)
        if fb - fa == 0:
            print("\nERROR: Division by zero. f(a) and f(b) are equal.")
            return None

        # Step 2: Compute x_r using linear interpolation formula
        xr = b - (fb * (b - a)) / (fb - fa)
        fxr = f(xr)

        if show_steps:
            print(f"Step {i}: Interval [{a:.6f}, {b:.6f}], x_r = {xr:.6f} | f(x_r) = {fxr:.6f}")

        # Step 6 & 7: Stopping Criteria (Relative error and Residual)
        rel_error = 0
        if i > 1:
            if xr != 0:
                rel_error = abs((xr - xr_prev) / xr)
            else:
                rel_error = abs(xr - xr_prev)

            if rel_error < tol or abs(fxr) < 1e-12:
                print(f"\nConvergence achieved! (Terminated at step {i})")
                return xr
        elif abs(fxr) < 1e-12: # If the very first guess is exactly the root
            print(f"\nExact root found at first step!")
            return xr

        xr_prev = xr

        # Step 4 & 5: Update the interval bracket
        if fa * fxr < 0:
            b = xr  # Root is between a and x_r
        elif fb * fxr < 0:
            a = xr  # Root is between x_r and b
        else:
            # fxr is exactly 0
            print(f"\nExact root found! (Terminated at step {i})")
            return xr

    print("\nMaximum iterations reached without achieving the target tolerance.")
    print("Warning: The method might be suffering from 'Endpoint Stagnation' (one bound is stuck).")
    return xr

# --- USER INPUT SECTION ---
print("=== Regula Falsi (False Position) Calculator ===")
print("A bracketing method that uses linear interpolation for faster convergence than Bisection.")
print("Supported math functions: sin(x), cos(x), exp(x), log(x), sqrt(x), etc.")
print("Important Note: Use '**' for exponentiation (e.g., x**2 - 4)")
print("-" * 50)

# Getting values from the user safely
f_input = input("Enter the equation f(x): ")
a_input = float(input("Enter the lower bound of the interval (a): "))
b_input = float(input("Enter the upper bound of the interval (b): "))
tol_input = float(input("Enter the target relative error tolerance (e.g., 0.001): "))

step_choice = input("Do you want to see the step-by-step iteration results? (y/n): ").strip().lower()
show_steps = step_choice == 'y'

# Running the function
root = regula_falsi_method(f_input, a_input, b_input, tol_input, show_steps)

if root is not None:
    print(f"==> Calculated Approximate Root: {root:.6f}")
