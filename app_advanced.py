"""
ADVANCED SLEEP DISORDER DETECTION SYSTEM
A Professional ML-Based Healthcare Application
Author: Software Engineering Specialist
Version: 2.0 (Advanced)
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for, send_file
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import sqlite3
import joblib
import pandas as pd
import numpy as np
import json
import os
from functools import wraps
import io
import csv

# ============================================================================
# FLASK APPLICATION INITIALIZATION
# ============================================================================

app = Flask(__name__)
app.secret_key = 'sleep_disorder_detection_2024_secure_key_change_in_production'
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE'] = False  # Set to True in production with HTTPS
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=24)

# ============================================================================
# DATABASE INITIALIZATION
# ============================================================================

def init_db():
    """Initialize SQLite database with required tables"""
    conn = sqlite3.connect('database/users.db')
    c = conn.cursor()
    
    # Users table
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    
    # Assessment results table
    c.execute('''CREATE TABLE IF NOT EXISTS assessments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        age INTEGER,
        gender TEXT,
        bedtime INTEGER,
        wakeup_time INTEGER,
        sleep_duration REAL,
        rem_sleep REAL,
        deep_sleep REAL,
        light_sleep REAL,
        awakenings REAL,
        caffeine REAL,
        alcohol REAL,
        smoking TEXT,
        exercise_frequency REAL,
        sleep_efficiency REAL,
        disorder_type TEXT,
        risk_score REAL,
        risk_level TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )''')
    
    conn.commit()
    conn.close()

# Create database directory
if not os.path.exists('database'):
    os.makedirs('database')
init_db()

# ============================================================================
# MACHINE LEARNING MODEL & UTILITIES
# ============================================================================

# Load the pre-trained Random Forest model
try:
    model = joblib.load('random_forest_model.pkl')
except FileNotFoundError:
    print("⚠️ Warning: random_forest_model.pkl not found. Using dummy model for demo.")
    model = None

class SleepDisorderAnalyzer:
    """Advanced Sleep Disorder Detection & Analysis Engine"""
    
    @staticmethod
    def calculate_risk_score(data):
        """
        Calculate comprehensive risk score based on multiple factors
        Returns: (risk_score: 0-100, risk_level: 'Low'/'Medium'/'High')
        """
        risk_factors = {}
        total_risk = 0
        
        # Sleep Efficiency Impact (30% weight)
        efficiency = float(data['sleep_efficiency'])
        if efficiency < 0.55:
            risk_factors['efficiency'] = 30
        elif efficiency < 0.70:
            risk_factors['efficiency'] = 20
        elif efficiency < 0.85:
            risk_factors['efficiency'] = 10
        else:
            risk_factors['efficiency'] = 0
            
        
        # Awakenings Impact (20% weight)
        awakenings = float(data['awakenings'])
        if awakenings > 4:
            risk_factors['awakenings'] = 20
        elif awakenings > 2:
            risk_factors['awakenings'] = 12
        else:
            risk_factors['awakenings'] = 0
        
        # Deep Sleep Impact (25% weight)
        deep_sleep = float(data['deep_sleep'])
        if deep_sleep < 30:
            risk_factors['deep_sleep'] = 25
        elif deep_sleep < 45:
            risk_factors['deep_sleep'] = 15
        else:
            risk_factors['deep_sleep'] = 0
        
        # Lifestyle Factors (15% weight)
        caffeine = float(data['caffeine']) / 10 * 7
        smoking = 8 if data['smoking'] == 'Yes' else 0
        exercise = max(0, 5 - float(data['exercise']))
        
        risk_factors['lifestyle'] = min(15, caffeine + smoking + exercise)
        
        # Alcohol Impact (10% weight)
        alcohol = float(data['alcohol']) / 10 * 10
        risk_factors['alcohol'] = min(10, alcohol)
        
        # Calculate total risk
        total_risk = sum(risk_factors.values())
        
        # Determine risk level
        if total_risk < 30:
            risk_level = "🟢 LOW RISK"
            recommendation = "Your sleep patterns are healthy. Maintain current habits!"
        elif total_risk < 60:
            risk_level = "🟡 MEDIUM RISK"
            recommendation = "Some areas need improvement. See suggestions below."
        else:
            risk_level = "🔴 HIGH RISK"
            recommendation = "Significant concerns detected. Consult a healthcare provider."
        
        return {
            'risk_score': total_risk,
            'risk_level': risk_level,
            'recommendation': recommendation,
            'risk_factors': risk_factors
        }
    
    @staticmethod
    def classify_disorder(data, prediction=None):   
        """
        Classify sleep disorder type based on features
        """
 
        efficiency = float(data['sleep_efficiency'])
        awakenings = float(data['awakenings'])
        deep_sleep = float(data['deep_sleep'])
        rem_sleep = float(data['rem_sleep'])
        
        # Decision logic for disorder classification
        if awakenings > 4 and deep_sleep < 35:
            return "Sleep Apnea"
        elif efficiency < 0.55 and awakenings >2:
            return "Insomnia"
        elif rem_sleep < 15 and efficiency < 0.65:
            return "REM Sleep Disorder"
        elif deep_sleep < 20 and rem_sleep > 35:
            return "Narcolepsy"
        elif efficiency > 0.85 and awakenings <= 1:
            return "Healthy Sleep"
        else:
            return "Mixed Sleep Disorder"
    
    @staticmethod
    def interpret_efficiency(efficiency):
        """Interpret sleep efficiency level"""
        efficiency = float(efficiency)
        if efficiency >= 0.85:
            return "Excellent ⭐⭐⭐⭐⭐"
        elif efficiency >= 0.70:
            return "Good ⭐⭐⭐⭐"
        elif efficiency >= 0.55:
            return "Fair ⭐⭐⭐"
        else:
            return "Poor ⭐⭐"
    
    @staticmethod
    def generate_health_suggestions(data, disorder, risk_level):
        """Generate personalized health suggestions"""
        suggestions = []
        
        # ✅ FIX: Convert ALL string inputs to float BEFORE using them
        
        # Get efficiency-based suggestions
        efficiency = float(data['sleep_efficiency'])
        if efficiency < 0.70:
            suggestions.append({
                'category': '😴 Sleep Efficiency',
                'suggestion': 'Improve sleep environment: keep room dark, cool (65-68°F), and quiet',
                'priority': 'HIGH'
            })
        
        # Awakenings-based suggestions
        awakenings = float(data['awakenings'])
        if awakenings > 3:
            suggestions.append({
                'category': '⏰ Frequent Awakenings',
                'suggestion': 'Reduce caffeine intake (avoid after 2 PM) and maintain consistent sleep schedule',
                'priority': 'HIGH'
            })
        
        # Deep sleep suggestions
        deep_sleep = float(data['deep_sleep'])
        if deep_sleep < 40:
            suggestions.append({
                'category': '💪 Deep Sleep',
                'suggestion': 'Increase exercise frequency to 3-5 times per week (avoid before bedtime)',
                'priority': 'MEDIUM'
            })
        
        # REM sleep suggestions
        rem_sleep = float(data['rem_sleep'])
        if rem_sleep < 20:
            suggestions.append({
                'category': '🧠 REM Sleep',
                'suggestion': 'Practice stress management: meditation, yoga, or breathing exercises',
                'priority': 'MEDIUM'
            })
        
        # ✅ CONVERT TO FLOAT - This is where the bug was!
        # Lifestyle suggestions
        caffeine = float(data['caffeine'])  # ← CONVERT STRING TO FLOAT
        if caffeine > 50:
            suggestions.append({
                'category': '☕ Caffeine',
                'suggestion': 'Reduce caffeine consumption. Switch to decaf after 12 PM',
                'priority': 'HIGH'
            })
        
        alcohol = float(data['alcohol'])  # ← CONVERT STRING TO FLOAT
        if alcohol > 3:
            suggestions.append({
                'category': '🍷 Alcohol',
                'suggestion': 'Limit alcohol intake - it disrupts sleep architecture',
                'priority': 'HIGH'
            })
        
        if data['smoking'] == 'Yes':
            suggestions.append({
                'category': '🚭 Smoking',
                'suggestion': 'Consider smoking cessation - nicotine is a stimulant',
                'priority': 'CRITICAL'
            })
        
        exercise = float(data['exercise'])  # ← CONVERT STRING TO FLOAT
        if exercise < 2:
            suggestions.append({
                'category': '🏃 Exercise',
                'suggestion': 'Increase physical activity to at least 30 mins, 3x per week',
                'priority': 'MEDIUM'
            })
        
        # Disorder-specific suggestions
        if disorder == "Sleep Apnea":
            suggestions.append({
                'category': '🏥 Sleep Apnea',
                'suggestion': 'Consult sleep specialist for sleep study and possible CPAP therapy',
                'priority': 'CRITICAL'
            })
        
        elif disorder == "Insomnia":
            suggestions.append({
                'category': '🏥 Insomnia',
                'suggestion': 'Try CBT-I (Cognitive Behavioral Therapy for Insomnia) or consult physician',
                'priority': 'HIGH'
            })
        
        elif disorder == "Narcolepsy":
            suggestions.append({
                'category': '🏥 Narcolepsy',
                'suggestion': 'Seek immediate specialist evaluation and neurological assessment',
                'priority': 'CRITICAL'
            })
        
        return suggestions

# ============================================================================
# AUTHENTICATION ROUTES
# ============================================================================

def login_required(f):
    """Decorator for routes requiring authentication"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/register', methods=['GET', 'POST'])
def register():
    """User registration route"""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Validation
        if not username or not email or not password:
            return jsonify({'error': 'All fields required'}), 400
        if password != confirm_password:
            return jsonify({'error': 'Passwords do not match'}), 400
        if len(password) < 6:
            return jsonify({'error': 'Password must be at least 6 characters'}), 400
        
        try:
            conn = sqlite3.connect('database/users.db')
            c = conn.cursor()
            hashed_password = generate_password_hash(password)
            c.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                     (username, email, hashed_password))
            conn.commit()
            conn.close()
            return jsonify({'success': True, 'message': 'Registration successful!'}), 201
        except sqlite3.IntegrityError:
            return jsonify({'error': 'Username or email already exists'}), 409
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """User login route"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        conn = sqlite3.connect('database/users.db')
        c = conn.cursor()
        c.execute('SELECT id, password FROM users WHERE username = ?', (username,))
        user = c.fetchone()
        conn.close()
        
        if user and check_password_hash(user[1], password):
            session['user_id'] = user[0]
            session['username'] = username
            return jsonify({'success': True, 'redirect': '/home'}), 200
        else:
            return jsonify({'error': 'Invalid credentials'}), 401
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """User logout route"""
    session.clear()
    return redirect(url_for('login'))

# ============================================================================
# MAIN ROUTES
# ============================================================================

@app.route('/')
def index():
    """Landing page"""
    if 'user_id' in session:
        return redirect(url_for('home'))
    return redirect(url_for('login'))

@app.route('/home')
@login_required
def home():
    """Home/Dashboard page"""
    return render_template('home.html', username=session.get('username'))

@app.route('/sleep-disorders')
@login_required
def sleep_disorders():
    return render_template('sleep_disorders.html')

@app.route('/assessment', methods=['GET', 'POST'])
@login_required
def assessment():
    """Sleep assessment form"""
    if request.method == 'POST':
        return handle_assessment()
    return render_template('assessment.html')

@app.route('/api/assess', methods=['POST'])
@login_required
def handle_assessment():
    """Handle sleep assessment and prediction"""
    data = request.get_json()
    
    # Data preparation
    input_features = {
        'Age': [int(data['age'])],
        'Gender': [1 if data['gender'] == 'Female' else 0],
        'Bedtime': [int(data['bedtime'])],
        'Wakeup time': [int(data['wakeup_time'])],
        'Sleep duration': [float(data['sleep_duration'])],
        'REM sleep percentage': [float(data['rem_sleep'])],
        'Deep sleep percentage': [float(data['deep_sleep'])],
        'Light sleep percentage': [float(data['light_sleep'])],
        'Awakenings': [float(data['awakenings'])],
        'Caffeine consumption': [float(data['caffeine'])],
        'Alcohol consumption': [float(data['alcohol'])],
        'Smoking status': [1 if data['smoking'] == 'Yes' else 0],
        'Exercise frequency': [float(data['exercise'])]
    }
    
    input_df = pd.DataFrame(input_features)
    
    # ML Prediction
    if model:
        sleep_efficiency = model.predict(input_df)[0]
    else:
        # Demo mode: generate realistic prediction
        sleep_efficiency = np.random.uniform(0.50, 0.95)
    
    # Analysis
    analysis_data = {
        'sleep_efficiency': sleep_efficiency,
        'awakenings': data['awakenings'],
        'deep_sleep': data['deep_sleep'],
        'rem_sleep': data['rem_sleep'],
        'caffeine': data['caffeine'],
        'alcohol': data['alcohol'],
        'smoking': data['smoking'],
        'exercise': data['exercise']
    }
    
    risk_assessment = SleepDisorderAnalyzer.calculate_risk_score(analysis_data)
    disorder = SleepDisorderAnalyzer.classify_disorder(analysis_data, sleep_efficiency)
    efficiency_level = SleepDisorderAnalyzer.interpret_efficiency(sleep_efficiency)
    suggestions = SleepDisorderAnalyzer.generate_health_suggestions(
        analysis_data, disorder, risk_assessment['risk_level']
    )
    
    # Save to database
    conn = sqlite3.connect('database/users.db')
    c = conn.cursor()
    c.execute('''INSERT INTO assessments 
                (user_id, age, gender, bedtime, wakeup_time, sleep_duration, 
                 rem_sleep, deep_sleep, light_sleep, awakenings, caffeine, 
                 alcohol, smoking, exercise_frequency, sleep_efficiency, 
                 disorder_type, risk_score, risk_level)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
             (session['user_id'], int(data['age']), data['gender'], 
              int(data['bedtime']), int(data['wakeup_time']), float(data['sleep_duration']),
              float(data['rem_sleep']), float(data['deep_sleep']), 
              float(data['light_sleep']), float(data['awakenings']),
              float(data['caffeine']), float(data['alcohol']), 
              data['smoking'], float(data['exercise']),
              sleep_efficiency, disorder, risk_assessment['risk_score'], 
              risk_assessment['risk_level']))
    conn.commit()
    conn.close()
    

    # ✅ Store assessment result in session
    session['assessment_result'] = {
        'sleep_efficiency': round(sleep_efficiency, 4),
        'efficiency_level': efficiency_level,
        'disorder': disorder,
        'risk_score': round(risk_assessment['risk_score'], 2),
        'risk_level': risk_assessment['risk_level'],
        'recommendation': risk_assessment['recommendation'],
        'suggestions': suggestions,
        'sleep_duration': f"{float(data['sleep_duration']):.1f} hours",
        'awakenings': f"{int(float(data['awakenings']))} times",
        'chart_data': {
            'sleep_stages': {
                'REM': float(data['rem_sleep']),
                'Deep': float(data['deep_sleep']),
                'Light': float(data['light_sleep'])
            }
        }
    }
    
    # ✅ Return success with redirect URL
    return jsonify({
        'success': True,
        'redirect': '/results'
    })

@app.route('/results')
@login_required
def results():
    """Display assessment results page"""
    if 'assessment_result' not in session:
        return redirect(url_for('assessment'))
    
    result = session.get('assessment_result', {})
    
    # Ensure all required fields exist
    result_with_defaults = {
        'sleep_efficiency': result.get('sleep_efficiency', 0),
        'efficiency_level': result.get('efficiency_level', 'Unknown'),
        'disorder': result.get('disorder', 'Unclassified'),
        'risk_score': result.get('risk_score', 0),
        'risk_level': result.get('risk_level', 'Unknown'),
        'recommendation': result.get('recommendation', 'No recommendation available'),
        'suggestions': result.get('suggestions', []),
        'chart_data': result.get('chart_data', {}),
        'sleep_duration': result.get('sleep_duration', '--'),
        'awakenings': result.get('awakenings', '--')
    }
    
    # Store back in session so it persists
    session['assessment_result'] = result_with_defaults
    
    return render_template('results.html', result=result_with_defaults)

@app.route('/api/assessment-history')
@login_required
def get_assessment_history():
    """Return assessment history as JSON"""
    conn = sqlite3.connect('database/users.db')
    c = conn.cursor()
    
    c.execute('''
        SELECT id, age, sleep_efficiency, disorder_type, risk_score, risk_level, created_at
        FROM assessments 
        WHERE user_id = ? 
        ORDER BY created_at DESC
    ''', (session['user_id'],))
    
    assessments = c.fetchall()
    conn.close()
    
    assessment_list = []
    for a in assessments:
        assessment_list.append({
            'id': a[0],
            'age': a[1],
            'sleep_efficiency': a[2],
            'disorder_type': a[3],
            'risk_score': a[4],
            'risk_level': a[5],
            'created_at': a[6]
        })
    
    return jsonify({'assessments': assessment_list})

@app.route('/history')
@login_required
def history():
    """User assessment history"""
    conn = sqlite3.connect('database/users.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM assessments WHERE user_id = ? ORDER BY created_at DESC''', 
             (session['user_id'],))
    assessments = c.fetchall()
    conn.close()
    
    return render_template('history.html', assessments=assessments)

@app.route('/assessment/<int:assessment_id>')
@login_required
def assessment_details(assessment_id):
    conn = sqlite3.connect('database/users.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM assessments 
                 WHERE id = ? AND user_id = ?''', 
              (assessment_id, session['user_id']))
    assessment = c.fetchone()
    conn.close()
    if not assessment:
        return redirect(url_for('history'))
    
    assessment_data = {
        'id': assessment[0],
        'age': assessment[3],
        'gender': assessment[4],
        'sleep_duration': assessment[6],
        'rem_sleep': assessment[7],
        'deep_sleep': assessment[8],
        'light_sleep': assessment[9],
        'awakenings': assessment[10],
        'sleep_efficiency': assessment[15],
        'disorder_type': assessment[16],
        'risk_score': assessment[17],
        'risk_level': assessment[18],
        'created_at': assessment[19],
    }
    return render_template('assessment_details.html', assessment=assessment_data)

@app.route('/export')
@login_required
def export_data():
    """Export user assessment history as CSV"""
    conn = sqlite3.connect('database/users.db')
    c = conn.cursor()
    c.execute('''SELECT * FROM assessments WHERE user_id = ? ORDER BY created_at DESC''', 
             (session['user_id'],))
    assessments = c.fetchall()
    conn.close()
    
    # Create CSV in memory
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['Date', 'Age', 'Gender', 'Sleep Efficiency', 'Disorder', 
                     'Risk Score', 'Risk Level'])
    
    for assessment in assessments:
        writer.writerow([
            assessment[18],  # created_at
            assessment[3],   # age
            assessment[4],   # gender
            assessment[15],  # sleep_efficiency
            assessment[16],  # disorder_type
            assessment[17],  # risk_score
            assessment[18]   # risk_level
        ])
    
    output.seek(0)
    return send_file(
        io.BytesIO(output.getvalue().encode()),
        mimetype='text/csv',
        as_attachment=True,
        download_name=f'sleep_assessments_{datetime.now().strftime("%Y%m%d")}.csv'
    )

# ============================================================================
# ERROR HANDLING
# ============================================================================

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

# ============================================================================
# APPLICATION ENTRY POINT
# ============================================================================

if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=5000,
        threaded=True
    )
