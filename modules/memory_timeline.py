import streamlit as st
from datetime import datetime
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from .ui_components import render_page_header, render_card, render_progress_card, render_section_divider
except ImportError:
    # Fallback for Streamlit Cloud
    import importlib.util
    ui_components_path = os.path.join(os.path.dirname(__file__), "ui_components.py")
    spec = importlib.util.spec_from_file_location("ui_components", ui_components_path)
    ui_components = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ui_components)

    render_page_header = ui_components.render_page_header
    render_card = ui_components.render_card
    render_progress_card = ui_components.render_progress_card
    render_section_divider = ui_components.render_section_divider


def show():
    """Memory timeline to share and record special moments"""

    # Page header
    render_page_header(
        title="Memory Timeline",
        subtitle="Share your favorite memories and special moments! Each memory earns you points! 💖",
        icon="📸"
    )

    # Initialize memory list in session state
    if "memories" not in st.session_state:
        st.session_state.memories = []
    
    # Progress card
    memories_count = len(st.session_state.memories)
    render_progress_card("Memories Added", min(memories_count, 5), 5, "📝")

    # Check completion status
    if st.session_state.memory_completed:
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #E8F8E8 0%, rgba(255,255,255,0.95) 100%);
            border: 1px solid #C1F0C1;
            border-radius: 24px;
            padding: 32px;
            box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
            margin-bottom: 24px;
            text-align: center;
        ">
            <div style="font-size: 2.5rem; margin-bottom: 8px;">✨</div>
            <p style="color: #8B4789; font-weight: 600; font-size: 1.1rem; margin: 0;">
                Memory Timeline Completed! You earned {st.session_state.memory_score} points!
            </p>
        </div>
        """, unsafe_allow_html=True)

    render_section_divider()

    # Add new memory form
    st.markdown("""
    <h3 style="color: #8B4789; margin-bottom: 16px;">➕ Add a New Memory</h3>
    """, unsafe_allow_html=True)

    with st.form("memory_form"):
        col1, col2 = st.columns(2)

        with col1:
            memory_title = st.text_input("📝 Memory Title", placeholder="e.g., Our First Date")
            memory_date = st.date_input("📅 Date", datetime.now())

        with col2:
            memory_feeling = st.selectbox(
                "💭 How did it make you feel?",
                ["Happy 😊", "Loved 🥰", "Excited 🤩", "Grateful 🙏", "Romantic 💕"]
            )

        memory_description = st.text_area(
            "✍️ Description",
            placeholder="Describe this special moment...",
            height=120
        )

        submit_memory = st.form_submit_button("💾 Save Memory", use_container_width=True)

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

                    st.success(f"✨ Memory added! You earned {points_earned} points!")
                    st.rerun()
                else:
                    st.info("Memory added! (Max points reached)")
                    st.rerun()
            else:
                st.error("Please fill in all fields!")

    render_section_divider()

    # Display memories timeline
    if st.session_state.memories:
        st.markdown(f"""
        <h3 style="color: #8B4789; margin-bottom: 8px;">📖 Your Memory Timeline</h3>
        <p style="color: #8E7FA0; margin-bottom: 24px;">
            {len(st.session_state.memories)} precious memories saved
        </p>
        """, unsafe_allow_html=True)

        # Sort memories by date (newest first)
        sorted_memories = sorted(
            st.session_state.memories,
            key=lambda x: x['date'],
            reverse=True
        )

        for i, memory in enumerate(sorted_memories):
            st.markdown(f"""
            <div style="
                background: rgba(255, 255, 255, 0.92);
                border: 1px solid rgba(224, 187, 228, 0.2);
                border-radius: 24px;
                padding: 24px;
                box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
                margin-bottom: 16px;
            ">
                <div style="display: flex; gap: 16px;">
                    <div style="
                        min-width: 80px;
                        text-align: center;
                        padding: 12px;
                        background: linear-gradient(135deg, #FFE4EC 0%, #F0E6F4 100%);
                        border-radius: 12px;
                    ">
                        <div style="font-size: 1.5rem; margin-bottom: 4px;">{memory['feeling'].split()[-1]}</div>
                        <div style="font-size: 0.75rem; color: #8E7FA0; font-weight: 500;">
                            {memory['date'].strftime('%b %d')}
                        </div>
                        <div style="font-size: 0.7rem; color: #8E7FA0;">
                            {memory['date'].strftime('%Y')}
                        </div>
                    </div>
                    <div style="flex: 1;">
                        <h4 style="color: #4A3F55; margin: 0 0 8px 0; font-size: 1.1rem;">
                            {memory['title']}
                        </h4>
                        <p style="color: #6B5B7A; margin: 0; line-height: 1.6;">
                            {memory['description']}
                        </p>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="
            background: rgba(255, 255, 255, 0.92);
            border: 1px solid rgba(224, 187, 228, 0.2);
            border-radius: 24px;
            padding: 32px;
            box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
            margin-bottom: 24px;
            text-align: center;
        ">
            <div style="font-size: 3rem; margin-bottom: 16px; opacity: 0.5;">📸</div>
            <p style="color: #8E7FA0; font-size: 1.1rem; margin: 0;">
                No memories yet! Start adding some special moments!
            </p>
        </div>
        """, unsafe_allow_html=True)

    # Progress indicator
    if len(st.session_state.memories) < 3:
        remaining = 3 - len(st.session_state.memories)
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #E8F6FA 0%, rgba(255,255,255,0.95) 100%);
            border: 1px solid #BFEAF5;
            border-radius: 24px;
            padding: 24px;
            box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
            margin-bottom: 24px;
            text-align: center;
        ">
            <span style="color: #6B5B7A;">
                💡 Add <strong>{remaining}</strong> more {'memory' if remaining == 1 else 'memories'} to complete this section!
            </span>
        </div>
        """, unsafe_allow_html=True)
