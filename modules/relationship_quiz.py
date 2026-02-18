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
render_progress_card = ui_components.render_progress_card


def show():
    """Relationship quiz to test knowledge and earn points"""

    # Page header
    render_page_header(
        title="Relationship Quiz",
        subtitle="Test your relationship knowledge and earn points! 💝",
        icon="💑"
    )

    # Quiz questions
    questions = [
        {
            "question": "What's the most important thing in a relationship?",
            "options": ["Money", "Communication", "Gifts", "Looks"],
            "correct": 1,
            "points": 10
        },
        {
            "question": "How should you resolve conflicts?",
            "options": ["Ignore them", "Talk it out calmly", "Argue loudly", "Give silent treatment"],
            "correct": 1,
            "points": 10
        },
        {
            "question": "What makes a relationship strong?",
            "options": ["Trust and respect", "Jealousy", "Control", "Independence only"],
            "correct": 0,
            "points": 10
        },
        {
            "question": "How often should you express appreciation?",
            "options": ["Never", "Once a year", "Regularly", "Only on special occasions"],
            "correct": 2,
            "points": 10
        },
        {
            "question": "What's key to maintaining romance?",
            "options": ["Expensive gifts", "Quality time together", "Being apart", "Social media posts"],
            "correct": 1,
            "points": 10
        }
    ]
    
    # Check if already completed
    if st.session_state.quiz_completed:
        # Show completion card
        score = st.session_state.quiz_score

        if score >= 40:
            result_message = "Amazing! You're a relationship expert! 💕"
            bg_gradient = "linear-gradient(135deg, #E8F8E8 0%, rgba(255,255,255,0.95) 100%)"
            border_color = "#C1F0C1"
        elif score >= 30:
            result_message = "Great job! You know a lot about love! 💖"
            bg_gradient = "linear-gradient(135deg, #E8F6FA 0%, rgba(255,255,255,0.95) 100%)"
            border_color = "#BFEAF5"
        else:
            result_message = "Good effort! There's always more to learn about love! 💝"
            bg_gradient = "linear-gradient(135deg, #FFE4EC 0%, rgba(255,255,255,0.95) 100%)"
            border_color = "#FFD1DC"

        st.markdown(f"""
        <div style="
            background: {bg_gradient};
            border: 1px solid {border_color};
            border-radius: 24px;
            padding: 32px;
            box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
            margin-bottom: 24px;
            text-align: center;
        ">
            <div style="font-size: 4rem; margin-bottom: 16px;">🎉</div>
            <h2 style="color: #8B4789; margin-bottom: 8px; margin-top: 0;">Quiz Completed!</h2>
            <p style="font-size: 2rem; font-weight: 700; color: #8B4789; margin: 16px 0;">
                {score} / 50 Points
            </p>
            <p style="color: #6B5B7A; font-size: 1.1rem; margin: 0;">{result_message}</p>
        </div>
        """, unsafe_allow_html=True)

        if st.button("🔄 Retake Quiz", use_container_width=True):
            st.session_state.quiz_completed = False
            st.session_state.total_score -= st.session_state.quiz_score
            st.session_state.quiz_score = 0
            st.session_state.level = (st.session_state.total_score // 50) + 1
            st.rerun()
        return
    
    # Progress indicator
    render_progress_card("Questions", 5, 5, "📝")

    # Display quiz in a styled form
    st.markdown("""
    <div style="
        background: linear-gradient(135deg, #E8F6FA 0%, rgba(255,255,255,0.95) 100%);
        border: 1px solid #BFEAF5;
        border-radius: 24px;
        padding: 24px;
        box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
        margin-bottom: 24px;
        text-align: center;
    ">
        <p style="color: #6B5B7A; margin: 0;">
            Answer all 5 questions below. Each correct answer earns you <strong>10 points</strong>!
        </p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("quiz_form"):
        answers = []
        for i, q in enumerate(questions):
            st.markdown(f"""
            <div style="
                background: rgba(255, 255, 255, 0.92);
                padding: 20px;
                border-radius: 16px;
                margin-bottom: 16px;
                border: 1px solid rgba(224, 187, 228, 0.2);
            ">
                <p style="
                    color: #8B4789;
                    font-weight: 600;
                    font-size: 1.1rem;
                    margin-bottom: 8px;
                ">Question {i+1}</p>
                <p style="color: #4A3F55; font-size: 1rem;">{q['question']}</p>
            </div>
            """, unsafe_allow_html=True)

            answer = st.radio(
                f"Select your answer for question {i+1}:",
                q['options'],
                key=f"q_{i}",
                label_visibility="collapsed"
            )
            answers.append(answer)

        st.markdown("<br>", unsafe_allow_html=True)
        submitted = st.form_submit_button("✨ Submit Quiz", use_container_width=True)

        if submitted:
            # Calculate score
            score = 0
            correct_count = 0
            
            for i, q in enumerate(questions):
                if answers[i] == q['options'][q['correct']]:
                    score += q['points']
                    correct_count += 1
            
            # Update session state
            st.session_state.quiz_score = score
            st.session_state.total_score += score
            st.session_state.quiz_completed = True
            
            # Update level based on total score
            st.session_state.level = (st.session_state.total_score // 50) + 1
            
            # Show celebration
            st.balloons()
            st.rerun()
