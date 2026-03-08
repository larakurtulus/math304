import math

def secant_method(f_str, x0, x1, tol, show_steps, max_iter=100):
    # Safely evaluate f(x)
    def f(x):
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        allowed_names['x'] = x
        return eval(f_str, {"__builtins__": {}}, allowed_names)

    if show_steps:
        print("\n--- Iteration Steps ---")

    # Initializing points
    x_prev = x0
    x_curr = x1
    
    # Secant iteration process
    for i in range(1, max_iter + 1):
        try:
            f_prev = f(x_prev)
            f_curr = f(x_curr)
        except OverflowError:
            print("\nERROR: Math overflow! The function values are getting too large.")
            return None

        # Limitation Check: If f(x_n) - f(x_{n-1}) is very small (Division by zero)
        denominator = f_curr - f_prev
        if abs(denominator) < 1e-12:
            print(f"\nERROR: Denominator is too small (f(x_n) ≈ f(x_n-1)) at step {i}.")
            print("Secant method fails due to division by zero. Try different initial guesses.")
            return None

        # Calculate next x using Secant formula
        x_next = x_curr - f_curr * ((x_curr - x_prev) / denominator)

        if show_steps:
            print(f"Step {i}: x_{i+1} = {x_next:.6f} | f(x) = {f(x_next):.6f}")

        # Stopping Criteria 1: Relative Change (from stopping criteria notes)
        if x_next != 0:
            rel_error = abs((x_next - x_curr) / x_next)
        else:
            rel_error = abs(x_next - x_curr)

        # Stopping Criteria 2: Residual check
        if rel_error < tol or abs(f(x_next)) < 1e-12:
            print(f"\nConvergence achieved! (Terminated at step {i} with relative error: {rel_error:.6f})")
            return x_next
        
        # Prepare for the next iteration: Shift values
        x_prev = x_curr
        x_curr = x_next

    print("\nMaximum iterations reached. The method might be diverging.")
    print("Secant method does not guarantee bracketing. Try initial guesses closer to the root.")
    return x_curr

# --- USER INPUT SECTION ---
print("=== Secant Method Calculator ===")
print("A derivative-free alternative to Newton's method.")
print("Supported math functions: sin(x), cos(x), exp(x), log(x), sqrt(x), etc.")
print("Important Note: Use '**' for exponentiation (e.g., exp(x) - 3)")
print("-" * 50)

# Getting values from the user safely
f_input = input("Enter the equation f(x): ")
x0_input = float(input("Enter the first initial guess (x0): "))
x1_input = float(input("Enter the second initial guess (x1): "))
tol_input = float(input("Enter the target relative error tolerance (e.g., 0.001): "))

step_choice = input("Do you want to see the step-by-step iteration results? (y/n): ").strip().lower()
show_steps = step_choice == 'y'

# Running the function
root = secant_method(f_input, x0_input, x1_input, tol_input, show_steps)

if root is not None:
    print(f"==> Calculated Approximate Root: {root:.6f}")
