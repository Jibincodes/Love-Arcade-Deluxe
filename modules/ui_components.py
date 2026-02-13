"""
Love Arcade Deluxe - UI Components & Theme System
Reusable components with consistent styling
"""
import streamlit as st


# ============================================
# GLOBAL CSS THEME SYSTEM
# ============================================
def load_global_css():
    """Load the complete CSS theme system"""
    st.markdown("""
    <style>
        /* ============================================
           CSS VARIABLES - Design Tokens
           Using 8px spacing scale
        ============================================ */
        :root {
            /* Pastel Color Palette */
            --color-pink-light: #FFE4EC;
            --color-pink: #FFD1DC;
            --color-pink-dark: #F8B4C4;
            --color-purple-light: #F0E6F4;
            --color-purple: #E0BBE4;
            --color-purple-dark: #C9A3D4;
            --color-blue-light: #E8F6FA;
            --color-blue: #BFEAF5;
            --color-blue-dark: #9AD8E8;
            --color-yellow-light: #FFFDF0;
            --color-yellow: #FFF5CC;
            --color-peach: #FFE5D0;
            --color-green-light: #E8F8E8;
            --color-green: #C1F0C1;
            --color-gold: #FFD700;
            
            /* Text Colors */
            --text-primary: #4A3F55;
            --text-secondary: #6B5B7A;
            --text-muted: #8E7FA0;
            --text-accent: #8B4789;
            
            /* Background */
            --bg-primary: linear-gradient(145deg, #FFF0F5 0%, #F8E8FF 50%, #E8F4FF 100%);
            --bg-card: rgba(255, 255, 255, 0.92);
            --bg-card-hover: rgba(255, 255, 255, 0.98);
            
            /* Shadows */
            --shadow-soft: 0 4px 20px rgba(139, 71, 137, 0.08);
            --shadow-medium: 0 8px 32px rgba(139, 71, 137, 0.12);
            --shadow-hover: 0 12px 40px rgba(139, 71, 137, 0.16);
            
            /* Spacing Scale (8px) */
            --space-xs: 4px;
            --space-sm: 8px;
            --space-md: 16px;
            --space-lg: 24px;
            --space-xl: 32px;
            --space-2xl: 48px;
            --space-3xl: 64px;
            
            /* Border Radius */
            --radius-sm: 8px;
            --radius-md: 12px;
            --radius-lg: 16px;
            --radius-xl: 24px;
            --radius-full: 50px;
            
            /* Typography */
            --font-display: 'Segoe UI', system-ui, sans-serif;
            --font-body: 'Segoe UI', system-ui, sans-serif;
            
            /* Transitions */
            --transition-fast: 0.15s ease;
            --transition-normal: 0.25s ease;
            --transition-slow: 0.4s ease;
        }
        
        /* ============================================
           ANIMATIONS
        ============================================ */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        
        @keyframes pulse {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.02); }
        }
        
        @keyframes shimmer {
            0% { background-position: -200% center; }
            100% { background-position: 200% center; }
        }
        
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-6px); }
        }
        
        @keyframes confetti-fall {
            0% { transform: translateY(-100vh) rotate(0deg); opacity: 1; }
            100% { transform: translateY(100vh) rotate(720deg); opacity: 0; }
        }
        
        @keyframes heartbeat {
            0%, 100% { transform: scale(1); }
            25% { transform: scale(1.1); }
            50% { transform: scale(1); }
            75% { transform: scale(1.1); }
        }
        
        .animate-fade-in {
            animation: fadeIn 0.5s ease forwards;
        }
        
        .animate-fade-in-up {
            animation: fadeInUp 0.6s ease forwards;
        }
        
        .animate-float {
            animation: float 3s ease-in-out infinite;
        }
        
        .animate-pulse {
            animation: pulse 2s ease-in-out infinite;
        }
        
        .animate-heartbeat {
            animation: heartbeat 1.5s ease-in-out infinite;
        }
        
        /* ============================================
           BASE STYLES
        ============================================ */
        .stApp {
            background: var(--bg-primary) !important;
            min-height: 100vh;
        }
        
        /* Hide default streamlit elements for cleaner look */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* Main content area */
        .main .block-container {
            padding: var(--space-xl) var(--space-lg) !important;
            max-width: 1200px !important;
            animation: fadeIn 0.4s ease;
        }
        
        /* ============================================
           TYPOGRAPHY
        ============================================ */
        h1 {
            font-family: var(--font-display) !important;
            font-size: 2.5rem !important;
            font-weight: 700 !important;
            color: var(--text-accent) !important;
            letter-spacing: -0.02em;
            margin-bottom: var(--space-lg) !important;
            text-align: center;
        }
        
        h2 {
            font-family: var(--font-display) !important;
            font-size: 1.75rem !important;
            font-weight: 600 !important;
            color: var(--text-primary) !important;
            margin-bottom: var(--space-md) !important;
        }
        
        h3 {
            font-family: var(--font-display) !important;
            font-size: 1.25rem !important;
            font-weight: 600 !important;
            color: var(--text-secondary) !important;
            margin-bottom: var(--space-sm) !important;
        }
        
        p, li, span {
            font-family: var(--font-body) !important;
            color: var(--text-secondary);
            line-height: 1.6;
        }
        
        /* ============================================
           SIDEBAR STYLING
        ============================================ */
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #FFFFFF 0%, #FFF5F8 50%, #F8F0FF 100%) !important;
            border-right: 1px solid rgba(224, 187, 228, 0.3);
            padding-top: var(--space-lg);
        }
        
        [data-testid="stSidebar"] > div:first-child {
            padding: var(--space-md) var(--space-lg);
        }
        
        /* Sidebar title */
        [data-testid="stSidebar"] h1 {
            font-size: 1.5rem !important;
            text-align: left !important;
            padding-bottom: var(--space-md);
            border-bottom: 2px solid var(--color-purple);
            margin-bottom: var(--space-lg) !important;
        }
        
        /* Sidebar metrics */
        [data-testid="stSidebar"] [data-testid="stMetric"] {
            background: var(--bg-card);
            border-radius: var(--radius-md);
            padding: var(--space-md);
            margin-bottom: var(--space-sm);
            box-shadow: var(--shadow-soft);
            border: 1px solid rgba(224, 187, 228, 0.2);
        }
        
        [data-testid="stSidebar"] [data-testid="stMetricValue"] {
            color: var(--text-accent) !important;
            font-weight: 700 !important;
        }
        
        /* Sidebar radio buttons (navigation) */
        [data-testid="stSidebar"] .stRadio > div {
            gap: var(--space-xs) !important;
        }
        
        [data-testid="stSidebar"] .stRadio label {
            background: transparent !important;
            border-radius: var(--radius-md) !important;
            padding: var(--space-md) var(--space-lg) !important;
            margin: var(--space-xs) 0 !important;
            transition: all var(--transition-normal) !important;
            border: 1px solid transparent !important;
            font-weight: 500 !important;
        }
        
        [data-testid="stSidebar"] .stRadio label:hover {
            background: rgba(255, 209, 220, 0.4) !important;
            border-color: var(--color-pink) !important;
            transform: translateX(4px);
        }
        
        [data-testid="stSidebar"] .stRadio label[data-checked="true"] {
            background: linear-gradient(135deg, var(--color-pink-light) 0%, var(--color-purple-light) 100%) !important;
            border-color: var(--color-purple) !important;
            box-shadow: var(--shadow-soft) !important;
        }
        
        /* ============================================
           BUTTONS
        ============================================ */
        .stButton > button {
            font-family: var(--font-body) !important;
            font-weight: 600 !important;
            font-size: 0.95rem !important;
            border-radius: var(--radius-full) !important;
            border: none !important;
            background: linear-gradient(135deg, var(--color-pink) 0%, var(--color-purple) 100%) !important;
            color: var(--text-primary) !important;
            padding: var(--space-md) var(--space-xl) !important;
            transition: all var(--transition-normal) !important;
            box-shadow: var(--shadow-soft) !important;
            min-height: 48px !important;
        }
        
        .stButton > button:hover {
            transform: translateY(-2px) !important;
            box-shadow: var(--shadow-hover) !important;
            background: linear-gradient(135deg, var(--color-pink-dark) 0%, var(--color-purple-dark) 100%) !important;
        }
        
        .stButton > button:active {
            transform: translateY(0) !important;
            box-shadow: var(--shadow-soft) !important;
        }
        
        .stButton > button:disabled {
            background: linear-gradient(135deg, #E8E8E8 0%, #D8D8D8 100%) !important;
            color: var(--text-muted) !important;
            cursor: not-allowed !important;
            transform: none !important;
        }
        
        /* Primary button variant */
        .stButton > button[kind="primary"] {
            background: linear-gradient(135deg, var(--color-purple) 0%, var(--color-pink) 100%) !important;
        }
        
        /* ============================================
           FORM INPUTS
        ============================================ */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > div,
        .stDateInput > div > div > input {
            border-radius: var(--radius-md) !important;
            border: 2px solid rgba(224, 187, 228, 0.4) !important;
            padding: var(--space-md) !important;
            font-family: var(--font-body) !important;
            transition: all var(--transition-fast) !important;
            background: var(--bg-card) !important;
        }
        
        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus,
        .stSelectbox > div > div > div:focus-within {
            border-color: var(--color-purple) !important;
            box-shadow: 0 0 0 3px rgba(224, 187, 228, 0.2) !important;
        }
        
        /* ============================================
           METRICS
        ============================================ */
        [data-testid="stMetric"] {
            background: var(--bg-card) !important;
            border-radius: var(--radius-lg) !important;
            padding: var(--space-lg) !important;
            box-shadow: var(--shadow-soft) !important;
            border: 1px solid rgba(224, 187, 228, 0.15) !important;
            transition: all var(--transition-normal) !important;
        }
        
        [data-testid="stMetric"]:hover {
            box-shadow: var(--shadow-medium) !important;
            transform: translateY(-2px);
        }
        
        [data-testid="stMetricLabel"] {
            color: var(--text-muted) !important;
            font-size: 0.85rem !important;
            font-weight: 500 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.05em !important;
        }
        
        [data-testid="stMetricValue"] {
            color: var(--text-accent) !important;
            font-size: 1.75rem !important;
            font-weight: 700 !important;
        }
        
        /* ============================================
           PROGRESS BAR
        ============================================ */
        .stProgress > div > div {
            background: rgba(224, 187, 228, 0.2) !important;
            border-radius: var(--radius-full) !important;
            height: 12px !important;
        }
        
        .stProgress > div > div > div {
            background: linear-gradient(90deg, 
                var(--color-pink) 0%, 
                var(--color-purple) 50%, 
                var(--color-blue) 100%) !important;
            border-radius: var(--radius-full) !important;
            background-size: 200% 100% !important;
            animation: shimmer 2s linear infinite !important;
        }
        
        /* ============================================
           ALERTS & MESSAGES
        ============================================ */
        .stAlert {
            border-radius: var(--radius-lg) !important;
            border: none !important;
            padding: var(--space-lg) !important;
            animation: fadeInUp 0.4s ease !important;
        }
        
        /* Success */
        .stAlert[data-baseweb="notification"] div[data-testid*="success"],
        .stSuccess {
            background: linear-gradient(135deg, var(--color-green-light) 0%, rgba(193, 240, 193, 0.3) 100%) !important;
            border-left: 4px solid var(--color-green) !important;
        }
        
        /* Info */
        .stAlert[data-baseweb="notification"] div[data-testid*="info"],
        .stInfo {
            background: linear-gradient(135deg, var(--color-blue-light) 0%, rgba(191, 234, 245, 0.3) 100%) !important;
            border-left: 4px solid var(--color-blue) !important;
        }
        
        /* Warning */
        .stAlert[data-baseweb="notification"] div[data-testid*="warning"],
        .stWarning {
            background: linear-gradient(135deg, var(--color-yellow-light) 0%, rgba(255, 245, 204, 0.3) 100%) !important;
            border-left: 4px solid var(--color-yellow) !important;
        }
        
        /* Error */
        .stAlert[data-baseweb="notification"] div[data-testid*="error"],
        .stError {
            background: linear-gradient(135deg, var(--color-pink-light) 0%, rgba(255, 209, 220, 0.3) 100%) !important;
            border-left: 4px solid var(--color-pink-dark) !important;
        }
        
        /* ============================================
           EXPANDER
        ============================================ */
        .streamlit-expanderHeader {
            background: var(--bg-card) !important;
            border-radius: var(--radius-lg) !important;
            border: 1px solid rgba(224, 187, 228, 0.2) !important;
            padding: var(--space-md) var(--space-lg) !important;
            font-weight: 600 !important;
            transition: all var(--transition-normal) !important;
        }
        
        .streamlit-expanderHeader:hover {
            background: var(--bg-card-hover) !important;
            border-color: var(--color-purple) !important;
        }
        
        .streamlit-expanderContent {
            border: 1px solid rgba(224, 187, 228, 0.2) !important;
            border-top: none !important;
            border-radius: 0 0 var(--radius-lg) var(--radius-lg) !important;
            padding: var(--space-lg) !important;
            background: var(--bg-card) !important;
        }
        
        /* ============================================
           RADIO BUTTONS (Quiz)
        ============================================ */
        .stRadio > div {
            gap: var(--space-sm) !important;
        }
        
        .stRadio label {
            background: var(--bg-card) !important;
            border-radius: var(--radius-md) !important;
            padding: var(--space-md) var(--space-lg) !important;
            border: 2px solid rgba(224, 187, 228, 0.2) !important;
            transition: all var(--transition-normal) !important;
            cursor: pointer !important;
        }
        
        .stRadio label:hover {
            border-color: var(--color-purple) !important;
            background: rgba(224, 187, 228, 0.1) !important;
            transform: translateX(4px);
        }
        
        .stRadio label[data-checked="true"] {
            background: linear-gradient(135deg, var(--color-pink-light) 0%, var(--color-purple-light) 100%) !important;
            border-color: var(--color-purple) !important;
        }
        
        /* ============================================
           FORMS
        ============================================ */
        [data-testid="stForm"] {
            background: var(--bg-card) !important;
            border-radius: var(--radius-xl) !important;
            padding: var(--space-xl) !important;
            box-shadow: var(--shadow-soft) !important;
            border: 1px solid rgba(224, 187, 228, 0.15) !important;
        }
        
        /* ============================================
           DIVIDER
        ============================================ */
        hr {
            border: none !important;
            height: 2px !important;
            background: linear-gradient(90deg, 
                transparent 0%, 
                var(--color-purple) 50%, 
                transparent 100%) !important;
            margin: var(--space-xl) 0 !important;
            opacity: 0.3;
        }
        
        /* ============================================
           COLUMNS SPACING
        ============================================ */
        [data-testid="column"] {
            padding: var(--space-sm) !important;
        }
        
        /* ============================================
           MOBILE RESPONSIVE
        ============================================ */
        @media (max-width: 768px) {
            h1 {
                font-size: 1.75rem !important;
            }
            
            h2 {
                font-size: 1.35rem !important;
            }
            
            .main .block-container {
                padding: var(--space-md) var(--space-sm) !important;
            }
            
            [data-testid="stMetric"] {
                padding: var(--space-md) !important;
            }
            
            [data-testid="stMetricValue"] {
                font-size: 1.35rem !important;
            }
        }
    </style>
    """, unsafe_allow_html=True)


# ============================================
# REUSABLE UI COMPONENTS
# ============================================

def render_page_header(title: str, subtitle: str = "", icon: str = ""):
    """Render a styled page header with optional subtitle"""
    header_html = f"""
    <div class="page-header animate-fade-in-up" style="
        text-align: center;
        padding: var(--space-xl) var(--space-lg);
        margin-bottom: var(--space-xl);
        background: linear-gradient(135deg, rgba(255,255,255,0.95) 0%, rgba(248,240,255,0.95) 100%);
        border-radius: var(--radius-xl);
        box-shadow: var(--shadow-medium);
        border: 1px solid rgba(224, 187, 228, 0.2);
    ">
        <div style="font-size: 3rem; margin-bottom: var(--space-sm);" class="animate-float">{icon}</div>
        <h1 style="margin: 0 0 var(--space-sm) 0 !important; font-size: 2rem !important;">{title}</h1>
        <p style="
            color: var(--text-secondary);
            font-size: 1.1rem;
            margin: 0;
            max-width: 500px;
            margin: 0 auto;
        ">{subtitle}</p>
    </div>
    """
    st.markdown(header_html, unsafe_allow_html=True)


def render_card(content: str, variant: str = "default", extra_style: str = ""):
    """Render a styled card component

    Variants: default, pink, purple, blue, success, warning, gold
    """
    variant_styles = {
        "default": "background: rgba(255, 255, 255, 0.92); border-color: rgba(224, 187, 228, 0.2);",
        "pink": "background: linear-gradient(135deg, #FFE4EC 0%, rgba(255,255,255,0.95) 100%); border-color: #FFD1DC;",
        "purple": "background: linear-gradient(135deg, #F0E6F4 0%, rgba(255,255,255,0.95) 100%); border-color: #E0BBE4;",
        "blue": "background: linear-gradient(135deg, #E8F6FA 0%, rgba(255,255,255,0.95) 100%); border-color: #BFEAF5;",
        "success": "background: linear-gradient(135deg, #E8F8E8 0%, rgba(255,255,255,0.95) 100%); border-color: #C1F0C1;",
        "warning": "background: linear-gradient(135deg, #FFFDF0 0%, rgba(255,255,255,0.95) 100%); border-color: #FFF5CC;",
        "gold": "background: linear-gradient(135deg, rgba(255,215,0,0.15) 0%, rgba(255,255,255,0.95) 100%); border-color: #FFD700;",
    }

    style = variant_styles.get(variant, variant_styles["default"])

    card_html = f"""
    <div class="ui-card animate-fade-in-up" style="
        {style}
        border-radius: 24px;
        padding: 32px;
        box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
        border: 1px solid;
        margin-bottom: 24px;
        transition: all 0.25s ease;
        {extra_style}
    ">
        {content}
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)


def render_stat_card(label: str, value: str, icon: str = "", variant: str = "default"):
    """Render a statistics card"""
    variant_colors = {
        "default": "#8B4789",
        "pink": "#E75480",
        "purple": "#8B4789",
        "blue": "#4A90A4",
        "gold": "#DAA520",
    }

    color = variant_colors.get(variant, variant_colors["default"])

    stat_html = f"""
    <div class="stat-card animate-fade-in-up" style="
        background: rgba(255, 255, 255, 0.92);
        border-radius: 16px;
        padding: 24px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
        border: 1px solid rgba(224, 187, 228, 0.15);
        transition: all 0.25s ease;
    ">
        <div style="font-size: 2rem; margin-bottom: 4px;">{icon}</div>
        <div style="
            font-size: 1.75rem;
            font-weight: 700;
            color: {color};
            margin-bottom: 4px;
        ">{value}</div>
        <div style="
            font-size: 0.8rem;
            color: #8E7FA0;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            font-weight: 500;
        ">{label}</div>
    </div>
    """
    st.markdown(stat_html, unsafe_allow_html=True)


def render_badge(text: str, variant: str = "default"):
    """Render a small badge/chip component

    Variants: default, success, warning, info, gold
    """
    variant_styles = {
        "default": "background: #F0E6F4; color: #8B4789;",
        "success": "background: #E8F8E8; color: #2E7D32;",
        "warning": "background: #FFFDF0; color: #F57C00;",
        "info": "background: #E8F6FA; color: #0277BD;",
        "gold": "background: rgba(255,215,0,0.2); color: #DAA520;",
        "pink": "background: #FFE4EC; color: #C2185B;",
    }

    style = variant_styles.get(variant, variant_styles["default"])

    badge_html = f"""
    <span style="
        {style}
        padding: 4px 16px;
        border-radius: 50px;
        font-size: 0.8rem;
        font-weight: 600;
        display: inline-block;
    ">{text}</span>
    """
    return badge_html


def render_achievement_badge(name: str, description: str, unlocked: bool = True):
    """Render an achievement badge"""
    opacity = "1" if unlocked else "0.4"
    bg = "linear-gradient(135deg, rgba(255,215,0,0.2) 0%, rgba(255,245,200,0.3) 100%)" if unlocked else "rgba(200,200,200,0.2)"
    border = "#FFD700" if unlocked else "#ccc"

    badge_html = f"""
    <div class="achievement-badge animate-fade-in-up" style="
        background: {bg};
        border: 2px solid {border};
        border-radius: 16px;
        padding: 16px 24px;
        margin-bottom: 16px;
        opacity: {opacity};
        transition: all 0.25s ease;
    ">
        <div style="font-weight: 600; color: #4A3F55; margin-bottom: 4px;">
            {name}
        </div>
        <div style="font-size: 0.85rem; color: #8E7FA0;">
            {description}
        </div>
    </div>
    """
    st.markdown(badge_html, unsafe_allow_html=True)


def render_progress_card(title: str, current: int, total: int, icon: str = ""):
    """Render a card with progress bar"""
    percentage = min((current / total) * 100, 100) if total > 0 else 0

    progress_html = f"""
    <div class="progress-card animate-fade-in-up" style="
        background: rgba(255, 255, 255, 0.92);
        border-radius: 16px;
        padding: 24px;
        box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
        border: 1px solid rgba(224, 187, 228, 0.15);
        margin-bottom: 16px;
    ">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
            <span style="font-weight: 600; color: #4A3F55;">
                {icon} {title}
            </span>
            <span style="color: #8B4789; font-weight: 700;">
                {current}/{total}
            </span>
        </div>
        <div style="
            background: rgba(224, 187, 228, 0.2);
            border-radius: 50px;
            height: 10px;
            overflow: hidden;
        ">
            <div style="
                background: linear-gradient(90deg, #FFD1DC 0%, #E0BBE4 50%, #BFEAF5 100%);
                height: 100%;
                width: {percentage}%;
                border-radius: 50px;
                transition: width 0.5s ease;
            "></div>
        </div>
    </div>
    """
    st.markdown(progress_html, unsafe_allow_html=True)


def render_game_card(title: str, description: str, icon: str, completed: bool = False, points: int = 0):
    """Render a game selection card"""
    status_badge = render_badge("✓ Completed", "success") if completed else render_badge(f"+{points} pts", "gold")

    card_html = f"""
    <div class="game-card" style="
        background: rgba(255, 255, 255, 0.92);
        border-radius: 24px;
        padding: 32px;
        box-shadow: 0 4px 20px rgba(139, 71, 137, 0.08);
        border: 1px solid rgba(224, 187, 228, 0.15);
        text-align: center;
        transition: all 0.25s ease;
        cursor: pointer;
    ">
        <div style="font-size: 3rem; margin-bottom: 16px;">{icon}</div>
        <h3 style="margin: 0 0 8px 0; color: #4A3F55;">{title}</h3>
        <p style="color: #8E7FA0; font-size: 0.9rem; margin-bottom: 16px;">{description}</p>
        {status_badge}
    </div>
    """
    st.markdown(card_html, unsafe_allow_html=True)


def render_confetti():
    """Render CSS confetti animation for celebrations"""
    confetti_html = """
    <style>
        .confetti-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            overflow: hidden;
            z-index: 9999;
        }
        .confetti {
            position: absolute;
            width: 12px;
            height: 12px;
            animation: confetti-fall 4s ease-out forwards;
        }
    </style>
    <div class="confetti-container">
    """

    colors = ['#FFD1DC', '#E0BBE4', '#BFEAF5', '#FFF5CC', '#C1F0C1', '#FFD700']
    shapes = ['❤️', '💕', '✨', '🎉', '💖', '⭐']

    for i in range(30):
        import random
        left = random.randint(0, 100)
        delay = random.uniform(0, 2)
        shape = random.choice(shapes)
        confetti_html += f"""
        <div class="confetti" style="
            left: {left}%;
            animation-delay: {delay}s;
            font-size: {random.randint(14, 24)}px;
        ">{shape}</div>
        """

    confetti_html += "</div>"
    st.markdown(confetti_html, unsafe_allow_html=True)


def render_level_badge(level: int):
    """Render the current level badge"""
    level_names = {
        1: "Just Getting Started 🌱",
        2: "Memory Master 🧠",
        3: "Arcade Queen 👑",
        4: "Soulmate Mode 💕"
    }

    level_name = level_names.get(min(level, 4), level_names[4])

    badge_html = f"""
    <div class="level-badge animate-pulse" style="
        background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%);
        color: white;
        padding: 8px 24px;
        border-radius: 50px;
        display: inline-block;
        font-weight: 700;
        font-size: 0.9rem;
        box-shadow: 0 4px 15px rgba(255, 215, 0, 0.4);
        text-shadow: 0 1px 2px rgba(0,0,0,0.2);
    ">
        Level {level}: {level_name}
    </div>
    """
    st.markdown(badge_html, unsafe_allow_html=True)


def render_section_divider():
    """Render a decorative section divider"""
    divider_html = """
    <div style="
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 32px 0;
        gap: 16px;
    ">
        <div style="flex: 1; height: 2px; background: linear-gradient(90deg, transparent, #E0BBE4);"></div>
        <span style="color: #E0BBE4; font-size: 1.2rem;">💕</span>
        <div style="flex: 1; height: 2px; background: linear-gradient(90deg, #E0BBE4, transparent);"></div>
    </div>
    """
    st.markdown(divider_html, unsafe_allow_html=True)


def render_checklist_item(text: str, completed: bool):
    """Render a checklist item"""
    icon = "✅" if completed else "⬜"
    opacity = "1" if completed else "0.7"
    strikethrough = "line-through" if completed else "none"

    item_html = f"""
    <div style="
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 8px 0;
        opacity: {opacity};
    ">
        <span style="font-size: 1.2rem;">{icon}</span>
        <span style="text-decoration: {strikethrough}; color: #6B5B7A;">{text}</span>
    </div>
    """
    st.markdown(item_html, unsafe_allow_html=True)


def render_letter_envelope(unlocked: bool = False):
    """Render a decorative envelope for the secret letter"""
    if unlocked:
        envelope_html = """
        <div class="envelope-open animate-fade-in-up" style="
            text-align: center;
            margin-bottom: 32px;
        ">
            <div style="font-size: 5rem;" class="animate-heartbeat">💌</div>
            <div style="
                background: linear-gradient(135deg, #FFE4EC 0%, #F0E6F4 100%);
                padding: 24px 32px;
                border-radius: 24px;
                display: inline-block;
                margin-top: 16px;
            ">
                <span style="
                    color: #8B4789;
                    font-weight: 700;
                    font-size: 1.2rem;
                ">✨ Letter Unlocked! ✨</span>
            </div>
        </div>
        """
    else:
        envelope_html = """
        <div class="envelope-locked animate-fade-in-up" style="
            text-align: center;
            margin-bottom: 32px;
        ">
            <div style="font-size: 5rem; filter: grayscale(30%); opacity: 0.8;">🔒</div>
            <div style="
                background: rgba(200,200,200,0.3);
                padding: 24px 32px;
                border-radius: 24px;
                display: inline-block;
                margin-top: 16px;
            ">
                <span style="
                    color: #8E7FA0;
                    font-weight: 600;
                    font-size: 1.1rem;
                ">Complete challenges to unlock</span>
            </div>
        </div>
        """
    st.markdown(envelope_html, unsafe_allow_html=True)

