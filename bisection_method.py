import math

def bisection_method(f_str, a, b, tol, show_steps, max_iter=1000):
    # Defining the function safely with all math module capabilities
    def f(x):
        # We pass the math module's dictionary so users can type sin(x), exp(x), etc. directly
        allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
        allowed_names['x'] = x
        
        # Security fix: Using {} instead of None to allow proper error handling
        return eval(f_str, {"__builtins__": {}}, allowed_names)
    
    # Step 1: Intermediate Value Theorem check
    if f(a) * f(b) >= 0:
        print("\nERROR: f(a) and f(b) must have opposite signs. The root may not be in this interval or the interval is incorrect.")
        return None

    if show_steps:
        print("\n--- Iteration Steps ---")
        
    # Iteration process
    for i in range(1, max_iter + 1):
        # Step 2: Calculate the midpoint
        c = (a + b) / 2.0
        
        if show_steps:
            print(f"Step {i}: Interval [{a:.4f}, {b:.4f}], Midpoint (c) = {c:.4f}")
        
        # Step 3: Check stopping criteria
        if abs(b - a) < tol or f(c) == 0:
            print(f"\nRoot found successfully! (Terminated at step {i})")
            return c
        
        # Step 4: Determine the new interval
        if f(a) * f(c) < 0:
            b = c  # The root is in the left half
        else:
            a = c  # The root is in the right half
            
    print("\nMaximum iterations reached without achieving the target tolerance.")
    return (a + b) / 2.0

# --- USER INPUT SECTION ---
print("=== Bisection Method Calculator ===")
print("Please enter the function in terms of 'x'.")
print("Supported math functions: sin(x), cos(x), tan(x), exp(x), log(x), sqrt(x), etc.")
print("Important Note: Use '**' for exponentiation instead of '^' (e.g., x**3 - exp(x) - 2)")
print("-" * 50)

# Getting values from the user safely
f_input = input("Enter the equation f(x): ")
a_input = float(input("Enter the lower bound of the interval (a): "))
b_input = float(input("Enter the upper bound of the interval (b): "))
tol_input = float(input("Enter the target error tolerance (e.g., 0.001): "))

# Asking if the user wants to see the iteration steps
step_choice = input("Do you want to see the step-by-step iteration results? (y/n): ").strip().lower()
show_steps = step_choice == 'y'

# Running the function
root = bisection_method(f_input, a_input, b_input, tol_input, show_steps)

if root is not None:
    print(f"==> Calculated Approximate Root: {root:.5f}")
