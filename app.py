import streamlit as st
import random
import time
from datetime import datetime
from streamlit.components.v1 import html

# List of premium cars with embedded SVG graphics
CARS = {
    "Bentley Bentayga": """
        <svg viewBox="0 0 200 80" xmlns="http://www.w3.org/2000/svg">
            <rect x="30" y="40" width="140" height="25" rx="10" fill="#0f172a"/>
            <rect x="50" y="25" width="100" height="20" rx="5" fill="#0f172a"/>
            <circle cx="60" cy="65" r="15" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
            <circle cx="140" cy="65" r="15" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
            <rect x="75" y="35" width="50" height="15" fill="#475569"/>
        </svg>
    """,
    "Rolls-Royce Phantom": """
        <svg viewBox="0 0 200 80" xmlns="http://www.w3.org/2000/svg">
            <rect x="25" y="40" width="150" height="25" rx="5" fill="#0c4a6e"/>
            <rect x="45" y="20" width="110" height="25" rx="8" fill="#0c4a6e"/>
            <circle cx="55" cy="65" r="15" fill="#0e7490" stroke="#e0f2fe" stroke-width="2"/>
            <circle cx="145" cy="65" r="15" fill="#0e7490" stroke="#e0f2fe" stroke-width="2"/>
            <rect x="70" y="30" width="60" height="15" fill="#0284c7"/>
            <rect x="155" y="35" width="20" height="10" fill="#7dd3fc"/>
        </svg>
    """,
    "Ferrari SF90 Stradale": """
        <svg viewBox="0 0 200 80" xmlns="http://www.w3.org/2000/svg">
            <path d="M30,50 L50,30 L150,30 L170,50 L160,65 L40,65 Z" fill="#dc2626"/>
            <circle cx="60" cy="65" r="15" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
            <circle cx="140" cy="65" r="15" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
            <path d="M60,30 L80,40 L120,40 L140,30" fill="none" stroke="#fef3c7" stroke-width="2"/>
        </svg>
    """,
    "Lamborghini Revuelto": """
        <svg viewBox="0 0 200 80" xmlns="http://www.w3.org/2000/svg">
            <path d="M40,50 L60,30 L140,30 L160,50 L150,65 L50,65 Z" fill="#eab308"/>
            <circle cx="65" cy="65" r="15" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
            <circle cx="135" cy="65" r="15" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
            <path d="M70,30 L80,40 L120,40 L130,30" fill="none" stroke="#1e1b4b" stroke-width="3"/>
        </svg>
    """,
    "Bugatti Chiron": """
        <svg viewBox="0 0 200 80" xmlns="http://www.w3.org/2000/svg">
            <path d="M30,50 L60,25 L140,25 L170,50 L155,65 L45,65 Z" fill="#1e40af"/>
            <circle cx="60" cy="65" r="15" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
            <circle cx="140" cy="65" r="15" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
            <path d="M80,25 L80,50 L120,50 L120,25" fill="#bfdbfe" stroke="#1e3a8a" stroke-width="2"/>
        </svg>
    """,
    "Aston Martin DBS": """
        <svg viewBox="0 0 200 80" xmlns="http://www.w3.org/2000/svg">
            <path d="M35,50 L55,30 L145,30 L165,50 L155,65 L45,65 Z" fill="#064e3b"/>
            <circle cx="60" cy="65" r="15" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
            <circle cx="140" cy="65" r="15" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
            <path d="M65,30 L75,40 L125,40 L135,30" fill="none" stroke="#f0fdfa" stroke-width="2"/>
        </svg>
    """,
    "McLaren 720S": """
        <svg viewBox="0 0 200 80" xmlns="http://www.w3.org/2000/svg">
            <path d="M40,50 L70,25 L130,25 L160,50 L150,65 L50,65 Z" fill="#f97316"/>
            <circle cx="65" cy="65" r="15" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
            <circle cx="135" cy="65" r="15" fill="#1e293b" stroke="#94a3b8" stroke-width="2"/>
            <path d="M75,25 L85,40 L115,40 L125,25" fill="none" stroke="#fff7ed" stroke-width="2"/>
        </svg>
    """
}

def show_car_animation(car_svg, one_time=False):
    """Shows a car animation with the given SVG"""
    animation_code = f"""
    <div id="car-container" style="position: fixed; top: {random.randint(20, 70)}%; left: -200px; z-index: 9999;">
        <div style="width: 200px; height: 100px;">
            {car_svg}
        </div>
    </div>
    
    <script>
        // Log the animation parameters for debugging
        console.log("Animation started, one_time={str(one_time).lower()}");
        
        // Animate car across screen
        const car = document.getElementById('car-container');
        let position = -200;
        const screenWidth = window.innerWidth;
        
        function moveCar() {{
            position += 5;
            car.style.left = position + 'px';
            
            if (position < screenWidth + 200) {{
                requestAnimationFrame(moveCar);
            }} else {{
                car.remove();
                
                // Only reload if this is not a one-time test
                if (!{str(one_time).lower()}) {{
                    // Schedule next animation (using user-defined intervals)
                    const minMs = {st.session_state.min_interval * 60 * 1000};
                    const maxMs = {st.session_state.max_interval * 60 * 1000};
                    const nextInterval = Math.floor(Math.random() * (maxMs - minMs + 1)) + minMs;
                    
                    console.log("Next car in: " + (nextInterval/1000/60).toFixed(1) + " minutes");
                    
                    setTimeout(() => {{
                        window.location.reload();
                    }}, nextInterval);
                }}
            }}
        }}
        
        // Start animation
        requestAnimationFrame(moveCar);
    </script>
    """
    
    html(animation_code, height=0)

def main():
    st.set_page_config(page_title="Luxury Car Motivator", layout="wide")
    
    # Custom CSS to hide Streamlit elements when in animation mode
    st.markdown("""
        <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
        </style>
    """, unsafe_allow_html=True)
    
    # App title and description
    st.title("🚗 Luxury Car Motivator")
    st.write("This app will show your dream car driving across the screen every 40-60 minutes to keep you motivated!")
    
    # Car selection
    selected_car = st.selectbox("Select your dream car:", list(CARS.keys()))
    
    # Interval selection (in minutes)
    min_interval = st.slider("Minimum interval (minutes):", 1, 60, 40)
    max_interval = st.slider("Maximum interval (minutes):", min_interval, 120, 60)
    
    # Test and Start buttons in separate columns
    col1, col2 = st.columns(2)
    
    # Test button
    with col1:
        if st.button("Test This Car"):
            car_svg = CARS[selected_car]
            show_car_animation(car_svg, one_time=True)
            st.success(f"Testing {selected_car} animation. Is this motivating for you?")
    
    # Start button
    with col2:
        if st.button("Start Motivation"):
            st.session_state.motivation_active = True
            st.session_state.selected_car = selected_car
            st.session_state.min_interval = min_interval
            st.session_state.max_interval = max_interval
            st.session_state.last_time = datetime.now().timestamp() - 9999  # Trigger first animation immediately
            st.rerun()  # Changed from st.experimental_rerun()
    
    # Check if motivation is active
    if 'motivation_active' in st.session_state and st.session_state.motivation_active:
        current_time = datetime.now().timestamp()
        
        # If it's time for an animation
        if 'next_animation_time' not in st.session_state:
            # First run - schedule immediately
            st.session_state.next_animation_time = current_time
        
        if current_time >= st.session_state.next_animation_time:
            # Show car animation
            car_svg = CARS[st.session_state.selected_car]
            show_car_animation(car_svg)
            
            # Schedule next animation
            interval_seconds = random.randint(st.session_state.min_interval * 60, st.session_state.max_interval * 60)
            st.session_state.next_animation_time = current_time + interval_seconds
        
        # Show stop button
        if st.button("Stop Motivation"):
            st.session_state.motivation_active = False
            st.rerun()  # Changed from st.experimental_rerun()
        
        # Display status
        if 'next_animation_time' in st.session_state:
            next_time = datetime.fromtimestamp(st.session_state.next_animation_time)
            time_diff = max(0, st.session_state.next_animation_time - current_time)
            minutes = int(time_diff // 60)
            seconds = int(time_diff % 60)
            
            st.info(f"Next car will appear in: {minutes} minutes and {seconds} seconds")
            st.write("Keep this tab open to see your motivation!")
            
            # Add debug information to help with interval issues
            st.write(f"Current settings: {st.session_state.min_interval}-{st.session_state.max_interval} minutes")
            
            # Auto-refresh the page every 30 seconds to update the countdown
            html("""
            <script>
                setTimeout(function() {
                    window.location.reload();
                }, 30000);
            </script>
            """, height=0)

if __name__ == "__main__":
    main()
