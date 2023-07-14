import streamlit as st
import streamlit.components.v1 as components

header = st.container()
body = st.container()
footer = st.container()

with header:
    st.title("Wordle Cheater")
    st.text("Statistical Solver for the Daily Wordle Puzzle")

with body:
    states = [
        {"name": "Grey", "color": "#808080"},
        {"name": "Yellow", "color": "#FFFF00"},
        {"name": "Green", "color": "#00FF00"},
    ]

    # Initialize the current state
    current_state = 0

    # Function to cycle through states
    def cycle_state():
        global current_state
        current_state = (current_state + 1) % len(states)

    # Create a button to cycle through states
    if st.button("Click me!"):
        cycle_state()

    # Get the current state and corresponding color
    selected_state = states[current_state]["name"]
    selected_color = states[current_state]["color"]

    # Apply CSS to display the color
    colored_checkbox = f'<div style="background-color: {selected_color}; padding: 10px;">{selected_state}</div>'
    st.markdown(colored_checkbox, unsafe_allow_html=True)
