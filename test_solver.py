import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from core.math_solver import solve_expression
from core.plotter import generate_graph_base64
import json

res = solve_expression("x^{2}+2x-10=0")
for step in res['steps']:
    print(step)
print("Graph can plot:", res['can_plot'])
if res['can_plot']:
    try:
        generate_graph_base64(res['plot_expr'], res['plot_var'])
        print("Graph generated OK!")
    except Exception as e:
        print("Graph failed:", e)
