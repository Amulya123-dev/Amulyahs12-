import traceback
from core.ocr_engine import ocr_engine
from core.math_solver import solve_expression
from PIL import Image

# Create a dummy image
img = Image.new('RGB', (100, 30), color = (255, 255, 255))
# This is just to pass to TrOCR so it doesn't crash on preprocessing

try:
    print("Testing TrOCR extraction...")
    extracted_text = ocr_engine.process_with_trocr(img)
    print(f"Extracted: {extracted_text}")
    
    print("Testing solver...")
    result = solve_expression(extracted_text, is_latex=True)
    print(f"Result: {result}")
except Exception as e:
    traceback.print_exc()
