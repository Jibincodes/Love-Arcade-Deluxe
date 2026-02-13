import streamlit as st


def show():
    """Secret letter that unlocks when requirements are met"""
    st.title("💌 Secret Letter")
    
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
    
    # Display unlock status
    if not st.session_state.letter_unlocked:
        st.markdown("""
        <div style='background: rgba(255, 209, 220, 0.6); padding: 30px; border-radius: 20px; text-align: center;'>
            <h2>🔒 Letter is Locked</h2>
            <p style='font-size: 18px;'>Complete the requirements to unlock this special message!</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📋 Requirements:")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Score Requirements")
            progress = min(st.session_state.total_score / score_requirement, 1.0)
            st.progress(progress)
            st.write(f"Score: {st.session_state.total_score}/{score_requirement}")
            
            if score_met:
                st.success("✅ Score requirement met!")
            else:
                st.warning(f"❌ Need {score_requirement - st.session_state.total_score} more points")
        
        with col2:
            st.markdown("#### Completion Requirements")
            st.write(f"{'✅' if completion_requirements['quiz'] else '❌'} Complete Relationship Quiz")
            st.write(f"{'✅' if completion_requirements['memory'] else '❌'} Complete Memory Timeline")
            st.write(f"{'✅' if completion_requirements['at_least_one_game'] else '❌'} Complete at least one Mini Game")
        
        st.markdown("---")
        st.info("💡 Keep playing to unlock the secret letter! It contains a special message just for you! 💝")
    
    else:
        # Letter is unlocked - show the secret message
        # Show balloons only on first unlock
        if "balloons_shown" not in st.session_state:
            st.session_state.balloons_shown = True
            st.balloons()
        
        st.markdown("""
        <div style='background: linear-gradient(135deg, #FFD1DC 0%, #E0BBE4 100%); 
                    padding: 40px; border-radius: 20px; box-shadow: 0 8px 16px rgba(0,0,0,0.2);
                    border: 3px solid #E0BBE4;'>
            <h2 style='text-align: center; color: #8B4789;'>💌 A Special Message For You 💌</h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # The secret letter content
        st.markdown("""
        <div style='background: rgba(255, 255, 255, 0.9); padding: 30px; border-radius: 15px; 
                    box-shadow: 0 4px 8px rgba(0,0,0,0.1); font-family: cursive;'>
            <p style='font-size: 20px; color: #555; line-height: 1.8;'>
                <b>My Dearest Love,</b><br><br>
                
                If you're reading this, it means you've completed all the challenges! 
                I'm so proud of you! 🎉<br><br>
                
                This little arcade was created especially for you, filled with love and care. 
                Every game, every question, every moment was designed to make you smile 
                and to show you just how much you mean to me. 💕<br><br>
                
                You are my favorite person, my best friend, and my greatest adventure. 
                Thank you for being you, for your laughter, your kindness, and for making 
                every day brighter. ☀️<br><br>
                
                Remember, no matter what challenges come our way, we'll face them together - 
                just like you completed these games! 🎮<br><br>
                
                Keep being amazing, keep smiling, and know that you are loved beyond measure. ❤️<br><br>
                
                <b>Forever yours,</b><br>
                <b>Your Biggest Fan 💝</b>
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Achievement badge
        st.markdown("""
        <div style='background: rgba(255, 215, 0, 0.3); padding: 20px; border-radius: 15px; 
                    text-align: center; border: 2px solid gold;'>
            <h3>🏆 Achievement Unlocked! 🏆</h3>
            <p style='font-size: 18px;'><b>Love Arcade Master</b></p>
            <p>You've completed all challenges and unlocked the secret letter!</p>
        </div>
        """, unsafe_allow_html=True)
