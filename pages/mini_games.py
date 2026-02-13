import streamlit as st
import random
import time


def show():
    """Mini games collection: TicTacToe, Memory Match, Reaction"""
    st.title("🎮 Mini Games")
    
    st.markdown("""
    <div style='background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 15px; margin-bottom: 20px;'>
        <p style='font-size: 16px; color: #555;'>
            Choose a game to play and earn points! Each game completion earns you 20 points! 🎯
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Game selection
    game_choice = st.selectbox(
        "Select a Game:",
        ["🎯 TicTacToe", "🃏 Memory Match", "⚡ Reaction Game"]
    )
    
    st.markdown("---")
    
    if game_choice == "🎯 TicTacToe":
        show_tictactoe()
    elif game_choice == "🃏 Memory Match":
        show_memory_match()
    elif game_choice == "⚡ Reaction Game":
        show_reaction_game()


def show_tictactoe():
    """TicTacToe game implementation"""
    st.subheader("🎯 TicTacToe")
    
    if st.session_state.games_completed["tictactoe"]:
        st.success("✅ TicTacToe completed! You earned 20 points!")
        if st.button("Play Again"):
            st.session_state.games_completed["tictactoe"] = False
            reset_tictactoe()
            st.rerun()
        return
    
    # Display board
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            with cols[j]:
                cell = st.session_state.tictactoe_board[i][j]
                if st.button(cell if cell != " " else "⬜", 
                           key=f"cell_{i}_{j}", 
                           disabled=st.session_state.game_over or cell != " ",
                           use_container_width=True):
                    make_move(i, j)
                    st.rerun()
    
    # Game status
    winner = check_winner()
    if winner:
        st.session_state.game_over = True
        if winner == "X":
            st.success("🎉 You won! Great job!")
            award_game_points("tictactoe")
        elif winner == "O":
            st.error("Computer wins! Try again!")
        else:
            st.info("It's a draw!")
        
        if st.button("New Game"):
            reset_tictactoe()
            st.rerun()
    elif st.session_state.game_over:
        if st.button("New Game"):
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
    st.subheader("🃏 Memory Match")
    
    if st.session_state.games_completed["memory_match"]:
        st.success("✅ Memory Match completed! You earned 20 points!")
        if st.button("Play Again"):
            st.session_state.games_completed["memory_match"] = False
            reset_memory_match()
            st.rerun()
        return
    
    # Initialize game
    if "memory_cards" not in st.session_state or not st.session_state.memory_cards:
        reset_memory_match()
    
    # Display cards
    st.write("Match all the pairs!")
    
    cols_per_row = 4
    for i in range(0, 16, cols_per_row):
        cols = st.columns(cols_per_row)
        for j in range(cols_per_row):
            idx = i + j
            if idx < len(st.session_state.memory_cards):
                with cols[j]:
                    card = st.session_state.memory_cards[idx]
                    if card['matched'] or idx in st.session_state.flipped_cards:
                        st.button(card['emoji'], key=f"card_{idx}", disabled=True, use_container_width=True)
                    else:
                        if st.button("❓", key=f"card_{idx}", use_container_width=True):
                            handle_card_flip(idx)
                            st.rerun()
    
    # Check if game is won
    if all(card['matched'] for card in st.session_state.memory_cards):
        st.success("🎉 You matched all pairs!")
        award_game_points("memory_match")
        if st.button("New Game"):
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
            
            # Reset flipped cards after a delay (handled in next interaction)
            time.sleep(0.5)
            st.session_state.flipped_cards = []


def show_reaction_game():
    """Reaction time game"""
    st.subheader("⚡ Reaction Game")
    
    if st.session_state.games_completed["reaction"]:
        st.success("✅ Reaction Game completed! You earned 20 points!")
        if st.button("Play Again"):
            st.session_state.games_completed["reaction"] = False
            st.rerun()
        return
    
    st.write("Click the button as fast as you can when it turns green!")
    
    if "reaction_state" not in st.session_state:
        st.session_state.reaction_state = "ready"
        st.session_state.reaction_start_time = None
    
    if st.session_state.reaction_state == "ready":
        if st.button("Start Reaction Test", use_container_width=True):
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
            st.warning("⏳ Wait for it...")
            time.sleep(0.1)
            st.rerun()
    
    elif st.session_state.reaction_state == "go":
        if st.button("🟢 CLICK NOW!", use_container_width=True):
            reaction_time = time.time() - st.session_state.reaction_start_time
            st.success(f"⚡ Your reaction time: {reaction_time:.3f} seconds!")
            
            if reaction_time < 1.0:
                st.balloons()
                award_game_points("reaction")
            else:
                st.info("Good! Try to be faster next time!")
            
            st.session_state.reaction_state = "ready"
            if st.button("Try Again"):
                st.rerun()


def award_game_points(game_name):
    """Award points for completing a game"""
    if not st.session_state.games_completed[game_name]:
        st.session_state.games_completed[game_name] = True
        st.session_state.game_scores[game_name] = 20
        st.session_state.total_score += 20
        st.session_state.level = (st.session_state.total_score // 50) + 1
