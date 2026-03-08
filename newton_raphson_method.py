import math

def newton_raphson_method(f_str, df_str, x0, tol, show_steps, max_iter=100):
    # Safely evaluate f(x)
    def f(x):
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        allowed_names['x'] = x
        return eval(f_str, {"__builtins__": {}}, allowed_names)

    # Safely evaluate f'(x) (derivative)
    def df(x):
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        allowed_names['x'] = x
        return eval(df_str, {"__builtins__": {}}, allowed_names)

    if show_steps:
        print("\n--- Iteration Steps ---")

    x_curr = x0
    
    # Iteration process: x_(n+1) = x_n - f(x_n) / f'(x_n)
    for i in range(1, max_iter + 1):
        try:
            fx = f(x_curr)
            dfx = df(x_curr)
        except OverflowError:
            print("\nERROR: Math overflow! The function values are getting too large.")
            return None

        # Failure Case Check: If derivative is close to zero (Division by zero)
        if abs(dfx) < 1e-12:
            print(f"\nERROR: Derivative is zero (or very close) at x = {x_curr:.6f}.")
            print("Newton's method fails because of division by zero. Try a different initial guess (x0).")
            return None

        # Calculate next x using Newton-Raphson formula
        x_next = x_curr - (fx / dfx)

        if show_steps:
            print(f"Step {i}: x_{i} = {x_next:.6f} | f(x) = {fx:.6f}")

        # Stopping Criteria 1: Relative Displacement Error (from practical implementation notes)
        if x_next != 0:
            rel_error = abs((x_next - x_curr) / x_next)
        else:
            rel_error = abs(x_next - x_curr)

        # Stopping Criteria 2: Residual check |f(x)| < tol
        if rel_error < tol or abs(fx) < 1e-12:
            print(f"\nConvergence achieved! (Terminated rapidly at step {i})")
            return x_next
        
        # Prepare for the next iteration
        x_curr = x_next

    print("\nMaximum iterations reached. The method might be diverging.")
    print("Check if the initial guess is too far from the root or if the function has multiple roots.")
    return x_curr

# --- USER INPUT SECTION ---
print("=== Newton-Raphson Method Calculator ===")
print("You need to enter both the function f(x) and its analytical derivative f'(x).")
print("Supported math functions: sin(x), cos(x), exp(x), log(x), sqrt(x), etc.")
print("Important Note: Use '**' for exponentiation (e.g., x**3 - x - 2)")
print("-" * 50)

# Getting values from the user safely
f_input = input("Enter the equation f(x): ")
df_input = input("Enter the derivative equation f'(x): ")
x0_input = float(input("Enter the initial guess (x0): "))
tol_input = float(input("Enter the target error tolerance (e.g., 0.001): "))

step_choice = input("Do you want to see the step-by-step iteration results? (y/n): ").strip().lower()
show_steps = step_choice == 'y'

# Running the function
root = newton_raphson_method(f_input, df_input, x0_input, tol_input, show_steps)

if root is not None:
    print(f"==> Calculated Approximate Root: {root:.6f}")
