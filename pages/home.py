import streamlit as st


def show():
    """Home page with welcome message and instructions"""
    st.title("💕 Welcome to Love Arcade Deluxe!")
    
    st.markdown("""
    <div style='background: rgba(255, 255, 255, 0.8); padding: 30px; border-radius: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'>
        <h2 style='text-align: center; color: #8B4789;'>A Special Game Collection For You! 💝</h2>
        <p style='font-size: 18px; text-align: center; color: #555;'>
            Welcome to your personal arcade of love! Complete challenges, earn points, 
            and unlock a special surprise!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Instructions
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background: rgba(255, 209, 220, 0.6); padding: 20px; border-radius: 15px; margin: 10px;'>
            <h3>🎯 How to Play</h3>
            <ul>
                <li>Complete the <b>Relationship Quiz</b> to test your knowledge</li>
                <li>Share memories in the <b>Memory Timeline</b></li>
                <li>Play fun <b>Mini Games</b> (TicTacToe, Memory Match, Reaction)</li>
                <li>Earn points for each activity</li>
                <li>Reach 100+ points to unlock the <b>Secret Letter</b>! 💌</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style='background: rgba(224, 187, 228, 0.6); padding: 20px; border-radius: 15px; margin: 10px;'>
            <h3>📊 Your Progress</h3>
            <ul>
                <li><b>Current Score:</b> {score} points</li>
                <li><b>Level:</b> {level}</li>
                <li><b>Quiz Status:</b> {quiz_status}</li>
                <li><b>Memory Status:</b> {memory_status}</li>
                <li><b>Games Completed:</b> {games_count}/3</li>
            </ul>
        </div>
        """.format(
            score=st.session_state.total_score,
            level=st.session_state.level,
            quiz_status="✅ Completed" if st.session_state.quiz_completed else "⏳ Pending",
            memory_status="✅ Completed" if st.session_state.memory_completed else "⏳ Pending",
            games_count=sum(st.session_state.games_completed.values())
        ), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Call to action
    if st.session_state.total_score < 100:
        st.info(f"💡 You need {100 - st.session_state.total_score} more points to unlock the Secret Letter!")
    else:
        st.success("🎉 Congratulations! You've unlocked the Secret Letter! Check it out in the sidebar!")
    
    # Fun fact or tip
    st.markdown("""
    <div style='background: rgba(191, 234, 245, 0.6); padding: 15px; border-radius: 15px; margin-top: 20px; text-align: center;'>
        <p style='font-size: 16px; color: #555; margin: 0;'>
            💡 <b>Tip:</b> Complete all activities to maximize your score and level up!
        </p>
    </div>
    """, unsafe_allow_html=True)
