# 🎨 Complete Guide: Change Colors, Add Images/Videos & Fix Buttons

## Part 1: Understanding Your Color System

Your app uses **CSS Color Variables** stored in `style.css`. This is the EASIEST way to customize colors!

### Current Dark Navbar Colors
```
Dark background: #1F2121 (charcoal-700)
Text color: #F5F5F5 (light gray)
Buttons: Teal/Blue colors
```

---

## Part 2: QUICK COLOR CHANGES (5 Minutes)

### ✅ Step 1: Open `style.css` file

### ✅ Step 2: Find This Section (Around Line 20)
```css
:root {
  /* Primitive Color Tokens */
  --color-charcoal-700: rgba(31, 33, 33, 1);
  --color-charcoal-800: rgba(38, 40, 40, 1);
  --color-teal-500: rgba(33, 128, 141, 1);
```

### ✅ Step 3: Change Navbar Background Color

**FIND THIS:**
```css
--color-charcoal-700: rgba(31, 33, 33, 1);
```

**REPLACE WITH YOUR COLOR:**

**Examples:**
```css
/* Deep Purple */
--color-charcoal-700: rgba(88, 28, 135, 1);

/* Deep Blue */
--color-charcoal-700: rgba(13, 71, 161, 1);

/* Deep Green */
--color-charcoal-700: rgba(27, 94, 32, 1);

/* Dark Red */
--color-charcoal-700: rgba(120, 29, 32, 1);

/* Navy */
--color-charcoal-700: rgba(25, 32, 71, 1);
```

### ✅ Step 4: Save and Refresh Browser

**Browser: Press `Ctrl + Shift + Delete` (Hard Refresh)**

---

## Part 3: Understand Color Codes

### How to Get Your Own Color

**Method 1: Use a Color Picker Online**
1. Go to: https://www.google.com/search?q=color+picker
2. Pick your color
3. Copy the RGB values
4. Format: `rgba(R, G, B, 1)` where R, G, B are numbers 0-255

**Method 2: Examples of Popular Colors**

| Color | RGB Code | CSS Format |
|-------|----------|-----------|
| Red | 255, 0, 0 | `rgba(255, 0, 0, 1)` |
| Green | 0, 128, 0 | `rgba(0, 128, 0, 1)` |
| Blue | 0, 0, 255 | `rgba(0, 0, 255, 1)` |
| Purple | 128, 0, 128 | `rgba(128, 0, 128, 1)` |
| Orange | 255, 165, 0 | `rgba(255, 165, 0, 1)` |
| Pink | 255, 192, 203 | `rgba(255, 192, 203, 1)` |
| Yellow | 255, 255, 0 | `rgba(255, 255, 0, 1)` |
| Cyan | 0, 255, 255 | `rgba(0, 255, 255, 1)` |

---

## Part 4: Complete Color Customization

### All Important Color Variables in style.css

```css
/* 🎨 NAVBAR/HEADER COLORS */
--color-charcoal-700: rgba(31, 33, 33, 1);     /* ← Navbar background */
--color-gray-200: rgba(245, 245, 245, 1);     /* ← Navbar text */

/* 🎨 BUTTON COLORS */
--color-teal-500: rgba(33, 128, 141, 1);      /* ← Primary button */
--color-teal-600: rgba(29, 116, 128, 1);      /* ← Button hover */
--color-teal-700: rgba(26, 104, 115, 1);      /* ← Button active/click */

/* 🎨 BACKGROUND COLORS */
--color-cream-50: rgba(252, 252, 249, 1);     /* ← Page background */
--color-cream-100: rgba(255, 255, 253, 1);    /* ← Card background */

/* 🎨 TEXT COLORS */
--color-slate-900: rgba(19, 52, 59, 1);       /* ← Main text */
--color-slate-500: rgba(98, 108, 113, 1);     /* ← Secondary text */

/* 🎨 STATUS COLORS */
--color-success: var(--color-teal-500);       /* ← Green checkmark */
--color-error: var(--color-red-500);          /* ← Red errors */
--color-warning: var(--color-orange-500);     /* ← Yellow warnings */
```

### Complete Color Change Example

**BEFORE (Current):**
```css
--color-charcoal-700: rgba(31, 33, 33, 1);
--color-gray-200: rgba(245, 245, 245, 1);
--color-teal-500: rgba(33, 128, 141, 1);
--color-teal-600: rgba(29, 116, 128, 1);
--color-teal-700: rgba(26, 104, 115, 1);
```

**AFTER (Your Custom Theme):**
```css
--color-charcoal-700: rgba(88, 28, 135, 1);    /* Purple navbar */
--color-gray-200: rgba(255, 255, 255, 1);     /* White text */
--color-teal-500: rgba(156, 39, 176, 1);      /* Purple buttons */
--color-teal-600: rgba(142, 36, 159, 1);      /* Purple hover */
--color-teal-700: rgba(123, 31, 162, 1);      /* Purple active */
```

---

## Part 5: ADD IMAGES TO YOUR APP

### ✅ Step 1: Create Folders

In your project folder, create:
```
/static/
  /images/          ← NEW FOLDER
    /home/
    /results/
    /icons/
```

### ✅ Step 2: Add Images (3 Methods)

**Method 1: Add Background Image to Page**

Open `style.css` and add:
```css
/* Add after the :root section, around line 100 */

.home-page {
  background-image: url('/static/images/home/background.jpg');
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

.navbar-background {
  background-image: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), 
                    url('/static/images/navbar-bg.jpg');
  background-size: cover;
  background-position: center;
}
```

**Method 2: Add Image to HTML Page**

Open `home.html` and add:
```html
<!-- Add after the welcome heading -->
<div class="hero-image">
  <img src="/static/images/home/hero.jpg" alt="Sleep wellness" class="hero-img">
</div>
```

Then add CSS in `style.css`:
```css
.hero-img {
  width: 100%;
  max-width: 600px;
  height: auto;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  margin: 20px auto;
  display: block;
}
```

**Method 3: Add Image to Cards**

In `home.html`:
```html
<div class="card">
  <img src="/static/images/icons/assessment.png" alt="Assessment" class="card-icon">
  <h3>Sleep Assessment</h3>
  <p>Analyze your sleep patterns...</p>
</div>
```

CSS in `style.css`:
```css
.card-icon {
  width: 80px;
  height: 80px;
  margin-bottom: 15px;
}
```

### ✅ Step 3: Download Free Images

**Best Free Image Sites:**
- Unsplash: https://unsplash.com (search "sleep", "wellness", "bedroom")
- Pexels: https://www.pexels.com
- Pixabay: https://pixabay.com
- Flaticon: https://www.flaticon.com (for icons)

**Download Steps:**
1. Search for "sleep" or "wellness" images
2. Download in JPG format
3. Save to `/static/images/home/` folder
4. Use in HTML/CSS

---

## Part 6: ADD VIDEOS TO YOUR APP

### ✅ Step 1: Add YouTube Video (EASIEST)

In `home.html`:
```html
<!-- Add in home page content -->
<div class="video-section">
  <h3>🎥 Sleep Tips & Wellness</h3>
  <iframe width="100%" height="400" 
          src="https://www.youtube.com/embed/XXXXXXXXXXX" 
          title="Sleep Wellness" 
          frameborder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen>
  </iframe>
</div>
```

**How to Get YouTube Video ID:**
1. Go to YouTube
2. Search "sleep wellness" or any video you want
3. Click video
4. Copy URL: `https://www.youtube.com/watch?v=XXXXXXXXXXX`
5. Use only: `XXXXXXXXXXX` part

**Example:**
```html
<iframe width="100%" height="400" 
        src="https://www.youtube.com/embed/dQw4w9WgXcQ" 
        title="Sleep Tips" 
        frameborder="0" 
        allowfullscreen>
</iframe>
```

### ✅ Step 2: Add CSS for Video

In `style.css`:
```css
.video-section {
  background: var(--color-surface);
  padding: 30px;
  border-radius: 12px;
  margin: 20px 0;
  border: 1px solid var(--color-border);
}

.video-section h3 {
  margin-bottom: 20px;
  color: var(--color-text);
}

.video-section iframe {
  border-radius: 8px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}
```

### ✅ Step 3: Responsive Video (Mobile Friendly)

```css
.video-container {
  position: relative;
  width: 100%;
  padding-bottom: 56.25%; /* 16:9 aspect ratio */
  height: 0;
  overflow: hidden;
  border-radius: 8px;
}

.video-container iframe {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}
```

HTML:
```html
<div class="video-container">
  <iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ" 
          frameborder="0" 
          allowfullscreen>
  </iframe>
</div>
```

---

## Part 7: FIX "LEARN MORE" BUTTON

### 🐛 Problem: Learn More Button Not Working

**The Issue:** No route/page exists for "Learn More"

### ✅ Solution: Add the Route

**Step 1: Open `app_advanced.py`**

**Step 2: Add this new route (after home route, around line 300):**

```python
@app.route('/sleep-disorders')
@login_required
def sleep_disorders():
    """Learn more about sleep disorders"""
    return render_template('sleep_disorders.html')
```

**Step 3: Create new file `templates/sleep_disorders.html`**

```html
{% extends 'base.html' %}

{% block title %}Sleep Disorders - Learn More{% endblock %}

{% block content %}

<div class="disorders-container">
    <h1>🏥 Understanding Sleep Disorders</h1>
    
    <div class="disorder-card">
        <h2>🚫 Insomnia</h2>
        <p><strong>What it is:</strong> Difficulty falling or staying asleep</p>
        <p><strong>Symptoms:</strong> Lying awake for hours, frequent night awakenings</p>
        <p><strong>What you can do:</strong></p>
        <ul>
            <li>Maintain consistent sleep schedule</li>
            <li>Avoid screens 1 hour before bed</li>
            <li>Try relaxation techniques (meditation, deep breathing)</li>
            <li>Limit caffeine after 2 PM</li>
            <li>Consult a sleep specialist if persistent</li>
        </ul>
    </div>

    <div class="disorder-card">
        <h2>😴 Sleep Apnea</h2>
        <p><strong>What it is:</strong> Breathing stops and starts during sleep</p>
        <p><strong>Symptoms:</strong> Loud snoring, gasping during sleep, daytime fatigue</p>
        <p><strong>What you can do:</strong></p>
        <ul>
            <li>Get a sleep study (polysomnography)</li>
            <li>Use CPAP machine if prescribed</li>
            <li>Sleep on your side</li>
            <li>Maintain healthy weight</li>
            <li>Avoid alcohol and sedatives</li>
        </ul>
    </div>

    <div class="disorder-card">
        <h2>🧠 REM Sleep Behavior Disorder</h2>
        <p><strong>What it is:</strong> Acting out dreams during REM sleep</p>
        <p><strong>Symptoms:</strong> Moving, talking, or punching while sleeping</p>
        <p><strong>What you can do:</strong></p>
        <ul>
            <li>Create safe sleeping environment</li>
            <li>Use relaxation techniques</li>
            <li>Avoid alcohol and caffeine</li>
            <li>Consult neurologist for medication options</li>
        </ul>
    </div>

    <div class="disorder-card">
        <h2>⚡ Narcolepsy</h2>
        <p><strong>What it is:</strong> Excessive daytime sleepiness and sudden sleep attacks</p>
        <p><strong>Symptoms:</strong> Falling asleep suddenly, sleep paralysis, hallucinations</p>
        <p><strong>What you can do:</strong></p>
        <ul>
            <li>Schedule regular naps (15-30 mins)</li>
            <li>Keep consistent sleep schedule</li>
            <li>Exercise regularly</li>
            <li>Medication management with doctor</li>
            <li>Professional support essential</li>
        </ul>
    </div>

    <div class="info-box">
        <h3>💡 When to See a Doctor</h3>
        <ul>
            <li>Sleep problems lasting more than 2 weeks</li>
            <li>Excessive daytime sleepiness</li>
            <li>Loud snoring with pauses in breathing</li>
            <li>Sleep paralysis or hallucinations</li>
            <li>Any sleep disorder affecting quality of life</li>
        </ul>
    </div>

    <a href="/home" class="btn btn--primary" style="margin-top: 30px;">← Back to Home</a>
</div>

{% endblock %}
```

**Step 4: Add CSS to `style.css`**

```css
.disorders-container {
    max-width: 900px;
    margin: 0 auto;
    padding: 30px 20px;
}

.disorders-container h1 {
    text-align: center;
    margin-bottom: 40px;
    color: var(--color-text);
}

.disorder-card {
    background: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: 12px;
    padding: 25px;
    margin-bottom: 20px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.disorder-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.disorder-card h2 {
    color: var(--color-primary);
    margin-top: 0;
    margin-bottom: 15px;
    font-size: 22px;
}

.disorder-card ul {
    margin: 15px 0;
    padding-left: 25px;
}

.disorder-card li {
    margin-bottom: 10px;
    color: var(--color-text);
    line-height: 1.6;
}

.info-box {
    background: var(--color-bg-1);
    border-left: 4px solid var(--color-primary);
    padding: 20px;
    border-radius: 8px;
    margin-top: 30px;
}

.info-box h3 {
    margin-top: 0;
    color: var(--color-primary);
}
```

**Step 5: Update home.html to Link "Learn More" Button**

**FIND this in home.html:**
```html
<a href="#" class="btn btn--primary">Learn More</a>
```

**REPLACE WITH:**
```html
<a href="/sleep-disorders" class="btn btn--primary">Learn More</a>
```

---

## Part 8: FIX "VIEW DETAILS" BUTTON (History Page)

### 🐛 Problem: View Details Button Not Working

**The Issue:** Missing route and modal/page to show details

### ✅ Solution: Add Details View

**Step 1: Open `app_advanced.py`**

**Step 2: Add this new route (after history route, around line 380):**

```python
@app.route('/assessment/<int:assessment_id>')
@login_required
def assessment_details(assessment_id):
    """View detailed assessment results"""
    conn = sqlite3.connect('database/users.db')
    c = conn.cursor()
    
    c.execute('''SELECT * FROM assessments 
                 WHERE id = ? AND user_id = ?''', 
              (assessment_id, session['user_id']))
    
    assessment = c.fetchone()
    conn.close()
    
    if not assessment:
        return redirect(url_for('history'))
    
    # Convert to dict for template
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
```

**Step 3: Create `templates/assessment_details.html`**

```html
{% extends 'base.html' %}

{% block title %}Assessment Details{% endblock %}

{% block content %}

<div class="details-container">
    <a href="/history" class="btn btn--outline" style="margin-bottom: 20px;">← Back to History</a>
    
    <h1>📋 Assessment Details</h1>
    
    <div class="details-header">
        <div class="detail-item">
            <span class="label">📅 Date:</span>
            <span class="value">{{ assessment.created_at }}</span>
        </div>
        <div class="detail-item">
            <span class="label">👤 Age:</span>
            <span class="value">{{ assessment.age }} years</span>
        </div>
        <div class="detail-item">
            <span class="label">⚧ Gender:</span>
            <span class="value">{{ assessment.gender }}</span>
        </div>
    </div>

    <div class="details-grid">
        <!-- Sleep Duration -->
        <div class="detail-card">
            <h3>😴 Sleep Duration</h3>
            <div class="big-value">{{ assessment.sleep_duration }}<span class="unit">hrs</span></div>
        </div>

        <!-- Sleep Efficiency -->
        <div class="detail-card">
            <h3>⚡ Sleep Efficiency</h3>
            <div class="big-value">{{ "%.2f"|format(assessment.sleep_efficiency * 100) }}<span class="unit">%</span></div>
        </div>

        <!-- Awakenings -->
        <div class="detail-card">
            <h3>⏰ Awakenings</h3>
            <div class="big-value">{{ assessment.awakenings }}<span class="unit">times</span></div>
        </div>

        <!-- Disorder Type -->
        <div class="detail-card">
            <h3>🏥 Disorder Type</h3>
            <div class="big-value" style="font-size: 20px;">{{ assessment.disorder_type }}</div>
        </div>
    </div>

    <div class="sleep-stages">
        <h3>🧠 Sleep Stages Breakdown</h3>
        <div class="stage-chart">
            <div class="stage-bar">
                <div class="stage-name">REM Sleep</div>
                <div class="stage-value">{{ assessment.rem_sleep }}%</div>
                <div class="stage-visual" style="width: {{ assessment.rem_sleep }}%; background: #FF6B6B;"></div>
            </div>
            <div class="stage-bar">
                <div class="stage-name">Deep Sleep</div>
                <div class="stage-value">{{ assessment.deep_sleep }}%</div>
                <div class="stage-visual" style="width: {{ assessment.deep_sleep }}%; background: #4ECDC4;"></div>
            </div>
            <div class="stage-bar">
                <div class="stage-name">Light Sleep</div>
                <div class="stage-value">{{ assessment.light_sleep }}%</div>
                <div class="stage-visual" style="width: {{ assessment.light_sleep }}%; background: #95E1D3;"></div>
            </div>
        </div>
    </div>

    <div class="risk-assessment">
        <h3>📊 Risk Assessment</h3>
        <div class="risk-box {% if 'LOW' in assessment.risk_level %}low{% elif 'MEDIUM' in assessment.risk_level %}medium{% else %}high{% endif %}">
            <div class="risk-score">{{ assessment.risk_score }}/100</div>
            <div class="risk-level">{{ assessment.risk_level }}</div>
        </div>
    </div>

    <a href="/home" class="btn btn--primary" style="margin-top: 30px;">← Back to Home</a>
</div>

{% endblock %}
```

**Step 4: Add CSS to `style.css`**

```css
.details-container {
    max-width: 900px;
    margin: 0 auto;
    padding: 30px 20px;
}

.details-header {
    display: flex;
    gap: 30px;
    background: var(--color-surface);
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 30px;
    border: 1px solid var(--color-border);
    flex-wrap: wrap;
}

.detail-item {
    display: flex;
    flex-direction: column;
}

.detail-item .label {
    font-weight: 600;
    color: var(--color-text-secondary);
    font-size: 12px;
    text-transform: uppercase;
    margin-bottom: 5px;
}

.detail-item .value {
    font-size: 18px;
    color: var(--color-text);
    font-weight: 500;
}

.details-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
    margin-bottom: 30px;
}

.detail-card {
    background: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: 12px;
    padding: 25px;
    text-align: center;
}

.detail-card h3 {
    margin-top: 0;
    margin-bottom: 15px;
    font-size: 16px;
    color: var(--color-text-secondary);
}

.big-value {
    font-size: 36px;
    font-weight: 700;
    color: var(--color-primary);
    margin-bottom: 5px;
}

.unit {
    font-size: 14px;
    font-weight: 400;
    color: var(--color-text-secondary);
    margin-left: 5px;
}

.sleep-stages {
    background: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: 12px;
    padding: 25px;
    margin-bottom: 30px;
}

.stage-chart {
    margin-top: 20px;
}

.stage-bar {
    margin-bottom: 20px;
}

.stage-name {
    font-weight: 600;
    color: var(--color-text);
    margin-bottom: 5px;
}

.stage-value {
    font-size: 14px;
    color: var(--color-text-secondary);
    margin-bottom: 5px;
}

.stage-visual {
    height: 30px;
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    padding-right: 10px;
    color: white;
    font-weight: 600;
}

.risk-assessment {
    background: var(--color-surface);
    border: 1px solid var(--color-border);
    border-radius: 12px;
    padding: 25px;
}

.risk-box {
    display: flex;
    gap: 20px;
    align-items: center;
    padding: 20px;
    border-radius: 8px;
    margin-top: 15px;
}

.risk-box.low {
    background: rgba(76, 175, 80, 0.1);
    border: 2px solid #4CAF50;
}

.risk-box.medium {
    background: rgba(255, 193, 7, 0.1);
    border: 2px solid #FFC107;
}

.risk-box.high {
    background: rgba(244, 67, 54, 0.1);
    border: 2px solid #F44336;
}

.risk-score {
    font-size: 48px;
    font-weight: 700;
    min-width: 120px;
}

.risk-level {
    font-size: 20px;
    font-weight: 600;
    color: var(--color-text);
}
```

**Step 5: Update `history.html` to Link View Details Button**

In your `history.html`, find:
```html
<button class="btn btn--primary">View Details</button>
```

Replace with:
```html
<a href="/assessment/{{ assessment.id }}" class="btn btn--primary">View Details</a>
```

Or if it's in a table, replace the entire table row rendering with:
```html
<td>
    <a href="/assessment/{{ assessment.0 }}" class="btn btn--primary btn--sm">View Details</a>
</td>
```

---

## Part 9: TEST YOUR CHANGES

### ✅ Checklist

- [ ] Changed navbar color in `style.css`
- [ ] Refreshed browser (Ctrl+Shift+Delete)
- [ ] Created `/static/images/` folder
- [ ] Added images to folders
- [ ] Added image HTML to home.html
- [ ] Added "Learn More" route to `app_advanced.py`
- [ ] Created `sleep_disorders.html`
- [ ] Updated "Learn More" button link
- [ ] Added "View Details" route to `app_advanced.py`
- [ ] Created `assessment_details.html`
- [ ] Updated "View Details" button links
- [ ] Tested all buttons work

### Quick Test Steps

1. **Color change:**
   - Open `http://127.0.0.1:5000/home`
   - Should see new navbar color

2. **Learn More:**
   - Click "Learn More" button
   - Should go to sleep disorders page

3. **View Details:**
   - Go to History page
   - Click any "View Details" button
   - Should show detailed assessment

---

## Part 10: VIDEO TUTORIAL - Common Mistakes

### ❌ Common Mistake #1: Hard-coded Colors
**Wrong:**
```html
<div style="background: red;">
```
**Right:**
```html
<div style="background: var(--color-primary);">
```

### ❌ Common Mistake #2: Wrong File Path for Images
**Wrong:**
```html
<img src="images/photo.jpg">
```
**Right:**
```html
<img src="/static/images/photo.jpg">
```

### ❌ Common Mistake #3: Forgetting Flask Route
**Wrong:** Button links to page that doesn't exist
```html
<a href="/learn-more">
```
**Right:** Route exists in app_advanced.py
```python
@app.route('/learn-more')
def learn_more():
    return render_template('learn_more.html')
```

---

## 🎓 Next Steps

1. **Color Theme Generator:**
   - Visit: https://coolors.co
   - Generate professional color palettes
   - Copy RGB values to `style.css`

2. **Stock Photos:**
   - Download from Unsplash/Pexels
   - Save to `/static/images/`
   - Use in HTML

3. **Advanced Customization:**
   - Change button styles
   - Update card designs
   - Customize fonts
   - Add animations

---

## 📞 Quick Reference

| Task | File | What to Change |
|------|------|-----------------|
| Change navbar color | `style.css` | `--color-charcoal-700` |
| Change button color | `style.css` | `--color-teal-500` |
| Add page | `app_advanced.py` | Add new `@app.route()` |
| Add HTML page | Create file | `templates/new.html` |
| Add image | HTML file | `<img src="/static/images/...">` |
| Add video | HTML file | `<iframe src="...">` |
| Fix button | Update `href` | Point to real route |

---

**You've got this! 🚀**
