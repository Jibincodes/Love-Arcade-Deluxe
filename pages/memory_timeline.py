import streamlit as st
from datetime import datetime


def show():
    """Memory timeline to share and record special moments"""
    st.title("📸 Memory Timeline")
    
    st.markdown("""
    <div style='background: rgba(255, 255, 255, 0.8); padding: 20px; border-radius: 15px; margin-bottom: 20px;'>
        <p style='font-size: 16px; color: #555;'>
            Share your favorite memories and special moments! Each memory you add earns you points! 💖
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Initialize memory list in session state
    if "memories" not in st.session_state:
        st.session_state.memories = []
    
    # Check completion status
    if st.session_state.memory_completed:
        st.success(f"✅ Memory Timeline completed! You earned {st.session_state.memory_score} points!")
    
    # Add new memory form
    with st.expander("➕ Add a New Memory", expanded=not st.session_state.memory_completed):
        with st.form("memory_form"):
            memory_title = st.text_input("Memory Title", placeholder="e.g., Our First Date")
            memory_date = st.date_input("Date", datetime.now())
            memory_description = st.text_area("Description", placeholder="Describe this special moment...")
            memory_feeling = st.selectbox("How did it make you feel?", 
                                         ["Happy 😊", "Loved 🥰", "Excited 🤩", "Grateful 🙏", "Romantic 💕"])
            
            submit_memory = st.form_submit_button("Add Memory", use_container_width=True)
            
            if submit_memory:
                if memory_title and memory_description:
                    new_memory = {
                        "title": memory_title,
                        "date": memory_date,
                        "description": memory_description,
                        "feeling": memory_feeling,
                        "timestamp": datetime.now()
                    }
                    st.session_state.memories.append(new_memory)
                    
                    # Award points (10 points per memory, max 50 points)
                    if len(st.session_state.memories) <= 5:
                        points_earned = 10
                        st.session_state.memory_score += points_earned
                        st.session_state.total_score += points_earned
                        
                        # Update level
                        st.session_state.level = (st.session_state.total_score // 50) + 1
                        
                        # Mark as completed after 3 memories
                        if len(st.session_state.memories) >= 3:
                            st.session_state.memory_completed = True
                        
                        st.success(f"Memory added! You earned {points_earned} points! 🎉")
                        st.rerun()
                    else:
                        st.info("Memory added! (Max points reached)")
                        st.rerun()
                else:
                    st.error("Please fill in all fields!")
    
    # Display memories timeline
    if st.session_state.memories:
        st.markdown("### 📖 Your Memory Timeline")
        st.markdown(f"**Total Memories:** {len(st.session_state.memories)}")
        st.markdown("---")
        
        # Sort memories by date (newest first)
        sorted_memories = sorted(st.session_state.memories, 
                                key=lambda x: x['date'], 
                                reverse=True)
        
        for i, memory in enumerate(sorted_memories):
            with st.container():
                col1, col2 = st.columns([1, 4])
                with col1:
                    st.markdown(f"**{memory['date'].strftime('%b %d, %Y')}**")
                    st.markdown(memory['feeling'])
                with col2:
                    st.markdown(f"### {memory['title']}")
                    st.markdown(memory['description'])
                st.markdown("---")
    else:
        st.info("No memories yet! Start adding some special moments! 💝")
    
    # Progress indicator
    if len(st.session_state.memories) < 3:
        st.info(f"💡 Add {3 - len(st.session_state.memories)} more memories to complete this section!")
