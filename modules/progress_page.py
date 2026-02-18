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
render_achievement_badge = ui_components.render_achievement_badge
render_section_divider = ui_components.render_section_divider
render_level_badge = ui_components.render_level_badge


def show():
    """Progress page showing stats, achievements, and progress bars"""

    # Page header
    render_page_header(
        title="Your Progress",
        subtitle="Track your journey through Love Arcade Deluxe! 🎯",
        icon="📊"
    )

    # Calculate stats
    completed_activities = (
        int(st.session_state.quiz_completed) +
        int(st.session_state.memory_completed) +
        sum(st.session_state.games_completed.values())
    )
    completion_percentage = int((completed_activities / 5) * 100)
    max_score = 150  # 50 quiz + 50 memory + 60 games

    # Stats row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        render_stat_card("Total Score", str(st.session_state.total_score), "⭐", "gold")
    with col2:
        render_stat_card("Level", str(st.session_state.level), "🏆", "purple")
    with col3:
        render_stat_card("Activities", f"{completed_activities}/5", "📋", "pink")
    with col4:
        render_stat_card("Completion", f"{completion_percentage}%", "✅", "blue")

    render_section_divider()

    # Level progress with custom badge
    st.markdown("""
    <h3 style="text-align: center; color: #8B4789; margin-bottom: 16px;">
        🎖️ Current Level
    </h3>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        render_level_badge(st.session_state.level)

        # Level progress bar
        current_level_threshold = (st.session_state.level - 1) * 50
        next_level_threshold = st.session_state.level * 50
        points_in_level = st.session_state.total_score - current_level_threshold
        points_needed = 50

        st.markdown("<br>", unsafe_allow_html=True)
        render_progress_card(
            f"Level {st.session_state.level} → Level {st.session_state.level + 1}",
            points_in_level,
            points_needed,
            "📈"
        )

    # Level guide
    st.markdown("""
    <div style="
        background: rgba(255, 255, 255, 0.92);
        border: 1px solid rgba(224, 187, 228, 0.2);
        border-radius: 24px;
        padding: 32px;
        box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
        margin-bottom: 24px;
    ">
        <div style="display: flex; justify-content: space-around; flex-wrap: wrap; gap: 12px; text-align: center;">
            <div style="padding: 12px 16px; background: rgba(255,209,220,0.3); border-radius: 12px;">
                <div style="font-weight: 600; color: #8B4789;">Level 1</div>
                <div style="font-size: 0.85rem; color: #8E7FA0;">0-50 pts</div>
                <div style="font-size: 0.8rem;">Just Getting Started 🌱</div>
            </div>
            <div style="padding: 12px 16px; background: rgba(224,187,228,0.3); border-radius: 12px;">
                <div style="font-weight: 600; color: #8B4789;">Level 2</div>
                <div style="font-size: 0.85rem; color: #8E7FA0;">50-100 pts</div>
                <div style="font-size: 0.8rem;">Memory Master 🧠</div>
            </div>
            <div style="padding: 12px 16px; background: rgba(191,234,245,0.3); border-radius: 12px;">
                <div style="font-weight: 600; color: #8B4789;">Level 3</div>
                <div style="font-size: 0.85rem; color: #8E7FA0;">100-150 pts</div>
                <div style="font-size: 0.8rem;">Arcade Queen 👑</div>
            </div>
            <div style="padding: 12px 16px; background: rgba(255,215,0,0.2); border-radius: 12px;">
                <div style="font-weight: 600; color: #8B4789;">Level 4+</div>
                <div style="font-size: 0.85rem; color: #8E7FA0;">150+ pts</div>
                <div style="font-size: 0.8rem;">Soulmate Mode 💕</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    render_section_divider()

    # Two column layout for scores and achievements
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <h3 style="color: #8B4789; margin-bottom: 16px;">📈 Score Breakdown</h3>
        """, unsafe_allow_html=True)

        # Quiz score
        quiz_bg = '#E8F8E8' if st.session_state.quiz_completed else 'rgba(200,200,200,0.2)'
        quiz_color = '#2E7D32' if st.session_state.quiz_completed else '#8E7FA0'
        st.markdown(f"""
        <div style="
            background: rgba(255, 255, 255, 0.92);
            border: 1px solid rgba(224, 187, 228, 0.2);
            border-radius: 24px;
            padding: 24px;
            box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
            margin-bottom: 16px;
        ">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <span style="font-size: 1.5rem; margin-right: 8px;">💑</span>
                    <span style="font-weight: 600; color: #4A3F55;">Relationship Quiz</span>
                </div>
                <div style="
                    background: {quiz_bg};
                    padding: 4px 12px;
                    border-radius: 20px;
                    font-weight: 600;
                    color: {quiz_color};
                ">
                    {st.session_state.quiz_score} pts
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Memory score
        memory_bg = '#E8F8E8' if st.session_state.memory_completed else 'rgba(200,200,200,0.2)'
        memory_color = '#2E7D32' if st.session_state.memory_completed else '#8E7FA0'
        st.markdown(f"""
        <div style="
            background: rgba(255, 255, 255, 0.92);
            border: 1px solid rgba(224, 187, 228, 0.2);
            border-radius: 24px;
            padding: 24px;
            box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
            margin-bottom: 16px;
        ">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <span style="font-size: 1.5rem; margin-right: 8px;">📸</span>
                    <span style="font-weight: 600; color: #4A3F55;">Memory Timeline</span>
                </div>
                <div style="
                    background: {memory_bg};
                    padding: 4px 12px;
                    border-radius: 20px;
                    font-weight: 600;
                    color: {memory_color};
                ">
                    {st.session_state.memory_score} pts
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Game scores
        game_display_names = {
            "tictactoe": ("🎯", "TicTacToe"),
            "memory_match": ("🃏", "Memory Match"),
            "reaction": ("⚡", "Reaction Game")
        }

        for game_name, (icon, display_name) in game_display_names.items():
            completed = st.session_state.games_completed[game_name]
            score = st.session_state.game_scores[game_name]
            game_bg = '#E8F8E8' if completed else 'rgba(200,200,200,0.2)'
            game_color = '#2E7D32' if completed else '#8E7FA0'

            st.markdown(f"""
            <div style="
                background: rgba(255, 255, 255, 0.92);
                border: 1px solid rgba(224, 187, 228, 0.2);
                border-radius: 24px;
                padding: 24px;
                box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
                margin-bottom: 16px;
            ">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <span style="font-size: 1.5rem; margin-right: 8px;">{icon}</span>
                        <span style="font-weight: 600; color: #4A3F55;">{display_name}</span>
                    </div>
                    <div style="
                        background: {game_bg};
                        padding: 4px 12px;
                        border-radius: 20px;
                        font-weight: 600;
                        color: {game_color};
                    ">
                        {score} pts
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <h3 style="color: #8B4789; margin-bottom: 16px;">🏆 Achievements</h3>
        """, unsafe_allow_html=True)

        # Define achievements
        achievements = [
            ("🌟 Beginner", "Earned 50+ points", st.session_state.total_score >= 50),
            ("⭐ Expert", "Earned 100+ points", st.session_state.total_score >= 100),
            ("🧠 Quiz Master", "Completed the relationship quiz", st.session_state.quiz_completed),
            ("📸 Memory Keeper", "Added memories to timeline", st.session_state.memory_completed),
            ("🎮 Game Champion", "Completed all mini games", all(st.session_state.games_completed.values())),
            ("💌 Letter Unlocker", "Unlocked the secret letter", st.session_state.letter_unlocked),
            ("🚀 Level 3+", "Reached level 3 or higher", st.session_state.level >= 3),
        ]

        unlocked_count = sum(1 for _, _, unlocked in achievements if unlocked)

        st.markdown(f"""
        <div style="
            text-align: center;
            padding: 8px;
            margin-bottom: 16px;
            color: #8E7FA0;
        ">
            {unlocked_count} / {len(achievements)} achievements unlocked
        </div>
        """, unsafe_allow_html=True)

        for name, desc, unlocked in achievements:
            render_achievement_badge(name, desc, unlocked)

    render_section_divider()

    # Next goals section
    st.markdown("""
    <h3 style="text-align: center; color: #8B4789; margin-bottom: 16px;">
        🎯 Next Goals
    </h3>
    """, unsafe_allow_html=True)

    goals = []
    
    if not st.session_state.quiz_completed:
        goals.append(("💑", "Complete the Relationship Quiz", "+50 pts"))

    if not st.session_state.memory_completed:
        memories_left = 3 - len(st.session_state.get('memories', []))
        if memories_left > 0:
            goals.append(("📸", f"Add {memories_left} more memories", "+10 pts each"))

    for game_name, completed in st.session_state.games_completed.items():
        if not completed:
            game_names = {"tictactoe": "TicTacToe", "memory_match": "Memory Match", "reaction": "Reaction Game"}
            game_icons = {"tictactoe": "🎯", "memory_match": "🃏", "reaction": "⚡"}
            goals.append((game_icons[game_name], f"Complete {game_names[game_name]}", "+20 pts"))

    if not st.session_state.letter_unlocked:
        points_needed = max(0, 100 - st.session_state.total_score)
        if points_needed > 0:
            goals.append(("💌", f"Earn {points_needed} more points", "Unlock letter"))

    if goals:
        goals_html = "<div style='display: flex; flex-direction: column; gap: 12px;'>"
        for icon, goal, reward in goals[:4]:  # Show max 4 goals
            goals_html += f"""
            <div style="
                display: flex;
                justify-content: space-between;
                align-items: center;
                background: rgba(255, 255, 255, 0.92);
                padding: 16px 20px;
                border-radius: 12px;
                border: 1px solid rgba(224, 187, 228, 0.2);
            ">
                <div style="display: flex; align-items: center; gap: 12px;">
                    <span style="font-size: 1.5rem;">{icon}</span>
                    <span style="color: #6B5B7A;">{goal}</span>
                </div>
                <span style="
                    background: #FFD700;
                    color: white;
                    padding: 4px 12px;
                    border-radius: 20px;
                    font-size: 0.85rem;
                    font-weight: 600;
                ">{reward}</span>
            </div>
            """
        goals_html += "</div>"
        st.markdown(goals_html, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, rgba(255,215,0,0.15) 0%, rgba(255,255,255,0.95) 100%);
            border: 1px solid #FFD700;
            border-radius: 24px;
            padding: 32px;
            box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
            margin-bottom: 24px;
            text-align: center;
        ">
            <div style="font-size: 3rem; margin-bottom: 12px;">🎉</div>
            <p style="color: #8B4789; font-weight: 600; font-size: 1.2rem; margin-bottom: 8px;">
                Congratulations! You've completed everything!
            </p>
            <p style="color: #8E7FA0; margin: 0;">You're a true Love Arcade Champion!</p>
        </div>
        """, unsafe_allow_html=True)
