# app.py
import streamlit as st
import random
import time
from datetime import datetime
from streamlit.components.v1 import html

# Embedded SVG car graphics (Bentley, Porsche, etc.)
CAR_SVGS = {
    "Bentley Bentayga": """<svg viewBox="0 0 100 40"><path d="M10 20 L30 20 L35 15 L65 15 L70 20 L90 20 L85 25 L15 25 Z" fill="#15803d"/><circle cx="25" cy="30" r="5" fill="black"/><circle cx="75" cy="30" r="5" fill="black"/></svg>""",
    "Rolls-Royce Phantom": """<svg viewBox="0 0 100 40"><path d="M15 18 L35 18 L40 12 L60 12 L65 18 L85 18 L80 25 L20 25 Z" fill="#0ea5e9"/><rect x="30" y="15" width="40" height="5" fill="#1e3a8a"/><circle cx="30" cy="30" r="5" fill="black"/><circle cx="70" cy="30" r="5" fill="black"/></svg>""",
    "Ferrari SF90": """<svg viewBox="0 0 100 40"><path d="M10 25 L25 15 L75 15 L90 25 L80 30 L20 30 Z" fill="#dc2626"/><path d="M40 15 L60 15 L55 20 L45 20 Z" fill="#facc15"/><circle cx="30" cy="30" r="5" fill="black"/><circle cx="70" cy="30" r="5" fill="black"/></svg>""",
    "Porsche 911": """<svg viewBox="0 0 100 40"><path d="M20 20 L40 15 L60 15 L80 20 L75 25 L25 25 Z" fill="#000000"/><path d="M35 17 L45 17 L50 20 L30 20 Z" fill="#f59e0b"/><circle cx="30" cy="30" r="5" fill="silver"/><circle cx="70" cy="30" r="5" fill="silver"/></svg>"""
}

def car_animation():
    car_name, car_svg = random.choice(list(CAR_SVGS.items()))
    interval = random.randint(2400, 3600)  # 40-60 minutes in seconds
    
    js_code = f"""
    <style>
        @keyframes drive {{
            0% {{ left: -200px; }}
            100% {{ left: 100vw; }}
        }}
        .car {{
            position: fixed;
            top: {random.randint(20, 70)}%;
            animation: drive 8s cubic-bezier(0.25, 0.46, 0.45, 0.94);
            filter: drop-shadow(2px 2px 4px rgba(0,0,0,0.3));
            z-index: 9999;
        }}
    </style>
    
    <div class="car">
        {car_svg}
    </div>
    
    <script>
        // Schedule next animation
        setTimeout(() => window.location.reload(), {interval * 1000});
    </script>
    """
    html(js_code)

st.set_page_config(page_title="Executive Car Motivator", layout="wide")
st.markdown("""
    <style>
        [data-testid="stToolbar"] {{ display: none; }}
        .stApp {{ background: transparent !important; }}
        .stApp > header {{ display: none; }}
    </style>
    """, unsafe_allow_html=True)

# Initial empty container
st.empty()

# First animation
car_animation()
