import os
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from werkzeug.utils import secure_filename

from core.auth import register_user, authenticate_user
from core.image_processing import preprocess_image_for_ocr, preprocess_for_trocr
from core.ocr_engine import ocr_engine
from core.math_solver import solve_expression
from core.plotter import generate_graph_base64
from core.db_models import log_solve_history, get_user_dashboard_stats, get_user_full_history

app = Flask(__name__)
app.secret_key = 'super_secret_dev_key_that_does_not_change_on_reload'

UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure user is logged in
def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def landing():
    # If user is logged in, they can still see landing, or maybe we redirect?
    # Let's just show landing.
    return render_template('landing.html')

@app.route('/workspace')
@login_required
def workspace():
    import torch
    cuda_available = torch.cuda.is_available()
    return render_template('workspace.html', cuda_available=cuda_available)

@app.route('/dashboard')
@login_required
def dashboard():
    stats = get_user_dashboard_stats(session['username'])
    return render_template('dashboard.html', stats=stats)

@app.route('/history')
@login_required
def history():
    history = get_user_full_history(session['username'])
    return render_template('history.html', history=history)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate_user(username, password):
            session['username'] = username
            return redirect(url_for('workspace'))
        else:
            return render_template('auth.html', error="Invalid credentials", type="login")
    return render_template('auth.html', type="login")

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        success, msg = register_user(username, password)
        if success:
            session['username'] = username
            return redirect(url_for('workspace'))
        else:
            return render_template('auth.html', error=msg, type="register")
    return render_template('auth.html', type="register")

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/api/extract', methods=['POST'])
@login_required
def extract_api():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400
        
    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
        
    model_choice = request.form.get('model', 'easyocr')
    hardware_choice = request.form.get('hardware', 'gpu')
    
    # Configure ocr_engine device dynamically before loading model or running inference
    ocr_engine.set_device(hardware_choice)
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    try:
        if model_choice == 'trocr':
            processed_img = preprocess_for_trocr(filepath)
            extracted_text = ocr_engine.process_with_trocr(processed_img)
        else:
            processed_img = preprocess_image_for_ocr(filepath)
            temp_path = os.path.join(app.config['UPLOAD_FOLDER'], 'temp_' + filename)
            import cv2
            cv2.imwrite(temp_path, processed_img)
            extracted_text = ocr_engine.process_with_easyocr(temp_path)
            
        return jsonify({"success": True, "extracted_text": extracted_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/solve', methods=['POST'])
@login_required
def solve_api():
    extracted_text = request.form.get('expression', '')
    if not extracted_text:
        return jsonify({"error": "No expression provided"}), 400
        
    try:
        solution_data = solve_expression(extracted_text)
        
        # Log to DB
        if not solution_data['success']:
            log_solve_history(session['username'], extracted_text, extracted_text, False)
            return jsonify({
                "success": True,
                "parsed_latex": extracted_text,
                "steps": [{"title": "Error", "content": f"Could not solve expression algebraically. Error: {solution_data.get('error', 'Unknown error')}", "is_latex": False}],
                "final_result": "N/A",
                "graph_base64": None
            })
            
        graph_base64 = None
        if solution_data.get('can_plot') and solution_data.get('plot_expr') is not None:
            graph_base64 = generate_graph_base64(solution_data['plot_expr'], solution_data['plot_var'])
            
        parsed_latex = solution_data.get('latex') or extracted_text
        if solution_data.get('solution') == 'Identity / Unsolvable':
             log_solve_history(session['username'], extracted_text, parsed_latex, False, complexity='NP-Hard')
        else:
             log_solve_history(session['username'], extracted_text, parsed_latex, True)
             
        return jsonify({
            "success": True,
            "parsed_latex": solution_data.get('latex') or extracted_text,
            "steps": solution_data['steps'],
            "final_result": solution_data['solution'],
            "graph_base64": graph_base64
        })

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
