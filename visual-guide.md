# 🎨 VISUAL CUSTOMIZATION REFERENCE

## How CSS Variables Work (Visual Guide)

### The Color System Structure

```
style.css:
├── :root { --color-variables }  ← All colors defined here
└── .classes { var(--color-name) }  ← Used by HTML elements


HTML:
├── Navbar: uses --color-charcoal-700
├── Buttons: use --color-teal-500
└── All styled automatically!
```

---

## COLOR VARIABLES QUICK REFERENCE

### 🎨 Primary Colors (Most Important)

| Variable | Current Color | Use Case |
|----------|--------------|----------|
| `--color-charcoal-700` | Dark Gray | Navbar background |
| `--color-gray-200` | Light Gray | Navbar text |
| `--color-teal-500` | Teal/Blue | Primary button |
| `--color-teal-600` | Darker Teal | Button hover |
| `--color-teal-700` | Even Darker | Button active |
| `--color-cream-50` | Off-white | Page background |
| `--color-slate-900` | Dark Blue | Main text |

### 📍 Where Each Color Shows

```
┌─────────────────────────────────────────┐
│  Navbar (--color-charcoal-700)          │ ← Dark background
│  SleepAI  │ Home │ Assessment │ Logout  │ ← (--color-gray-200 text)
├─────────────────────────────────────────┤
│                                         │
│  Page Background (--color-cream-50)     │ ← Off-white/cream
│                                         │
│  ┌─────────────────────────────────┐   │
│  │ Card (--color-cream-100)        │   │
│  │                                 │   │
│  │  Text: (--color-slate-900)      │   │
│  │                                 │   │
│  │  [Button] (--color-teal-500)    │   │ ← Teal/Blue
│  │   Hover: (--color-teal-600)     │   │
│  │  Click: (--color-teal-700)      │   │
│  └─────────────────────────────────┘   │
│                                         │
└─────────────────────────────────────────┘
```

---

## REAL-WORLD COLOR EXAMPLES

### Example 1: Purple Theme

**Original (Teal):**
```css
--color-teal-500: rgba(33, 128, 141, 1);      /* Teal */
--color-teal-600: rgba(29, 116, 128, 1);      /* Dark Teal */
--color-teal-700: rgba(26, 104, 115, 1);      /* Very Dark Teal */
```

**Your Change (Purple):**
```css
--color-teal-500: rgba(156, 39, 176, 1);      /* Purple */
--color-teal-600: rgba(142, 36, 159, 1);      /* Dark Purple */
--color-teal-700: rgba(123, 31, 162, 1);      /* Very Dark Purple */
```

### Example 2: Red & Orange Theme

**Original:**
```css
--color-charcoal-700: rgba(31, 33, 33, 1);    /* Dark Gray */
--color-teal-500: rgba(33, 128, 141, 1);      /* Teal */
```

**Your Change:**
```css
--color-charcoal-700: rgba(139, 0, 0, 1);     /* Dark Red */
--color-teal-500: rgba(255, 140, 0, 1);       /* Orange */
```

### Example 3: Green Theme

**Original:**
```css
--color-charcoal-700: rgba(31, 33, 33, 1);    /* Dark Gray */
--color-teal-500: rgba(33, 128, 141, 1);      /* Teal */
```

**Your Change:**
```css
--color-charcoal-700: rgba(27, 94, 32, 1);    /* Dark Green */
--color-teal-500: rgba(76, 175, 80, 1);       /* Bright Green */
```

---

## How to Pick Colors Online

### Step 1: Go to Color Picker
- https://www.google.com/search?q=color+picker
- Click "Open Color Picker"

### Step 2: Choose Your Color
- Click on the color square
- Or type hex code like `#FF5733`

### Step 3: Get RGB Values
- You'll see something like: RGB(255, 87, 51)
- Write down: 255, 87, 51

### Step 4: Convert to CSS Format
- `rgb(255, 87, 51)` becomes `rgba(255, 87, 51, 1)`

### Step 5: Copy to style.css
```css
--color-teal-500: rgba(255, 87, 51, 1);
```

---

## WHERE COLORS APPEAR IN YOUR APP

### 1. Navbar Area
```
┌─────────────────────────┐
│ SleepAI  Home  History  │  ← Navbar (dark color)
│ Assessment  Logout      │  ← Text (light color)
└─────────────────────────┘
  Colors used:
  - Background: --color-charcoal-700
  - Text: --color-gray-200
  - Links: --color-teal-500
```

### 2. Buttons
```
[Click Here]  ← Normal (--color-teal-500)
  ↓ mouse over
[Click Here]  ← Hover (--color-teal-600 - darker)
  ↓ click
[Click Here]  ← Active (--color-teal-700 - even darker)
```

### 3. Cards & Content
```
┌─────────────────────────┐
│ Card Title              │  ← --color-teal-500 (blue text)
│                         │
│ This is content text    │  ← --color-slate-900 (dark text)
│                         │
│ [Learn More Button]     │  ← --color-teal-500 button
└─────────────────────────┘
  Background: --color-cream-100 (light)
  Border: --color-border
```

### 4. Status Indicators
```
🟢 LOW RISK       ← --color-success (green)
🟡 MEDIUM RISK    ← --color-warning (orange)
🔴 HIGH RISK      ← --color-error (red)
```

---

## STEP-BY-STEP: Color Customization

### Task: Change Navbar to Purple

**Step 1:** Open `style.css`

**Step 2:** Find line ~20:
```css
--color-charcoal-700: rgba(31, 33, 33, 1);
```

**Step 3:** Replace with:
```css
--color-charcoal-700: rgba(88, 28, 135, 1);
```

**Step 4:** Also change button colors (line ~35):
```css
/* BEFORE */
--color-teal-500: rgba(33, 128, 141, 1);
--color-teal-600: rgba(29, 116, 128, 1);
--color-teal-700: rgba(26, 104, 115, 1);

/* AFTER */
--color-teal-500: rgba(156, 39, 176, 1);
--color-teal-600: rgba(142, 36, 159, 1);
--color-teal-700: rgba(123, 31, 162, 1);
```

**Step 5:** Save file

**Step 6:** Hard refresh browser:
- Windows: `Ctrl + Shift + Delete`
- Mac: `Cmd + Shift + Delete`

**Step 7:** Look at navbar - should be purple!

---

## ADD IMAGES - File Structure

### Before Adding Images
```
your-project/
├── app_advanced.py
├── requirements.txt
├── static/
│   ├── style.css
│   ├── charts.js
│   └── (no images folder)
├── templates/
│   ├── home.html
│   └── ...
└── database/
```

### After Adding Images
```
your-project/
├── app_advanced.py
├── requirements.txt
├── static/
│   ├── style.css
│   ├── charts.js
│   └── images/          ← NEW FOLDER
│       ├── home/
│       │   ├── hero.jpg
│       │   └── background.jpg
│       ├── results/
│       │   └── success.jpg
│       └── icons/
│           ├── check.png
│           └── warning.png
├── templates/
│   ├── home.html
│   └── ...
└── database/
```

### How to Add Image to HTML

**File Path Format:**
```html
<!-- CORRECT -->
<img src="/static/images/home/hero.jpg">

<!-- WRONG -->
<img src="images/hero.jpg">        ← Missing /static/
<img src="static/images/hero.jpg">  ← Extra static/
<img src="C:\Users\...\hero.jpg">   ← Wrong path format
```

### Image Size Guidelines

```css
/* Small icon */
.icon { width: 50px; height: 50px; }

/* Medium image in card */
.card-image { width: 200px; height: 150px; }

/* Large hero/banner */
.hero-image { width: 100%; max-width: 600px; }

/* Full screen background */
.background-image { 
  width: 100%;
  height: 100vh;
  background-size: cover;
}
```

---

## ADD VIDEOS - YouTube Embed Guide

### Getting Video ID

**Original URL:** `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
**Video ID:** `dQw4w9WgXcQ` (everything after `v=`)

### Embed Code

```html
<!-- Full width responsive video -->
<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
  <iframe 
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
    src="https://www.youtube.com/embed/dQw4w9WgXcQ"
    frameborder="0"
    allowfullscreen>
  </iframe>
</div>

<!-- Fixed size video -->
<iframe 
  width="560" height="315"
  src="https://www.youtube.com/embed/dQw4w9WgXcQ"
  frameborder="0"
  allowfullscreen>
</iframe>
```

### Video Size Options

| Width | Height | Best For |
|-------|--------|----------|
| 560 | 315 | Standard desktop |
| 100% | auto | Mobile responsive |
| 320 | 180 | Small screens |
| 800 | 450 | Large displays |

---

## BUTTON STYLING

### Current Button Appearance

```
Primary Button (.btn--primary):
┌────────────────────┐
│  CLICK HERE        │  ← Teal background
│                    │  ← Light text
└────────────────────┘
  Hover: Darker teal
  Click: Even darker teal

Secondary Button (.btn--secondary):
┌────────────────────┐
│  CLICK HERE        │  ← Light brown background
│                    │  ← Dark text
└────────────────────┘

Outline Button (.btn--outline):
┌────────────────────┐
│  CLICK HERE        │  ← Transparent, border only
│                    │  ← Dark text
└────────────────────┘
```

### Change Button Styles in CSS

```css
/* Original Primary Button */
.btn--primary {
  background: var(--color-teal-500);      /* Teal */
  color: var(--color-btn-primary-text);   /* Light text */
}

/* Your Custom Purple Primary Button */
.btn--primary {
  background: rgba(156, 39, 176, 1);      /* Purple */
  color: #ffffff;                         /* White text */
}

/* Your Custom Large Buttons */
.btn--lg {
  padding: var(--space-10) var(--space-20);
  font-size: var(--font-size-lg);
  border-radius: var(--radius-md);
}
```

---

## COMMON MISTAKES & FIXES

### ❌ Mistake 1: Wrong Image Path

```html
<!-- WRONG - doesn't work -->
<img src="images/photo.jpg">

<!-- RIGHT - works -->
<img src="/static/images/photo.jpg">
```

### ❌ Mistake 2: Forgetting to Save CSS

```
Action: Change color in style.css
Problem: Browser still shows old color
Solution: Save file, then hard refresh (Ctrl+Shift+Delete)
```

### ❌ Mistake 3: Hard-coded Colors

```html
<!-- WRONG - doesn't follow theme -->
<div style="background: red;">

<!-- RIGHT - follows color system -->
<div style="background: var(--color-primary);">
```

### ❌ Mistake 4: Button Link Goes Nowhere

```html
<!-- WRONG - no route exists -->
<a href="/page-that-doesnt-exist">Click</a>

<!-- RIGHT - route exists in app_advanced.py -->
<a href="/sleep-disorders">Click</a>
```

### ❌ Mistake 5: YouTube Embed Wrong Format

```html
<!-- WRONG - full watch URL -->
<iframe src="https://www.youtube.com/watch?v=dQw4w9WgXcQ"></iframe>

<!-- RIGHT - embed URL -->
<iframe src="https://www.youtube.com/embed/dQw4w9WgXcQ"></iframe>
```

---

## TESTING CHANGES

### Checklist Before Testing

- [ ] Saved all edited files
- [ ] Restarted Python app if added routes
- [ ] Hard refreshed browser (Ctrl+Shift+Delete)
- [ ] No browser errors (F12 to check console)
- [ ] Images file paths correct

### Test Each Feature

**Color Change:**
1. Open app
2. Look at navbar
3. Should see new color
4. Check buttons too

**Image Added:**
1. Go to page
2. Should see image
3. If not, check console for errors (F12)
4. Check file path in HTML

**Video Added:**
1. Go to page
2. Should see video player
3. Click play button
4. Video should play

**Button Fixed:**
1. Click button
2. Should navigate to page
3. New page should load
4. "Back" button should work

---

## COLOR COMBINATIONS (Ready to Use)

### Theme 1: Professional Blue
```css
--color-charcoal-700: rgba(0, 51, 102, 1);    /* Dark Blue */
--color-gray-200: rgba(255, 255, 255, 1);    /* White */
--color-teal-500: rgba(0, 102, 204, 1);      /* Bright Blue */
--color-teal-600: rgba(0, 77, 153, 1);       /* Medium Blue */
--color-teal-700: rgba(0, 51, 102, 1);       /* Dark Blue */
--color-cream-50: rgba(240, 248, 255, 1);    /* Alice Blue */
```

### Theme 2: Modern Green
```css
--color-charcoal-700: rgba(27, 94, 32, 1);   /* Dark Green */
--color-gray-200: rgba(255, 255, 255, 1);    /* White */
--color-teal-500: rgba(76, 175, 80, 1);      /* Bright Green */
--color-teal-600: rgba(56, 142, 60, 1);      /* Medium Green */
--color-teal-700: rgba(40, 167, 69, 1);      /* Deep Green */
--color-cream-50: rgba(240, 255, 240, 1);    /* Honeydew */
```

### Theme 3: Energetic Orange
```css
--color-charcoal-700: rgba(230, 126, 34, 1); /* Dark Orange */
--color-gray-200: rgba(255, 255, 255, 1);    /* White */
--color-teal-500: rgba(255, 152, 0, 1);      /* Bright Orange */
--color-teal-600: rgba(245, 127, 23, 1);     /* Medium Orange */
--color-teal-700: rgba(230, 124, 115, 1);    /* Deep Orange */
--color-cream-50: rgba(255, 248, 225, 1);    /* Floral White */
```

### Theme 4: Medical Purple
```css
--color-charcoal-700: rgba(88, 28, 135, 1);  /* Dark Purple */
--color-gray-200: rgba(255, 255, 255, 1);    /* White */
--color-teal-500: rgba(156, 39, 176, 1);     /* Bright Purple */
--color-teal-600: rgba(142, 36, 159, 1);     /* Medium Purple */
--color-teal-700: rgba(123, 31, 162, 1);     /* Deep Purple */
--color-cream-50: rgba(245, 245, 250, 1);    /* Ghost White */
```

---

**Happy customizing! 🎨✨**
