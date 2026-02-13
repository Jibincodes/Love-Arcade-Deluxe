import streamlit as st


def show():
    """Relationship quiz to test knowledge and earn points"""
    st.title("💑 Relationship Quiz")
    
    st.markdown("""
    <div style='background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 15px; margin-bottom: 20px;'>
        <p style='font-size: 16px; color: #555;'>
            Test your relationship knowledge! Answer these questions and earn points! 💝
        </p>
    </div>
    """, unsafe_allow_html=True)
    
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
        st.success(f"✅ Quiz already completed! You scored {st.session_state.quiz_score} points!")
        if st.button("Retake Quiz"):
            st.session_state.quiz_completed = False
            st.rerun()
        return
    
    # Display quiz
    with st.form("quiz_form"):
        answers = []
        for i, q in enumerate(questions):
            st.markdown(f"**Question {i+1}:** {q['question']}")
            answer = st.radio(
                f"Select your answer:",
                q['options'],
                key=f"q_{i}",
                label_visibility="collapsed"
            )
            answers.append(answer)
            st.markdown("---")
        
        submitted = st.form_submit_button("Submit Quiz", use_container_width=True)
        
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
            
            # Show results
            st.success(f"🎉 Quiz completed! You got {correct_count}/{len(questions)} correct!")
            st.info(f"You earned {score} points!")
            st.balloons()
            st.rerun()
