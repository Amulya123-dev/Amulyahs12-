import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from core.plotter import generate_graph_base64
import sympy as sp

x = sp.Symbol('x')
expr = x**2
print("Testing plotter with x**2...")
res = generate_graph_base64(expr, [x])
if res:
    print("Success: Generated base64 string")
else:
    print("Failed")
