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
render_progress_card = ui_components.render_progress_card
render_letter_envelope = ui_components.render_letter_envelope
render_confetti = ui_components.render_confetti
render_section_divider = ui_components.render_section_divider
render_checklist_item = ui_components.render_checklist_item


def show():
    """Secret letter that unlocks when requirements are met"""

    # Check unlock conditions
    score_requirement = 100
    completion_requirements = {
        "quiz": st.session_state.quiz_completed,
        "memory": st.session_state.memory_completed,
        "at_least_one_game": any(st.session_state.games_completed.values())
    }
    
    score_met = st.session_state.total_score >= score_requirement
    completions_met = all(completion_requirements.values())
    
    if score_met and completions_met:
        st.session_state.letter_unlocked = True
    
    # Display based on unlock status
    if not st.session_state.letter_unlocked:
        # Locked state
        render_page_header(
            title="Secret Letter",
            subtitle="Complete the requirements to unlock this special message! 💌",
            icon="🔒"
        )

        render_letter_envelope(unlocked=False)

        render_section_divider()

        # Requirements
        st.markdown("""
        <h3 style="text-align: center; color: #8B4789; margin-bottom: 24px;">
            📋 Unlock Requirements
        </h3>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div style="
                background: linear-gradient(135deg, #FFE4EC 0%, rgba(255,255,255,0.95) 100%);
                border: 1px solid #FFD1DC;
                border-radius: 24px;
                padding: 24px;
                padding-bottom: 16px;
                box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
                margin-bottom: 16px;
            ">
                <h4 style="color: #8B4789; margin: 0;">🎯 Score Requirement</h4>
            </div>
            """, unsafe_allow_html=True)
            render_progress_card("Points Needed", st.session_state.total_score, score_requirement, "⭐")

            if score_met:
                st.success("✅ Score requirement met!")
            else:
                points_needed = score_requirement - st.session_state.total_score
                st.info(f"💫 Need {points_needed} more points")

        with col2:
            st.markdown("""
            <div style="
                background: linear-gradient(135deg, #F0E6F4 0%, rgba(255,255,255,0.95) 100%);
                border: 1px solid #E0BBE4;
                border-radius: 24px;
                padding: 24px;
                padding-bottom: 16px;
                box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
                margin-bottom: 16px;
            ">
                <h4 style="color: #8B4789; margin: 0;">✅ Completion Requirements</h4>
            </div>
            """, unsafe_allow_html=True)

            render_checklist_item("Complete Relationship Quiz", completion_requirements['quiz'])
            render_checklist_item("Complete Memory Timeline (3+ memories)", completion_requirements['memory'])
            render_checklist_item("Complete at least one Mini Game", completion_requirements['at_least_one_game'])

        render_section_divider()

        # Motivational message
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, #E8F6FA 0%, rgba(255,255,255,0.95) 100%);
            border: 1px solid #BFEAF5;
            border-radius: 24px;
            padding: 32px;
            box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
            margin-bottom: 24px;
            text-align: center;
        ">
            <div style="font-size: 2rem; margin-bottom: 12px;">💪</div>
            <p style="color: #6B5B7A; font-size: 1.1rem; margin: 0;">
                Keep going! A special message is waiting for you! 💝
            </p>
        </div>
        """, unsafe_allow_html=True)

    else:
        # Unlocked state - show the secret message!
        render_page_header(
            title="Secret Letter",
            subtitle="You've unlocked a special message! 💕",
            icon="💌"
        )

        # Show confetti on first unlock
        if "confetti_shown" not in st.session_state:
            st.session_state.confetti_shown = True
            render_confetti()
            st.balloons()
        
        render_letter_envelope(unlocked=True)

        # The letter content with beautiful styling
        st.markdown("""
        <div style="
            background: linear-gradient(135deg, rgba(255,255,255,0.98) 0%, rgba(255,240,245,0.98) 100%);
            padding: 48px;
            border-radius: 24px;
            box-shadow: 0 20px 60px rgba(139, 71, 137, 0.15);
            border: 2px solid rgba(224, 187, 228, 0.3);
            max-width: 700px;
            margin: 0 auto 32px auto;
            position: relative;
        ">
            <div style="
                position: absolute;
                top: 16px;
                right: 16px;
                font-size: 1.5rem;
            ">💕</div>
            
            <div style="
                font-family: Georgia, serif;
                color: #6B5B7A;
                line-height: 2;
                font-size: 1.1rem;
            ">
                <p style="
                    color: #8B4789;
                    font-weight: 600;
                    font-size: 1.3rem;
                    margin-bottom: 24px;
                ">My Dearest Love,</p>
                
                <p>If you're reading this, it means you've completed all the challenges! 
                I'm so proud of you! 🎉</p>
                
                <p>This little arcade was created especially for you, filled with love and care. 
                Every game, every question, every moment was designed to make you smile 
                and to show you just how much you mean to me. 💕</p>
                
                <p>You are my favorite person, my best friend, and my greatest adventure. 
                Thank you for being you, for your laughter, your kindness, and for making 
                every day brighter. ☀️</p>
                
                <p>Remember, no matter what challenges come our way, we'll face them together — 
                just like you completed these games! 🎮</p>
                
                <p>Keep being amazing, keep smiling, and know that you are loved beyond measure. ❤️</p>
                
                <div style="margin-top: 32px; text-align: right;">
                    <p style="margin-bottom: 8px;"><strong>Forever yours,</strong></p>
                    <p style="
                        color: #8B4789;
                        font-size: 1.2rem;
                        font-weight: 600;
                    ">Your Biggest Fan 💝</p>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        render_section_divider()

        # Achievement badge
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
            <div style="font-size: 3rem; margin-bottom: 12px;">🏆</div>
            <h3 style="color: #DAA520; margin-bottom: 8px; margin-top: 0;">Achievement Unlocked!</h3>
            <p style="font-size: 1.3rem; font-weight: 700; color: #8B4789; margin-bottom: 8px;">
                Love Arcade Master
            </p>
            <p style="color: #8E7FA0; margin: 0;">
                You've completed all challenges and unlocked the secret letter!
            </p>
        </div>
        """, unsafe_allow_html=True)
