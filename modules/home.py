import streamlit as st
import sys
import os

# Get ui_components from sys.modules (loaded by app.py)
if "ui_components" in sys.modules:
    ui_components = sys.modules["ui_components"]
else:
    # Fallback: load directly
    import importlib.util
    ui_components_path = os.path.join(os.path.dirname(__file__), "ui_components.py")
    spec = importlib.util.spec_from_file_location("ui_components", ui_components_path)
    ui_components = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ui_components)

render_page_header = ui_components.render_page_header
render_card = ui_components.render_card
render_stat_card = ui_components.render_stat_card
render_progress_card = ui_components.render_progress_card
render_section_divider = ui_components.render_section_divider
render_checklist_item = ui_components.render_checklist_item


def show():
    """Home page with welcome message and instructions"""

    # Page header
    render_page_header(
        title="Welcome to Love Arcade Deluxe!",
        subtitle="Complete challenges, earn points, and unlock a special surprise! 💝",
        icon="💕"
    )

    # Quick stats row
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        render_stat_card("Total Score", str(st.session_state.total_score), "⭐", "gold")
    with col2:
        render_stat_card("Level", str(st.session_state.level), "🏆", "purple")
    with col3:
        games_done = sum(st.session_state.games_completed.values())
        render_stat_card("Games Done", f"{games_done}/3", "🎮", "pink")
    with col4:
        unlock_progress = min(int((st.session_state.total_score / 100) * 100), 100)
        render_stat_card("Unlock", f"{unlock_progress}%", "💌", "blue")

    render_section_divider()

    # Main content in two columns
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #FFE4EC 0%, rgba(255,255,255,0.95) 100%);
            border: 1px solid #FFD1DC;
            border-radius: 24px;
            padding: 32px;
            box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
            margin-bottom: 24px;
        ">
            <h3 style="color: #8B4789; margin-bottom: 16px; margin-top: 0;">🎯 How to Play</h3>
            <div style="color: #6B5B7A; line-height: 1.8;">
                <div style="display: flex; align-items: flex-start; gap: 12px; margin-bottom: 12px;">
                    <span style="font-size: 1.2rem;">💑</span>
                    <span>Complete the <strong>Relationship Quiz</strong> to earn 50 points</span>
                </div>
                <div style="display: flex; align-items: flex-start; gap: 12px; margin-bottom: 12px;">
                    <span style="font-size: 1.2rem;">📸</span>
                    <span>Share memories in the <strong>Memory Timeline</strong> for up to 50 points</span>
                </div>
                <div style="display: flex; align-items: flex-start; gap: 12px; margin-bottom: 12px;">
                    <span style="font-size: 1.2rem;">🎮</span>
                    <span>Play <strong>Mini Games</strong> and earn 20 points each</span>
                </div>
                <div style="display: flex; align-items: flex-start; gap: 12px; margin-bottom: 12px;">
                    <span style="font-size: 1.2rem;">🎁</span>
                    <span>Reach <strong>100+ points</strong> to unlock the Secret Letter!</span>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Progress checklist header
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #F0E6F4 0%, rgba(255,255,255,0.95) 100%);
            border: 1px solid #E0BBE4;
            border-radius: 24px;
            padding: 32px;
            padding-bottom: 16px;
            box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
            margin-bottom: 16px;
        ">
            <h3 style="color: #8B4789; margin: 0;">📋 Your Progress</h3>
        </div>
        """, unsafe_allow_html=True)

        render_checklist_item("Complete Relationship Quiz", st.session_state.quiz_completed)
        render_checklist_item("Add 3+ Memories", st.session_state.memory_completed)
        render_checklist_item("Win TicTacToe", st.session_state.games_completed["tictactoe"])
        render_checklist_item("Complete Memory Match", st.session_state.games_completed["memory_match"])
        render_checklist_item("Beat Reaction Game", st.session_state.games_completed["reaction"])
        render_checklist_item("Unlock Secret Letter", st.session_state.letter_unlocked)

    render_section_divider()

    # Progress to unlock
    st.markdown("<h3 style='text-align: center; color: #8B4789;'>🔓 Progress to Unlock Secret Letter</h3>", unsafe_allow_html=True)
    render_progress_card("Score Progress", st.session_state.total_score, 100, "💫")

    # Call to action
    if st.session_state.total_score < 100:
        points_needed = 100 - st.session_state.total_score
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #E8F6FA 0%, rgba(255,255,255,0.95) 100%);
            border: 1px solid #BFEAF5;
            border-radius: 24px;
            padding: 32px;
            box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
            margin-bottom: 24px;
            text-align: center;
        ">
            <span style="font-size: 1.5rem; margin-right: 8px;">💡</span>
            <span style="color: #6B5B7A; font-size: 1.1rem;">
                You need <strong style="color: #8B4789;">{points_needed} more points</strong> to unlock the Secret Letter!
            </span>
        </div>
        """, unsafe_allow_html=True)
    else:
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
            <span style="font-size: 1.5rem; margin-right: 8px;">🎉</span>
            <span style="color: #6B5B7A; font-size: 1.1rem;">
                <strong style="color: #8B4789;">Congratulations!</strong> You've unlocked the Secret Letter! Check it out! 💌
            </span>
        </div>
        """, unsafe_allow_html=True)

    # Fun tip at bottom
    tip_content = """
    <div style="text-align: center;">
        <span style="font-size: 1.2rem;">✨</span>
        <span style="color: #8E7FA0; font-style: italic;">
            Tip: Complete all activities to maximize your score and reach Soulmate Mode!
        </span>
        <span style="font-size: 1.2rem;">✨</span>
    </div>
    """
    st.markdown(f"""
    <div style="
        background: rgba(255,255,255,0.6);
        padding: 16px 24px;
        border-radius: 50px;
        margin-top: 24px;
    ">
        {tip_content}
    </div>
    """, unsafe_allow_html=True)
