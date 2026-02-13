# Love-Arcade-Deluxe 💕

A modular Streamlit application featuring interactive games and activities designed to create a fun, engaging experience with a beautiful pastel-themed UI.

## Features

### 🏠 Home Page
- Welcome screen with instructions
- Real-time progress tracking
- Beautiful pastel gradient design

### 💑 Relationship Quiz
- 5 relationship knowledge questions
- Earn 10 points per correct answer (50 points total)
- Updates level and total score
- Can retake to improve score

### 📸 Memory Timeline
- Add and share special memories
- Earn 10 points per memory (up to 50 points)
- Date-based timeline view
- Emotional tagging for each memory

### 🎮 Mini Games
Three interactive games to play:

1. **TicTacToe** - Classic game against AI opponent (20 points)
2. **Memory Match** - Card matching game with emojis (20 points)
3. **Reaction Game** - Test your reaction speed (20 points)

### 💌 Secret Letter
- Locked until requirements are met:
  - Score ≥ 100 points
  - Complete Relationship Quiz
  - Complete Memory Timeline (3+ memories)
  - Complete at least one Mini Game
- Reveals special message when unlocked

### 📊 Progress Page
- Total score and level tracking
- Activity completion status
- Achievement badges
- Progress bars and statistics
- Next goals tracking

## Installation

```bash
# Clone the repository
git clone https://github.com/Jibincodes/Love-Arcade-Deluxe.git
cd Love-Arcade-Deluxe

# Install dependencies
pip install -r requirements.txt
```

## Running the App

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## Requirements

- Python 3.11+
- Streamlit 1.31.0+

## Features Highlight

- **State Management**: All game states, scores, and progress managed via `st.session_state`
- **Modular Design**: Clean separation of pages in the `pages/` directory
- **Pastel Theme**: Custom CSS with rounded UI elements and gradient backgrounds
- **Level System**: Dynamic leveling based on total score (1 level per 50 points)
- **Progress Tracking**: Comprehensive progress bars and achievement system
- **Unlock Logic**: Secret letter unlocks when all requirements are met

## Project Structure

```
Love-Arcade-Deluxe/
├── app.py                      # Main application entry point
├── requirements.txt            # Python dependencies
├── pages/
│   ├── __init__.py
│   ├── home.py                # Home/welcome page
│   ├── relationship_quiz.py   # Quiz page
│   ├── memory_timeline.py     # Memory sharing page
│   ├── mini_games.py          # All mini games
│   ├── secret_letter.py       # Locked letter page
│   └── progress_page.py       # Progress tracking page
└── README.md
```

## How to Play

1. Start with the **Relationship Quiz** to earn your first 50 points
2. Add memories in the **Memory Timeline** for up to 50 more points
3. Play the **Mini Games** to earn 20 points each
4. Reach 100+ points and complete required activities
5. Unlock the **Secret Letter** to read the special message!

## Credits

Built with ❤️ using Streamlit
