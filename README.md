# Love-Arcade-Deluxe 💕

A beautifully designed Streamlit application featuring interactive games and activities with a polished, graphic-designer-level aesthetic and soft pastel romantic palette.

## 🚀 App - Deployed!
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://love-arcade-deluxe-gia.streamlit.app/)

## 🌐 Deployment

### ✅ FIXED: Import Error Resolution
This repository has been updated to resolve the `ImportError` that was preventing Streamlit Cloud deployment. 

**What was fixed:**
- ✅ Robust import system with fallback methods
- ✅ Streamlit Cloud compatibility improvements
- ✅ Python path management for module imports
- ✅ Error handling for deployment environments

### Streamlit Community Cloud (Recommended)
1. **Push your latest code to GitHub:**
   ```bash
   git add .
   git commit -m "Fix import errors for Streamlit deployment"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud:**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub account
   - Select your repository
   - **Important:** Make sure your repository is public or you have a Streamlit Cloud Pro account
   
### 🧪 Pre-Deployment Testing
Before deploying, you can verify everything works locally:
```bash
# Test imports
python test_imports.py

# Run locally
streamlit run app.py
```

### 🔧 Troubleshooting Deployment Issues

**If you still get import errors:**
1. Make sure your repository structure matches exactly:
   ```
   Love-Arcade-Deluxe/
   ├── app.py
   ├── requirements.txt
   ├── runtime.txt
   ├── modules/
   │   ├── __init__.py
   │   ├── home.py
   │   ├── relationship_quiz.py
   │   ├── memory_timeline.py
   │   ├── mini_games.py
   │   ├── secret_letter.py
   │   ├── progress_page.py
   │   └── ui_components.py
   └── .streamlit/
       └── config.toml
   ```

2. **Check your files are committed:**
   ```bash
   git status
   git add .
   git commit -m "Add all files"
   git push origin main
   ```

3. **Repository must be public** (for free Streamlit Cloud)

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## ✨ Features

### 🏠 Home Page
- Welcome screen with animated header
- Real-time progress tracking with stat cards
- Interactive checklist showing completion status
- Progress bar toward unlocking the secret letter

### 💑 Relationship Quiz
- 5 relationship knowledge questions with elegant card-based UI
- Earn 10 points per correct answer (50 points total)
- Personalized result messages based on score
- Smooth animations and visual feedback

### 📸 Memory Timeline
- Add and share special memories with beautiful timeline view
- Earn 10 points per memory (up to 50 points)
- Emotion-tagged memories with date tracking
- Card-based memory display

### 🎮 Mini Games
Three interactive games with modern card layouts:

1. **TicTacToe** - Classic strategy game against AI (20 points)
2. **Memory Match** - Find matching pairs with progress tracking (20 points)
3. **Reaction Game** - Test your reflexes with visual feedback (20 points)

### 💌 Secret Letter
- Unlocked when requirements are met:
  - Score ≥ 100 points
  - Complete Relationship Quiz
  - Complete Memory Timeline (3+ memories)
  - Complete at least one Mini Game
- CSS confetti celebration animation
- Beautifully styled letter reveal

### 📊 Progress Dashboard
- Total score and level tracking with stat cards
- Activity completion status with achievement badges
- Level system with custom badges:
  - Level 1: Just Getting Started 🌱 (0-50)
  - Level 2: Memory Master 🧠 (50-100)
  - Level 3: Arcade Queen 👑 (100-150)
  - Level 4: Soulmate Mode 💕 (150+)
- Next goals tracking

## 🎨 Design System

### Visual Identity
- **Soft pastel romantic palette** with pink, purple, and blue tones
- **Premium typography hierarchy** with clear visual rhythm
- **Modern rounded cards** with subtle shadows
- **Consistent 8px spacing scale**
- **Smooth fade-in and hover animations** (CSS only)

### UI Components
- Reusable card components with variants (pink, purple, blue, success, gold)
- Animated stat cards and progress bars
- Achievement badges with unlock states
- Level badges with gradient styling
- CSS confetti celebration effect
- Section dividers with decorative elements

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/Jibincodes/Love-Arcade-Deluxe.git
cd Love-Arcade-Deluxe

# Install dependencies
pip install -r requirements.txt
```

## ▶️ Running the App

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## 📋 Requirements

- Python 3.11+
- Streamlit 1.31.0+

## 📁 Project Structure

```
Love-Arcade-Deluxe/
├── app.py                          # Main application entry point
├── requirements.txt                # Python dependencies
├── modules/
│   ├── __init__.py
│   ├── ui_components.py           # Global CSS theme & reusable components
│   ├── home.py                    # Home/welcome page
│   ├── relationship_quiz.py       # Quiz page
│   ├── memory_timeline.py         # Memory sharing page
│   ├── mini_games.py              # All mini games
│   ├── secret_letter.py           # Locked letter page
│   └── progress_page.py           # Progress tracking page
└── README.md
```

## 🎯 How to Play

1. Start with the **Relationship Quiz** to earn your first 50 points
2. Add memories in the **Memory Timeline** for up to 50 more points
3. Play the **Mini Games** to earn 20 points each
4. Reach 100+ points and complete required activities
5. Unlock the **Secret Letter** to read the special message!

## 💡 Technical Highlights

- **Modular Architecture**: Clean separation with reusable UI components
- **State Management**: All game states managed via `st.session_state`
- **CSS Theme System**: Centralized design tokens and CSS variables
- **Mobile Responsive**: Adaptive layouts for all screen sizes
- **Performance**: CSS-only animations for smooth performance

## 💕 Credits

Built with ❤️ using Streamlit
