import streamlit as st
import random
import time
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from .ui_components import render_page_header, render_card, render_game_card, render_section_divider
except ImportError:
    # Fallback for Streamlit Cloud
    import importlib.util
    ui_components_path = os.path.join(os.path.dirname(__file__), "ui_components.py")
    spec = importlib.util.spec_from_file_location("ui_components", ui_components_path)
    ui_components = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ui_components)

    render_page_header = ui_components.render_page_header
    render_card = ui_components.render_card
    render_game_card = ui_components.render_game_card
    render_section_divider = ui_components.render_section_divider


def show():
    """Mini games collection: TicTacToe, Memory Match, Reaction"""

    # Page header
    render_page_header(
        title="Mini Games",
        subtitle="Choose a game to play and earn points! Each game completion earns you 20 points! 🎯",
        icon="🎮"
    )

    # Game cards preview
    col1, col2, col3 = st.columns(3)

    with col1:
        render_game_card(
            title="TicTacToe",
            description="Classic strategy game against AI",
            icon="🎯",
            completed=st.session_state.games_completed["tictactoe"],
            points=20
        )

    with col2:
        render_game_card(
            title="Memory Match",
            description="Find matching pairs of cards",
            icon="🃏",
            completed=st.session_state.games_completed["memory_match"],
            points=20
        )

    with col3:
        render_game_card(
            title="Reaction Game",
            description="Test your reflexes!",
            icon="⚡",
            completed=st.session_state.games_completed["reaction"],
            points=20
        )

    render_section_divider()

    # Game selection
    game_choice = st.selectbox(
        "🎮 Select a Game to Play:",
        ["🎯 TicTacToe", "🃏 Memory Match", "⚡ Reaction Game"]
    )
    
    st.markdown("<br>", unsafe_allow_html=True)

    if game_choice == "🎯 TicTacToe":
        show_tictactoe()
    elif game_choice == "🃏 Memory Match":
        show_memory_match()
    elif game_choice == "⚡ Reaction Game":
        show_reaction_game()


def show_tictactoe():
    """TicTacToe game implementation"""

    game_header = """
    <div style="text-align: center; margin-bottom: 24px;">
        <h2 style="color: #8B4789; margin: 0;">🎯 TicTacToe</h2>
        <p style="color: #8E7FA0;">You are X, Computer is O. Win to earn points!</p>
    </div>
    """
    st.markdown(game_header, unsafe_allow_html=True)

    if st.session_state.games_completed["tictactoe"]:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #E8F8E8 0%, rgba(255,255,255,0.95) 100%);
            border: 1px solid #C1F0C1;
            border-radius: 24px;
            padding: 32px;
            box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
            margin-bottom: 24px;
            text-align: center;
        ">
            <div style="font-size: 3rem; margin-bottom: 12px;">🏆</div>
            <p style="color: #8B4789; font-weight: 600; font-size: 1.2rem; margin: 0;">
                TicTacToe Completed! You earned 20 points!
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🔄 Play Again", use_container_width=True):
            st.session_state.games_completed["tictactoe"] = False
            reset_tictactoe()
            st.rerun()
        return
    
    # Game board container
    st.markdown("""
    <div style="
        background: rgba(255, 255, 255, 0.92);
        padding: 24px;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
        max-width: 350px;
        margin: 0 auto;
    ">
    """, unsafe_allow_html=True)

    # Center the board
    col_spacer1, col_board, col_spacer2 = st.columns([1, 2, 1])

    with col_board:
        # Display board with styled buttons
        for i in range(3):
            cols = st.columns(3)
            for j in range(3):
                with cols[j]:
                    cell = st.session_state.tictactoe_board[i][j]
                    display = cell if cell != " " else "·"

                    # Style based on cell content
                    if cell == "X":
                        display = "❌"
                    elif cell == "O":
                        display = "⭕"

                    if st.button(
                        display,
                        key=f"cell_{i}_{j}",
                        disabled=st.session_state.game_over or cell != " ",
                        use_container_width=True
                    ):
                        make_move(i, j)
                        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    # Game status
    winner = check_winner()
    if winner:
        st.session_state.game_over = True

        if winner == "X":
            st.success("🎉 You won! Great job!")
            award_game_points("tictactoe")
        elif winner == "O":
            st.error("😅 Computer wins! Try again!")
        else:
            st.info("🤝 It's a draw!")

        if st.button("🆕 New Game", use_container_width=True):
            reset_tictactoe()
            st.rerun()
    elif st.session_state.game_over:
        if st.button("🆕 New Game", use_container_width=True):
            reset_tictactoe()
            st.rerun()


def reset_tictactoe():
    """Reset TicTacToe game state"""
    st.session_state.tictactoe_board = [[" " for _ in range(3)] for _ in range(3)]
    st.session_state.current_player = "X"
    st.session_state.game_over = False


def make_move(row, col):
    """Make a move in TicTacToe"""
    if st.session_state.tictactoe_board[row][col] == " " and not st.session_state.game_over:
        st.session_state.tictactoe_board[row][col] = "X"
        
        if not check_winner() and not is_board_full():
            # Computer's turn
            ai_move()


def ai_move():
    """Simple AI for computer opponent"""
    empty_cells = [(i, j) for i in range(3) for j in range(3) 
                   if st.session_state.tictactoe_board[i][j] == " "]
    if empty_cells:
        row, col = random.choice(empty_cells)
        st.session_state.tictactoe_board[row][col] = "O"


def check_winner():
    """Check if there's a winner in TicTacToe"""
    board = st.session_state.tictactoe_board
    
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    # Check for draw
    if is_board_full():
        return "Draw"
    
    return None


def is_board_full():
    """Check if TicTacToe board is full"""
    return all(cell != " " for row in st.session_state.tictactoe_board for cell in row)


def show_memory_match():
    """Memory Match card game"""

    game_header = """
    <div style="text-align: center; margin-bottom: 24px;">
        <h2 style="color: #8B4789; margin: 0;">🃏 Memory Match</h2>
        <p style="color: #8E7FA0;">Find all matching pairs to win!</p>
    </div>
    """
    st.markdown(game_header, unsafe_allow_html=True)

    if st.session_state.games_completed["memory_match"]:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #E8F8E8 0%, rgba(255,255,255,0.95) 100%);
            border: 1px solid #C1F0C1;
            border-radius: 24px;
            padding: 32px;
            box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
            margin-bottom: 24px;
            text-align: center;
        ">
            <div style="font-size: 3rem; margin-bottom: 12px;">🏆</div>
            <p style="color: #8B4789; font-weight: 600; font-size: 1.2rem; margin: 0;">
                Memory Match Completed! You earned 20 points!
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🔄 Play Again", use_container_width=True):
            st.session_state.games_completed["memory_match"] = False
            reset_memory_match()
            st.rerun()
        return
    
    # Initialize game
    if "memory_cards" not in st.session_state or not st.session_state.memory_cards:
        reset_memory_match()
    
    # Progress
    matched_pairs = sum(1 for card in st.session_state.memory_cards if card['matched']) // 2
    total_pairs = len(st.session_state.memory_cards) // 2

    progress_html = f"""
    <div style="
        text-align: center;
        margin-bottom: 20px;
        padding: 12px 24px;
        background: rgba(255, 255, 255, 0.92);
        border-radius: 50px;
        display: inline-block;
    ">
        <span style="color: #8E7FA0;">Pairs Found: </span>
        <span style="color: #8B4789; font-weight: 700;">{matched_pairs}/{total_pairs}</span>
    </div>
    """
    st.markdown(f"<div style='text-align: center;'>{progress_html}</div>", unsafe_allow_html=True)

    # Display cards in a grid
    st.markdown("""
    <div style="
        background: rgba(255, 255, 255, 0.92);
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
    ">
    """, unsafe_allow_html=True)

    cols_per_row = 4
    for i in range(0, 16, cols_per_row):
        cols = st.columns(cols_per_row)
        for j in range(cols_per_row):
            idx = i + j
            if idx < len(st.session_state.memory_cards):
                with cols[j]:
                    card = st.session_state.memory_cards[idx]
                    if card['matched'] or idx in st.session_state.flipped_cards:
                        st.button(
                            card['emoji'],
                            key=f"card_{idx}",
                            disabled=True,
                            use_container_width=True
                        )
                    else:
                        if st.button("❓", key=f"card_{idx}", use_container_width=True):
                            # If two cards are already flipped and don't match, reset them first
                            if len(st.session_state.flipped_cards) == 2:
                                st.session_state.flipped_cards = []
                            handle_card_flip(idx)
                            st.rerun()
    
    st.markdown("</div>", unsafe_allow_html=True)

    # Check if game is won
    if all(card['matched'] for card in st.session_state.memory_cards):
        st.success("🎉 You matched all pairs!")
        award_game_points("memory_match")
        st.balloons()
        if st.button("🆕 New Game", use_container_width=True):
            reset_memory_match()
            st.rerun()


def reset_memory_match():
    """Reset Memory Match game"""
    emojis = ["❤️", "💕", "🌹", "💝", "🎁", "⭐", "🌈", "🦋"]
    cards = [{"emoji": emoji, "matched": False} for emoji in emojis] * 2
    random.shuffle(cards)
    st.session_state.memory_cards = cards
    st.session_state.flipped_cards = []


def handle_card_flip(idx):
    """Handle card flip in Memory Match"""
    if len(st.session_state.flipped_cards) < 2 and idx not in st.session_state.flipped_cards:
        st.session_state.flipped_cards.append(idx)
        
        if len(st.session_state.flipped_cards) == 2:
            idx1, idx2 = st.session_state.flipped_cards
            if st.session_state.memory_cards[idx1]['emoji'] == st.session_state.memory_cards[idx2]['emoji']:
                st.session_state.memory_cards[idx1]['matched'] = True
                st.session_state.memory_cards[idx2]['matched'] = True
                # Immediately clear flipped cards for matched pairs
                st.session_state.flipped_cards = []
            else:
                # For non-matching pairs, cards will stay flipped until next click
                pass


def show_reaction_game():
    """Reaction time game"""

    game_header = """
    <div style="text-align: center; margin-bottom: 24px;">
        <h2 style="color: #8B4789; margin: 0;">⚡ Reaction Game</h2>
        <p style="color: #8E7FA0;">Click as fast as you can when the button turns green!</p>
    </div>
    """
    st.markdown(game_header, unsafe_allow_html=True)

    if st.session_state.games_completed["reaction"]:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #E8F8E8 0%, rgba(255,255,255,0.95) 100%);
            border: 1px solid #C1F0C1;
            border-radius: 24px;
            padding: 32px;
            box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
            margin-bottom: 24px;
            text-align: center;
        ">
            <div style="font-size: 3rem; margin-bottom: 12px;">🏆</div>
            <p style="color: #8B4789; font-weight: 600; font-size: 1.2rem; margin: 0;">
                Reaction Game Completed! You earned 20 points!
            </p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🔄 Play Again", use_container_width=True):
            st.session_state.games_completed["reaction"] = False
            st.session_state.reaction_state = "ready"
            st.rerun()
        return
    
    if "reaction_state" not in st.session_state:
        st.session_state.reaction_state = "ready"
        st.session_state.reaction_start_time = None
    
    # Game container
    st.markdown("""
    <div style="
        background: rgba(255, 255, 255, 0.92);
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
        text-align: center;
        max-width: 500px;
        margin: 0 auto;
    ">
    """, unsafe_allow_html=True)

    if st.session_state.reaction_state == "ready":
        st.markdown("""
        <div style="font-size: 4rem; margin-bottom: 20px;">🎯</div>
        <p style="color: #6B5B7A; margin-bottom: 24px;">
            Press the button to start. When it turns <strong style="color: #4CAF50;">GREEN</strong>, click as fast as you can!
        </p>
        """, unsafe_allow_html=True)

        if st.button("🚀 Start Reaction Test", use_container_width=True):
            st.session_state.reaction_state = "waiting"
            st.session_state.reaction_start_time = time.time() + random.uniform(1, 3)
            st.rerun()
    
    elif st.session_state.reaction_state == "waiting":
        current_time = time.time()
        if current_time >= st.session_state.reaction_start_time:
            st.session_state.reaction_state = "go"
            st.session_state.reaction_start_time = time.time()
            st.rerun()
        else:
            st.markdown("""
            <div style="
                font-size: 4rem;
                margin-bottom: 20px;
                animation: pulse 1s infinite;
            ">⏳</div>
            <p style="
                color: #FF9800;
                font-weight: 700;
                font-size: 1.5rem;
                margin-bottom: 24px;
            ">Wait for it...</p>
            """, unsafe_allow_html=True)

            # Rerun to check timing
            time.sleep(0.1)
            st.rerun()
    
    elif st.session_state.reaction_state == "go":
        st.markdown("""
        <style>
            @keyframes glow {
                0%, 100% { box-shadow: 0 0 20px #4CAF50; }
                50% { box-shadow: 0 0 40px #4CAF50; }
            }
        </style>
        <div style="
            font-size: 4rem;
            margin-bottom: 20px;
        ">🟢</div>
        <p style="
            color: #4CAF50;
            font-weight: 700;
            font-size: 2rem;
            margin-bottom: 24px;
            animation: pulse 0.3s infinite;
        ">CLICK NOW!</p>
        """, unsafe_allow_html=True)

        if st.button("🟢 CLICK!", use_container_width=True):
            reaction_time = time.time() - st.session_state.reaction_start_time

            if reaction_time < 0.5:
                st.success(f"⚡ Lightning fast! {reaction_time:.3f} seconds!")
                st.balloons()
                award_game_points("reaction")
            elif reaction_time < 1.0:
                st.success(f"⚡ Great reflexes! {reaction_time:.3f} seconds!")
                award_game_points("reaction")
            else:
                st.info(f"Your reaction time: {reaction_time:.3f} seconds. Try to be faster!")

            st.session_state.reaction_state = "ready"

            if st.button("🔄 Try Again", use_container_width=True):
                st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)


def award_game_points(game_name):
    """Award points for completing a game"""
    if not st.session_state.games_completed[game_name]:
        st.session_state.games_completed[game_name] = True
        st.session_state.game_scores[game_name] = 20
        st.session_state.total_score += 20
        st.session_state.level = (st.session_state.total_score // 50) + 1
