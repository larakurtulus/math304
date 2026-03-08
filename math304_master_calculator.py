import math

# --- HELPER FUNCTION (DRY Principle) ---
def evaluate_math(expr_str, x_val):
    allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
    allowed_names['x'] = x_val
    try:
        return eval(expr_str, {"__builtins__": {}}, allowed_names)
    except OverflowError:
        print("\nERROR: Math overflow! The function values are getting too large.")
        return None
    except Exception as e:
        print(f"\nERROR evaluating the function: {e}")
        return None

# ==========================================
#        1. BISECTION METHOD
# ==========================================
def bisection(f_str, a, b, tol, show_steps, max_iter=100):
    fa = evaluate_math(f_str, a)
    fb = evaluate_math(f_str, b)
    if fa is None or fb is None: return None

    if fa * fb >= 0:
        print("\nERROR: f(a) and f(b) must have opposite signs. The root is not bracketed.")
        return None

    if show_steps: print("\n--- Bisection Iteration Steps ---")
    
    for i in range(1, max_iter + 1):
        mid = (a + b) / 2.0
        f_mid = evaluate_math(f_str, mid)
        if f_mid is None: return None

        if show_steps:
            print(f"Step {i}: Interval [{a:.6f}, {b:.6f}], Midpoint = {mid:.6f} | f(mid) = {f_mid:.6f}")

        if abs(f_mid) < 1e-12 or (b - a) / 2.0 < tol:
            print(f"\nConvergence achieved! (Terminated at step {i})")
            return mid

        if evaluate_math(f_str, a) * f_mid < 0:
            b = mid
        else:
            a = mid
            
    print("\nMaximum iterations reached.")
    return (a + b) / 2.0

# ==========================================
#        2. FIXED-POINT ITERATION
# ==========================================
def fixed_point(g_str, x0, tol, show_steps, max_iter=100):
    if show_steps: print("\n--- Fixed-Point Iteration Steps ---")
    
    x_curr = x0
    for i in range(1, max_iter + 1):
        x_next = evaluate_math(g_str, x_curr)
        if x_next is None: return None

        if show_steps:
            print(f"Step {i}: x_{i} = {x_next:.6f}")

        rel_error = abs((x_next - x_curr) / x_next) if x_next != 0 else abs(x_next - x_curr)

        if rel_error < tol:
            print(f"\nConvergence achieved! (Terminated at step {i})")
            return x_next
        x_curr = x_next
        
    print("\nMaximum iterations reached. The method might be diverging.")
    return x_curr

# ==========================================
#        3. NEWTON-RAPHSON METHOD
# ==========================================
def newton_raphson(f_str, df_str, x0, tol, show_steps, max_iter=100):
    if show_steps: print("\n--- Newton-Raphson Iteration Steps ---")
    
    x_curr = x0
    for i in range(1, max_iter + 1):
        fx = evaluate_math(f_str, x_curr)
        dfx = evaluate_math(df_str, x_curr)
        if fx is None or dfx is None: return None

        if abs(dfx) < 1e-12:
            print(f"\nERROR: Derivative is zero (or very close) at x = {x_curr:.6f}. Division by zero.")
            return None

        x_next = x_curr - (fx / dfx)

        if show_steps:
            print(f"Step {i}: x_{i} = {x_next:.6f} | f(x) = {fx:.6f}")

        rel_error = abs((x_next - x_curr) / x_next) if x_next != 0 else abs(x_next - x_curr)

        if rel_error < tol or abs(fx) < 1e-12:
            print(f"\nConvergence achieved! (Terminated rapidly at step {i})")
            return x_next
        x_curr = x_next
        
    print("\nMaximum iterations reached.")
    return x_curr

# ==========================================
#        4. SECANT METHOD
# ==========================================
def secant(f_str, x0, x1, tol, show_steps, max_iter=100):
    if show_steps: print("\n--- Secant Method Iteration Steps ---")
    
    x_prev, x_curr = x0, x1
    for i in range(1, max_iter + 1):
        f_prev = evaluate_math(f_str, x_prev)
        f_curr = evaluate_math(f_str, x_curr)
        if f_prev is None or f_curr is None: return None

        denominator = f_curr - f_prev
        if abs(denominator) < 1e-12:
            print(f"\nERROR: Denominator is too small. Secant method fails due to division by zero.")
            return None

        x_next = x_curr - f_curr * ((x_curr - x_prev) / denominator)

        if show_steps:
            print(f"Step {i}: x_{i+1} = {x_next:.6f} | f(x) = {evaluate_math(f_str, x_next):.6f}")

        rel_error = abs((x_next - x_curr) / x_next) if x_next != 0 else abs(x_next - x_curr)

        if rel_error < tol or abs(evaluate_math(f_str, x_next)) < 1e-12:
            print(f"\nConvergence achieved! (Terminated at step {i})")
            return x_next
        
        x_prev, x_curr = x_curr, x_next
        
    print("\nMaximum iterations reached.")
    return x_curr

# ==========================================
#        5. REGULA FALSI METHOD
# ==========================================
def regula_falsi(f_str, a, b, tol, show_steps, max_iter=100):
    fa = evaluate_math(f_str, a)
    fb = evaluate_math(f_str, b)
    if fa is None or fb is None: return None
    
    if fa * fb >= 0:
        print("\nERROR: f(a) and f(b) must have opposite signs.")
        return None

    if show_steps: print("\n--- Regula Falsi Iteration Steps ---")
    
    xr_prev = a
    for i in range(1, max_iter + 1):
        fa = evaluate_math(f_str, a)
        fb = evaluate_math(f_str, b)
        if fb - fa == 0: return None

        xr = b - (fb * (b - a)) / (fb - fa)
        fxr = evaluate_math(f_str, xr)

        if show_steps:
            print(f"Step {i}: Interval [{a:.6f}, {b:.6f}], x_r = {xr:.6f} | f(x_r) = {fxr:.6f}")

        rel_error = abs((xr - xr_prev) / xr) if xr != 0 and i > 1 else abs(xr - xr_prev)

        if (i > 1 and rel_error < tol) or abs(fxr) < 1e-12:
            print(f"\nConvergence achieved! (Terminated at step {i})")
            return xr

        xr_prev = xr

        if fa * fxr < 0:
            b = xr
        elif fb * fxr < 0:
            a = xr
        else:
            return xr
            
    print("\nMaximum iterations reached. Warning: Endpoint Stagnation may have occurred.")
    return xr

# ==========================================
#              MAIN MENU
# ==========================================
def main():
    while True:
        print("\n" + "="*55)
        print("    MATH 304 - NUMERICAL ANALYSIS MASTER CALCULATOR")
        print("="*55)
        print("1. Bisection Method")
        print("2. Fixed-Point Iteration")
        print("3. Newton-Raphson Method")
        print("4. Secant Method")
        print("5. Regula Falsi (False Position) Method")
        print("0. EXIT")
        print("-" * 55)
        
        choice = input("Select a method (0-5): ").strip()
        
        if choice == '0':
            print("Exiting program. Goodbye!")
            break
            
        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please enter a number between 0 and 5.")
            continue

        print("\n" + "-" * 55)
        
        # Displaying specific headers and warnings for the chosen method
        if choice == '1':
            print("=== Bisection Method Calculator ===")
            print("A reliable bracketing method.")
        elif choice == '2':
            print("=== Fixed-Point Iteration Calculator ===")
            print("Requires the equation to be in the form x = g(x).")
        elif choice == '3':
            print("=== Newton-Raphson Method Calculator ===")
            print("Requires both the function f(x) and its analytical derivative f'(x).")
        elif choice == '4':
            print("=== Secant Method Calculator ===")
            print("A derivative-free alternative to Newton's method.")
        elif choice == '5':
            print("=== Regula Falsi (False Position) Calculator ===")
            print("A bracketing method that uses linear interpolation.")

        print("Supported math functions: sin(x), cos(x), exp(x), log(x), sqrt(x), etc.")
        print("Important Note: Use '**' for exponentiation (e.g., x**3 - x - 2)")
        print("-" * 55)

        try:
            if choice == '1':
                f_in = input("Enter f(x): ")
                a_in = float(input("Enter lower bound (a): "))
                b_in = float(input("Enter upper bound (b): "))
                tol_in = float(input("Enter tolerance (e.g., 0.001): "))
                steps = input("Show steps? (y/n): ").lower() == 'y'
                root = bisection(f_in, a_in, b_in, tol_in, steps)
                
            elif choice == '2':
                g_in = input("Enter rearranged g(x): ")
                x0_in = float(input("Enter initial guess (x0): "))
                tol_in = float(input("Enter tolerance (e.g., 0.001): "))
                steps = input("Show steps? (y/n): ").lower() == 'y'
                root = fixed_point(g_in, x0_in, tol_in, steps)
                
            elif choice == '3':
                f_in = input("Enter f(x): ")
                df_in = input("Enter derivative f'(x): ")
                x0_in = float(input("Enter initial guess (x0): "))
                tol_in = float(input("Enter tolerance (e.g., 0.001): "))
                steps = input("Show steps? (y/n): ").lower() == 'y'
                root = newton_raphson(f_in, df_in, x0_in, tol_in, steps)
                
            elif choice == '4':
                f_in = input("Enter f(x): ")
                x0_in = float(input("Enter first guess (x0): "))
                x1_in = float(input("Enter second guess (x1): "))
                tol_in = float(input("Enter tolerance (e.g., 0.001): "))
                steps = input("Show steps? (y/n): ").lower() == 'y'
                root = secant(f_in, x0_in, x1_in, tol_in, steps)
                
            elif choice == '5':
                f_in = input("Enter f(x): ")
                a_in = float(input("Enter lower bound (a): "))
                b_in = float(input("Enter upper bound (b): "))
                tol_in = float(input("Enter tolerance (e.g., 0.001): "))
                steps = input("Show steps? (y/n): ").lower() == 'y'
                root = regula_falsi(f_in, a_in, b_in, tol_in, steps)

            if root is not None:
                print(f"\n==> FINAL RESULT: Approximate Root = {root:.6f}")
                
        except ValueError:
            print("\nERROR: Invalid input! Please enter numerical values for bounds, guesses, and tolerance.")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            break
            
        input("\nPress ENTER to return to the Main Menu...")

if __name__ == "__main__":
    main()
