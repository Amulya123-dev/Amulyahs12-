import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from core.math_solver import solve_expression

print("--- Testing Indefinite Integral ---")
res1 = solve_expression(r"\int x^2 dx")
print("Success:", res1['success'])
print("LaTeX output:", res1['latex'])
print("Steps:")
for s in res1['steps']:
    print(f"  [{s['title']}] -> {s['content']}")

print("\n--- Testing Calculus Equation (Derivative Identity) ---")
res2 = solve_expression(r"\frac{d}{dx}(x^2) = 2x")
print("Success:", res2['success'])
print("LaTeX output:", res2['latex'])
print("Steps:")
for s in res2['steps']:
    print(f"  [{s['title']}] -> {s['content']}")

print("\n--- Testing Trigonometric Equation ---")
res3 = solve_expression(r"\sin(x) = \frac{1}{2}")
print("Success:", res3['success'])
print("LaTeX output:", res3['latex'])
print("Steps:")
for s in res3['steps']:
    print(f"  [{s['title']}] -> {s['content']}")
