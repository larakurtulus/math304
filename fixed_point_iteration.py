import math

def fixed_point_iteration(g_str, x0, tol, show_steps, max_iter=1000):
    # Defining the function safely with all math module capabilities
    def g(x):
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        allowed_names['x'] = x
        return eval(g_str, {"__builtins__": {}}, allowed_names)

    if show_steps:
        print("\n--- Iteration Steps ---")

    x_prev = x0
    
    # Iteration process: x_(n+1) = g(x_n)
    for i in range(1, max_iter + 1):
        try:
            x_curr = g(x_prev)
        except OverflowError:
            # Divergence check: If values get too large (e.g., |g'(x)| > 1)
            print("\nERROR: Math overflow! The method is diverging rapidly.")
            print("Please rearrange f(x)=0 to a different g(x) where |g'(x)| < 1.")
            return None

        if show_steps:
            print(f"Step {i}: x_{i} = {x_curr:.6f}")

        # Stopping Criterion: Relative Error |(x_n - x_{n-1}) / x_n| < tol
        if x_curr != 0:
            rel_error = abs((x_curr - x_prev) / x_curr)
        else:
            rel_error = abs(x_curr - x_prev) # Fallback if x_curr is exactly zero

        if rel_error < tol:
            print(f"\nConvergence achieved! (Terminated at step {i} with relative error: {rel_error:.6f})")
            return x_curr
        
        # Prepare for the next step
        x_prev = x_curr

    print("\nMaximum iterations reached without achieving the target tolerance.")
    print("The method might be diverging. Check if the contraction condition |g'(x)| < 1 holds.")
    return x_curr

# --- USER INPUT SECTION ---
print("=== Fixed-Point Iteration Calculator ===")
print("First, rewrite your equation f(x) = 0 in the form x = g(x).")
print("Supported math functions: sin(x), cos(x), exp(x), log(x), sqrt(x), etc.")
print("Important Note: Use '**' for exponentiation (e.g., (x+1)**(1/3))")
print("-" * 50)

# Getting values from the user safely
g_input = input("Enter the rearranged equation g(x): ")
x0_input = float(input("Enter the initial guess (x0): "))
tol_input = float(input("Enter the target relative error tolerance (e.g., 0.001): "))

step_choice = input("Do you want to see the step-by-step iteration results? (y/n): ").strip().lower()
show_steps = step_choice == 'y'

# Running the function
root = fixed_point_iteration(g_input, x0_input, tol_input, show_steps)

if root is not None:
    print(f"==> Calculated Approximate Fixed-Point: {root:.6f}")
