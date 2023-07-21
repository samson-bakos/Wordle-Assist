import streamlit as st
import streamlit.components.v1 as components

header = st.container()
body1 = st.container()
body2 = st.container()
body3 = st.container()
body4 = st.container()
body5 = st.container()
body6 = st.container()

st.markdown(
    """
    <style>
    .stButton>button {
        width: 100%;
        box-sizing: border-box;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


with header:
    st.title("Wordle Cheater")
    st.text("Statistical Solver for the Daily Wordle Puzzle")

states = [
    {"name": "Grey", "color": "#808080"},
    {"name": "Yellow", "color": "#FFFF00"},
    {"name": "Green", "color": "#00FF00"},
]

num_states = len(states)

with body1:
    (
        fill1,
        fill2,
        col11,
        col12,
        col13,
        col14,
        col15,
        fill3,
        fill4,
    ) = st.columns(9)

    # Initialize session states and checkboxes
    for i, col in enumerate([col11, col12, col13, col14, col15], start=1):
        session_state_key = f"body1_current_state{i}"
        checkbox_state_key = f"body1_checkbox_state{i}"
        text_state_key = f"body1_text_state{i}"

        current_state = st.session_state.get(session_state_key, 0)
        checkbox_state = st.session_state.get(checkbox_state_key, False)

        letter1 = col.text_input("", "", 1, key=f"body1_text{i}")

        if col.button("", key=f"body1_button{i}"):
            current_state = (current_state + 1) % num_states

        st.session_state[session_state_key] = current_state

        selected_color = states[current_state]["color"]

        colored_checkbox = f'<div style="background-color: {selected_color}; width: 66px; height: 40px;"></div>'
        col.markdown(colored_checkbox, unsafe_allow_html=True)

with body2:
    fill21, fill22, col21, col22, col23, col24, col25, fill23, fill24 = st.columns(9)

    # Initialize session states and checkboxes
    for i, col in enumerate([col21, col22, col23, col24, col25], start=1):
        session_state_key = f"body2_current_state{i}"
        checkbox_state_key = f"body2_checkbox_state{i}"
        text_state_key = f"body2_text_state{i}"

        current_state = st.session_state.get(session_state_key, 0)
        checkbox_state = st.session_state.get(checkbox_state_key, False)

        letter2 = col.text_input("", "", 1, key=f"body2_text{i}")

        if col.button("", key=f"body2_button{i}"):
            current_state = (current_state + 1) % num_states

        st.session_state[session_state_key] = current_state

        selected_color = states[current_state]["color"]

        colored_checkbox = f'<div style="background-color: {selected_color}; width: 66px; height: 40px;"></div>'
        col.markdown(colored_checkbox, unsafe_allow_html=True)

with body3:
    fill31, fill32, col31, col32, col33, col34, col35, fill33, fill34 = st.columns(9)

    # Initialize session states and checkboxes
    for i, col in enumerate([col31, col32, col33, col34, col35], start=1):
        session_state_key = f"body3_current_state{i}"
        checkbox_state_key = f"body3_checkbox_state{i}"
        text_state_key = f"body3_text_state{i}"

        current_state = st.session_state.get(session_state_key, 0)
        checkbox_state = st.session_state.get(checkbox_state_key, False)

        letter3 = col.text_input("", "", 1, key=f"body3_text{i}")

        if col.button("", key=f"body3_button{i}"):
            current_state = (current_state + 1) % num_states

        st.session_state[session_state_key] = current_state

        selected_color = states[current_state]["color"]

        colored_checkbox = f'<div style="background-color: {selected_color}; width: 66px; height: 40px;"></div>'
        col.markdown(colored_checkbox, unsafe_allow_html=True)

with body4:
    fill41, fill42, col41, col42, col43, col44, col45, fill43, fill44 = st.columns(9)

    # Initialize session states and checkboxes
    for i, col in enumerate([col41, col42, col43, col44, col45], start=1):
        session_state_key = f"body4_current_state{i}"
        checkbox_state_key = f"body4_checkbox_state{i}"
        text_state_key = f"body4_text_state{i}"

        current_state = st.session_state.get(session_state_key, 0)
        checkbox_state = st.session_state.get(checkbox_state_key, False)

        letter4 = col.text_input("", "", 1, key=f"body4_text{i}")

        if col.button("", key=f"body4_button{i}"):
            current_state = (current_state + 1) % num_states

        st.session_state[session_state_key] = current_state

        selected_color = states[current_state]["color"]

        colored_checkbox = f'<div style="background-color: {selected_color}; width: 66px; height: 40px;"></div>'
        col.markdown(colored_checkbox, unsafe_allow_html=True)

    with body5:
        fill51, fill52, col51, col52, col53, col54, col55, fill53, fill54 = st.columns(
            9
        )

        # Initialize session states and checkboxes
        for i, col in enumerate([col51, col52, col53, col54, col55], start=1):
            session_state_key = f"body5_current_state{i}"
            checkbox_state_key = f"body5_checkbox_state{i}"
            text_state_key = f"body5_text_state{i}"

            current_state = st.session_state.get(session_state_key, 0)
            checkbox_state = st.session_state.get(checkbox_state_key, False)

            letter5 = col.text_input("", "", 1, key=f"body5_text{i}")

            if col.button("", key=f"body5_button{i}"):
                current_state = (current_state + 1) % num_states

            st.session_state[session_state_key] = current_state

            selected_color = states[current_state]["color"]

            colored_checkbox = f'<div style="background-color: {selected_color}; width: 66px; height: 40px;"></div>'
            col.markdown(colored_checkbox, unsafe_allow_html=True)

    with body6:
        fill61, fill62, col61, col62, col63, col64, col65, fill63, fill64 = st.columns(
            9
        )

        # Initialize session states and checkboxes
        for i, col in enumerate([col61, col62, col63, col64, col65], start=1):
            session_state_key = f"body6_current_state{i}"
            checkbox_state_key = f"body6_checkbox_state{i}"
            text_state_key = f"body6_text_state{i}"

            current_state = st.session_state.get(session_state_key, 0)
            checkbox_state = st.session_state.get(checkbox_state_key, False)

            letter6 = col.text_input("", "", 1, key=f"body6_text{i}")

            if col.button("", key=f"body6_button{i}"):
                current_state = (current_state + 1) % num_states

            st.session_state[session_state_key] = current_state

            selected_color = states[current_state]["color"]

            colored_checkbox = f'<div style="background-color: {selected_color}; width: 66px; height: 40px;"></div>'
            col.markdown(colored_checkbox, unsafe_allow_html=True)

    st.sidebar.header("Recommended Word:")
