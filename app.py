import streamlit as st

# Page configuration - MUST be first Streamlit command
st.set_page_config(
    page_title="Love Arcade Deluxe",
    page_icon="💕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import page modules after set_page_config
from modules import home, relationship_quiz, memory_timeline, mini_games, secret_letter, progress_page


# Custom CSS for pastel theme with rounded UI
def load_css():
    st.markdown("""
    <style>
        /* Pastel color scheme */
        :root {
            --pastel-pink: #FFD1DC;
            --pastel-purple: #E0BBE4;
            --pastel-blue: #BFEAF5;
            --pastel-yellow: #FFFACD;
            --pastel-green: #C1FFC1;
            --pastel-peach: #FFE5CC;
        }
        
        /* Main app styling */
        .stApp {
            background: linear-gradient(135deg, #FFD1DC 0%, #E0BBE4 100%);
        }
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #E0BBE4 0%, #BFEAF5 100%);
            border-radius: 15px;
            padding: 20px;
        }
        
        /* Buttons */
        .stButton > button {
            border-radius: 20px;
            border: none;
            background: linear-gradient(135deg, #FFD1DC 0%, #E0BBE4 100%);
            color: #333;
            font-weight: bold;
            padding: 10px 25px;
            transition: all 0.3s;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 8px rgba(0,0,0,0.15);
        }
        
        /* Text input and other inputs */
        .stTextInput > div > div > input,
        .stSelectbox > div > div > select,
        .stNumberInput > div > div > input {
            border-radius: 15px;
            border: 2px solid #E0BBE4;
            padding: 10px;
        }
        
        /* Cards/containers */
        .stMetric,
        [data-testid="stMetricValue"] {
            background: rgba(255, 255, 255, 0.8);
            border-radius: 15px;
            padding: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        
        /* Headers */
        h1, h2, h3 {
            color: #8B4789;
            text-shadow: 2px 2px 4px rgba(255,255,255,0.5);
        }
        
        /* Progress bar */
        .stProgress > div > div > div > div {
            background: linear-gradient(90deg, #FFD1DC 0%, #E0BBE4 50%, #BFEAF5 100%);
            border-radius: 10px;
        }
        
        /* Expander */
        .streamlit-expanderHeader {
            background: rgba(255, 255, 255, 0.6);
            border-radius: 15px;
            border: 2px solid #E0BBE4;
        }
        
        /* Info boxes */
        .stAlert {
            border-radius: 15px;
        }
        
        /* Radio buttons */
        .stRadio > label {
            background: rgba(255, 255, 255, 0.6);
            padding: 10px;
            border-radius: 10px;
            margin: 5px 0;
        }
    </style>
    """, unsafe_allow_html=True)


# Initialize session state
def initialize_state():
    if "initialized" not in st.session_state:
        # Scores
        st.session_state.total_score = 0
        st.session_state.quiz_score = 0
        st.session_state.memory_score = 0
        st.session_state.game_scores = {
            "tictactoe": 0,
            "memory_match": 0,
            "reaction": 0
        }
        
        # Completion flags
        st.session_state.quiz_completed = False
        st.session_state.memory_completed = False
        st.session_state.games_completed = {
            "tictactoe": False,
            "memory_match": False,
            "reaction": False
        }
        
        # Game states
        st.session_state.tictactoe_board = [[" " for _ in range(3)] for _ in range(3)]
        st.session_state.current_player = "X"
        st.session_state.game_over = False
        st.session_state.memory_cards = []
        st.session_state.flipped_cards = []
        
        # Memory timeline
        st.session_state.memories = []

        # Reaction game state
        st.session_state.reaction_state = "ready"
        st.session_state.reaction_start_time = None

        # Level system
        st.session_state.level = 1
        
        # Letter unlock
        st.session_state.letter_unlocked = False
        
        # Mark as initialized
        st.session_state.initialized = True


def main():
    initialize_state()
    load_css()
    
    # Sidebar navigation
    st.sidebar.title("💕 Love Arcade Deluxe")
    st.sidebar.markdown("---")
    
    # Display current score and level in sidebar
    st.sidebar.metric("Total Score", st.session_state.total_score)
    st.sidebar.metric("Level", st.session_state.level)
    st.sidebar.markdown("---")
    
    # Navigation
    page = st.sidebar.radio(
        "Navigate",
        ["🏠 Home", "💑 Relationship Quiz", "📸 Memory Timeline", 
         "🎮 Mini Games", "💌 Secret Letter", "📊 Progress"],
        label_visibility="collapsed"
    )
    
    # Route to appropriate page
    if page == "🏠 Home":
        home.show()
    elif page == "💑 Relationship Quiz":
        relationship_quiz.show()
    elif page == "📸 Memory Timeline":
        memory_timeline.show()
    elif page == "🎮 Mini Games":
        mini_games.show()
    elif page == "💌 Secret Letter":
        secret_letter.show()
    elif page == "📊 Progress":
        progress_page.show()


if __name__ == "__main__":
    main()
