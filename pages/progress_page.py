import streamlit as st


def show():
    """Progress page showing stats, achievements, and progress bars"""
    st.title("📊 Your Progress")
    
    st.markdown("""
    <div style='background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 15px; margin-bottom: 20px;'>
        <p style='font-size: 16px; color: #555;'>
            Track your progress and achievements! 🎯
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Overall stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Score", st.session_state.total_score, delta=None)
    
    with col2:
        st.metric("Current Level", st.session_state.level)
    
    with col3:
        completed_activities = (
            int(st.session_state.quiz_completed) +
            int(st.session_state.memory_completed) +
            sum(st.session_state.games_completed.values())
        )
        st.metric("Activities Completed", f"{completed_activities}/5")
    
    with col4:
        completion_percentage = (completed_activities / 5) * 100
        st.metric("Completion", f"{completion_percentage:.0f}%")
    
    st.markdown("---")
    
    # Overall progress bar
    st.subheader("🎯 Overall Progress")
    overall_progress = min(st.session_state.total_score / 150, 1.0)  # 150 is max expected score
    st.progress(overall_progress)
    st.write(f"Progress to maximum score: {int(overall_progress * 100)}%")
    
    st.markdown("---")
    
    # Detailed breakdown
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Score Breakdown")
        
        # Quiz score
        st.markdown("**💑 Relationship Quiz**")
        if st.session_state.quiz_completed:
            st.success(f"✅ Completed - {st.session_state.quiz_score} points")
        else:
            st.warning("⏳ Not completed - 0 points")
        
        # Memory score
        st.markdown("**📸 Memory Timeline**")
        if st.session_state.memory_completed:
            st.success(f"✅ Completed - {st.session_state.memory_score} points")
        else:
            st.info(f"⏳ In Progress - {st.session_state.memory_score} points")
        
        # Game scores
        st.markdown("**🎮 Mini Games**")
        for game_name, completed in st.session_state.games_completed.items():
            game_display_names = {
                "tictactoe": "TicTacToe",
                "memory_match": "Memory Match",
                "reaction": "Reaction Game"
            }
            display_name = game_display_names.get(game_name, game_name)
            
            if completed:
                st.success(f"✅ {display_name} - {st.session_state.game_scores[game_name]} points")
            else:
                st.warning(f"⏳ {display_name} - Not completed")
    
    with col2:
        st.subheader("🏆 Achievements")
        
        achievements = []
        
        # Define achievements
        if st.session_state.total_score >= 50:
            achievements.append({"name": "🌟 Beginner", "desc": "Earned 50+ points"})
        
        if st.session_state.total_score >= 100:
            achievements.append({"name": "⭐ Expert", "desc": "Earned 100+ points"})
        
        if st.session_state.quiz_completed:
            achievements.append({"name": "🧠 Quiz Master", "desc": "Completed the relationship quiz"})
        
        if st.session_state.memory_completed:
            achievements.append({"name": "📸 Memory Keeper", "desc": "Added memories to timeline"})
        
        if all(st.session_state.games_completed.values()):
            achievements.append({"name": "🎮 Game Champion", "desc": "Completed all mini games"})
        
        if st.session_state.letter_unlocked:
            achievements.append({"name": "💌 Letter Unlocker", "desc": "Unlocked the secret letter"})
        
        if st.session_state.level >= 3:
            achievements.append({"name": "🚀 Level 3+", "desc": "Reached level 3 or higher"})
        
        # Display achievements
        if achievements:
            for achievement in achievements:
                st.markdown(f"""
                <div style='background: rgba(255, 215, 0, 0.2); padding: 15px; 
                            border-radius: 10px; margin: 10px 0; border: 2px solid #FFD700;'>
                    <b>{achievement['name']}</b><br>
                    <small>{achievement['desc']}</small>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.info("Complete activities to unlock achievements!")
    
    st.markdown("---")
    
    # Next goals
    st.subheader("🎯 Next Goals")
    
    goals = []
    
    if not st.session_state.quiz_completed:
        goals.append("Complete the Relationship Quiz")
    
    if not st.session_state.memory_completed:
        goals.append("Add at least 3 memories to the timeline")
    
    for game_name, completed in st.session_state.games_completed.items():
        if not completed:
            game_display_names = {
                "tictactoe": "TicTacToe",
                "memory_match": "Memory Match",
                "reaction": "Reaction Game"
            }
            goals.append(f"Complete {game_display_names.get(game_name, game_name)}")
    
    if st.session_state.total_score < 100:
        goals.append(f"Earn {100 - st.session_state.total_score} more points to unlock the Secret Letter")
    
    if not st.session_state.letter_unlocked:
        goals.append("Unlock the Secret Letter by meeting all requirements")
    
    if goals:
        for i, goal in enumerate(goals, 1):
            st.markdown(f"{i}. {goal}")
    else:
        st.success("🎉 Congratulations! You've completed everything!")
    
    st.markdown("---")
    
    # Level progress
    st.subheader("📊 Level Progress")
    current_level_threshold = (st.session_state.level - 1) * 50
    next_level_threshold = st.session_state.level * 50
    points_in_level = st.session_state.total_score - current_level_threshold
    points_needed = next_level_threshold - current_level_threshold
    
    level_progress = points_in_level / points_needed if points_needed > 0 else 1.0
    st.progress(level_progress)
    st.write(f"Level {st.session_state.level}: {points_in_level}/{points_needed} points to next level")
