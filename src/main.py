import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import string

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

# -----------------------------------------------------


class Wordle:
    def __init__(self):
        with open("../data/words.txt", "r") as file:
            words = file.read().splitlines()
            self.words_array = np.array([list(word) for word in words])

        self.alphabet = list(string.ascii_lowercase)
        self.alphabet_dict = {
            letter: index for index, letter in enumerate(self.alphabet)
        }

        if "words_array" not in st.session_state:
            st.session_state["words_array"] = self.words_array

    def score_letters(self):
        self.letter_scores = np.zeros((26, 1))
        for i in range(0, 5):
            scores = []
            for letter in self.alphabet:
                count = np.count_nonzero(
                    st.session_state["words_array"][:, i] == letter
                )
                scores.append(count / len(st.session_state["words_array"]))
            self.letter_scores = np.column_stack((self.letter_scores, scores))
        self.letter_scores = self.letter_scores[:, 1:]
        return self.letter_scores

    @staticmethod
    def has_unique_rows(array):
        for row in array:
            if len(set(row)) == len(row):
                return True
        return False

    @staticmethod
    def remove_non_unique_rows(array):
        avail_list = [row for row in array if len(set(row)) == len(row)]
        return np.array(avail_list)

    def unique_check(self):
        if has_unique_rows(st.session_state["words_array"]) == True:
            self.avail_words = remove_non_unique_rows(st.session_state["words_array"])
        else:
            self.avail_words = st.session_state["words_array"]
        return

    def best_word(self, alphabet_dict):
        word_scores = np.zeros((len(self.avail_words), 5))
        for column in range(0, 5):
            for row in range(0, len(self.avail_words)):
                letter = self.avail_words[row, column]
                index = alphabet_dict[letter]
                word_scores[row, column] += self.letter_scores[index, column]

        word_scores = np.prod(word_scores, axis=1)
        best = np.argmax(word_scores)
        return self.avail_words[best]

    def filter_list(self, letters, colors):
        for key, color in zip(letters, colors):
            if color == "gray":
                st.session_state["words_array"] = st.session_state["words_array"][
                    ~np.any(st.session_state["words_array"] == key, axis=1)
                ]

            if color == "green":
                column = letters.index(key)
                st.session_state["words_array"] = st.session_state["words_array"][
                    st.session_state["words_array"][:, column] == key
                ]

            if color == "yellow":
                column = letters.index(key)
                st.session_state["words_array"] = st.session_state["words_array"][
                    st.session_state["words_array"][:, column] != key
                ]
                st.session_state["words_array"] = st.session_state["words_array"][
                    np.any(st.session_state["words_array"] == key, axis=1)
                ]

    def solve(self, input=None):
        if input is not None:
            self.filter_list(input)
        self.score_letters()
        self.unique_check()
        return self.best_word(self.alphabet_dict)


solver = Wordle()


# ------------------------------------------------------------------------------


with header:
    st.title("Wordle Cheater")
    st.text("Statistical Solver for the Daily Wordle Puzzle")

states = [
    {"name": "gray", "color": "#787c7f"},
    {"name": "yellow", "color": "#c8b653"},
    {"name": "green", "color": "#6ca965"},
]

num_states = len(states)

with body1:
    (
        word1,
        col11,
        col12,
        col13,
        col14,
        col15,
        done1,
    ) = st.columns([2, 1, 1, 1, 1, 1, 2])

    word1.write("")
    word1.write("")
    word1.write("")
    word1.write("")
    word1.write("")
    word1.write("### S A I N T")

    entries_list1 = []
    colors_list1 = []

    # Initialize session states and checkboxes
    for i, col in enumerate([col11, col12, col13, col14, col15], start=1):
        session_state_key = f"body1_current_state{i}"
        checkbox_state_key = f"body1_checkbox_state{i}"
        text_state_key = f"body1_text_state{i}"

        current_state = st.session_state.get(session_state_key, 0)
        checkbox_state = st.session_state.get(checkbox_state_key, False)

        letter1 = col.text_input("", "", 1, key=f"body1_text{i}")

        entries_list1.append(letter1)

        if col.button("", key=f"body1_button{i}"):
            current_state = (current_state + 1) % num_states

        st.session_state[session_state_key] = current_state

        selected_color = states[current_state]["color"]

        colors_list1.append(states[current_state]["name"])

        colored_checkbox = f'<div style="background-color: {selected_color}; width: 66px; height: 40px;"></div>'
        col.markdown(colored_checkbox, unsafe_allow_html=True)

    done1.write("")
    done1.write("")
    done1.write("")
    done1.write("")
    done1.write("")

    if done1.button("Done", key="DoneButton1"):
        if all(item is not "" for item in entries_list1):
            pass

        # put a warning message here later if this is false


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
