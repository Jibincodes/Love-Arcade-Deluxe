import streamlit as st
import sys
import os

# Add current directory to Python path for Streamlit Cloud
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Page configuration - MUST be first Streamlit command
st.set_page_config(
    page_title="Love Arcade Deluxe",
    page_icon="💕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import page modules after set_page_config with error handling
try:
    from modules import home
    from modules import relationship_quiz
    from modules import memory_timeline
    from modules import mini_games
    from modules import secret_letter
    from modules import progress_page
    from modules.ui_components import load_global_css, render_level_badge
except ImportError as e:
    st.error(f"Import error: {e}")
    st.info("Trying alternative import method...")
    # Alternative import method for Streamlit Cloud
    import importlib.util

    def load_module(module_name, file_path):
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module

    # Load modules directly
    base_dir = os.path.dirname(os.path.abspath(__file__))
    modules_dir = os.path.join(base_dir, "modules")

    home = load_module("home", os.path.join(modules_dir, "home.py"))
    relationship_quiz = load_module("relationship_quiz", os.path.join(modules_dir, "relationship_quiz.py"))
    memory_timeline = load_module("memory_timeline", os.path.join(modules_dir, "memory_timeline.py"))
    mini_games = load_module("mini_games", os.path.join(modules_dir, "mini_games.py"))
    secret_letter = load_module("secret_letter", os.path.join(modules_dir, "secret_letter.py"))
    progress_page = load_module("progress_page", os.path.join(modules_dir, "progress_page.py"))
    ui_components = load_module("ui_components", os.path.join(modules_dir, "ui_components.py"))

    load_global_css = ui_components.load_global_css
    render_level_badge = ui_components.render_level_badge


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
    load_global_css()

    # Sidebar navigation
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; padding: 16px 0 24px 0;">
            <div style="font-size: 2.5rem; margin-bottom: 8px;">💕</div>
            <h1 style="font-size: 1.3rem !important; margin: 0 !important; text-align: center !important;">
                Love Arcade Deluxe
            </h1>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("---")

        # Display current score and level in sidebar with custom styling
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Score", st.session_state.total_score)
        with col2:
            st.metric("Level", st.session_state.level)

        # Level badge
        st.markdown("<div style='margin: 16px 0;'>", unsafe_allow_html=True)
        render_level_badge(st.session_state.level)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("---")

        # Navigation
        page = st.radio(
            "Navigate",
            ["🏠 Home", "💑 Relationship Quiz", "📸 Memory Timeline",
             "🎮 Mini Games", "💌 Secret Letter", "📊 Progress"],
            label_visibility="collapsed"
        )

        # Footer
        st.markdown("---")
        st.markdown("""
        <div style="text-align: center; padding: 16px 0; opacity: 0.7;">
            <small>Made with 💕</small>
        </div>
        """, unsafe_allow_html=True)

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
