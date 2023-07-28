import streamlit as st
import streamlit.components.v1 as components
import numpy as np
import string
import os


class Wordle:
    def __init__(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        relative_file_path = "../data/words.txt"
        absolute_file_path = os.path.join(current_dir, relative_file_path)
        if os.path.exists(absolute_file_path):
            with open(absolute_file_path, "r") as file:
                words = file.read().splitlines()
                self.words_array = np.array([list(word) for word in words])
        else:
            st.write("File not found:", absolute_file_path)

        self.alphabet = list(string.ascii_lowercase)
        self.alphabet_dict = {
            letter: index for index, letter in enumerate(self.alphabet)
        }

        if "words_array" not in st.session_state:
            st.session_state["words_array"] = self.words_array

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

    def score_letters(self):
        self.letter_scores = np.zeros((26, 1))
        for i in range(0, 5):
            scores = []
            for letter in self.alphabet:
                count = np.count_nonzero(
                    st.session_state["words_array"][:, i] == letter
                )
                if len(st.session_state["words_array"]) == 0:
                    st.error(
                        "Error! No remaining solutions. Information was entered incorrectly, or something went wrong. Please refresh and try again, or create an issue describing the situation if error persists: https://github.com/samson-bakos/Wordle-Assist",
                        icon="🚨",
                    )
                    st.stop()
                scores.append(count / len(st.session_state["words_array"]))
            self.letter_scores = np.column_stack((self.letter_scores, scores))
        self.letter_scores = self.letter_scores[:, 1:]
        return self.letter_scores

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
        for index, (key, color) in enumerate(zip(letters, colors)):
            if color == "gray":
                temp_array = st.session_state["words_array"][
                    ~np.any(st.session_state["words_array"] == key, axis=1)
                ]

                # standard case
                if len(temp_array) != 0:
                    st.session_state["words_array"] = temp_array

                # handle weird edge case
                else:
                    column = index
                    st.session_state["words_array"] = st.session_state["words_array"][
                        st.session_state["words_array"][:, column] != key
                    ]

            if color == "green":
                column = index
                st.session_state["words_array"] = st.session_state["words_array"][
                    st.session_state["words_array"][:, column] == key
                ]

            if color == "yellow":
                column = index
                st.session_state["words_array"] = st.session_state["words_array"][
                    st.session_state["words_array"][:, column] != key
                ]
                st.session_state["words_array"] = st.session_state["words_array"][
                    np.any(st.session_state["words_array"] == key, axis=1)
                ]

    def solve(self, letters=None, colors=None):
        if letters is not None and colors is not None:
            self.filter_list(letters, colors)
        self.score_letters()
        self.unique_check()
        return self.best_word(self.alphabet_dict)


# -----------------------------------------------------


def main():
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

    st.markdown(
        """
        <style>
            section[data-testid="stSidebar"] {
                width: 470px !important; # Set the width to your desired value
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    solver = Wordle()

    for i in range(2, 7):
        var_name = f"recommended{i}"
        if var_name not in st.session_state:
            st.session_state[var_name] = None

    for i in range(2, 7):
        var_name = f"remaining{i}"
        if var_name not in st.session_state:
            st.session_state[var_name] = None

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

        for i in range(5):
            word1.write("")
        word1.write("### S A I N T")
        word1.write(f"Remaining: 2309")

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

        for i in range(5):
            done1.write("")

        if done1.button("Done", key="DoneButton1"):
            if (
                all(item is not "" for item in entries_list1)
                and st.session_state["recommended2"] is None
            ):
                entries_list1 = [
                    item.lower() if isinstance(item, str) else item
                    for item in entries_list1
                ]
                st.session_state["recommended2"] = " ".join(
                    char.upper()
                    for char in solver.solve(letters=entries_list1, colors=colors_list1)
                )
                st.session_state["remaining2"] = len(st.session_state["words_array"])

    with body2:
        (
            word2,
            col21,
            col22,
            col23,
            col24,
            col25,
            done2,
        ) = st.columns([2, 1, 1, 1, 1, 1, 2])

        if st.session_state["recommended2"] is not None:
            for i in range(5):
                word2.write("")
            word2.write(f"### {st.session_state['recommended2']}")
            if st.session_state["remaining2"] is not None:
                word2.write(f"Remaining: {st.session_state['remaining2']}")

        entries_list2 = []
        colors_list2 = []

        # Initialize session states and checkboxes
        for i, col in enumerate([col21, col22, col23, col24, col25], start=1):
            session_state_key = f"body2_current_state{i}"
            checkbox_state_key = f"body2_checkbox_state{i}"
            text_state_key = f"body2_text_state{i}"

            current_state = st.session_state.get(session_state_key, 0)
            checkbox_state = st.session_state.get(checkbox_state_key, False)

            letter2 = col.text_input("", "", 1, key=f"body2_text{i}")

            entries_list2.append(letter2)

            if col.button("", key=f"body2_button{i}"):
                current_state = (current_state + 1) % num_states

            st.session_state[session_state_key] = current_state

            selected_color = states[current_state]["color"]

            colors_list2.append(states[current_state]["name"])

            colored_checkbox = f'<div style="background-color: {selected_color}; width: 66px; height: 40px;"></div>'
            col.markdown(colored_checkbox, unsafe_allow_html=True)

        for i in range(5):
            done2.write("")

        if done2.button("Done", key="DoneButton2"):
            if (
                all(item is not "" for item in entries_list2)
                and st.session_state["recommended2"] is not None
                and st.session_state["recommended3"] is None
            ):
                entries_list2 = [
                    item.lower() if isinstance(item, str) else item
                    for item in entries_list2
                ]
                st.session_state["recommended3"] = " ".join(
                    char.upper()
                    for char in solver.solve(letters=entries_list2, colors=colors_list2)
                )
                st.session_state["remaining3"] = len(st.session_state["words_array"])

    with body3:
        (
            word3,
            col31,
            col32,
            col33,
            col34,
            col35,
            done3,
        ) = st.columns([2, 1, 1, 1, 1, 1, 2])

        if st.session_state["recommended3"] is not None:
            for i in range(5):
                word3.write("")
            word3.write(f"### {st.session_state['recommended3']}")
            if st.session_state["remaining3"] is not None:
                word3.write(f"Remaining: {st.session_state['remaining3']}")

        entries_list3 = []
        colors_list3 = []

        # Initialize session states and checkboxes
        for i, col in enumerate([col31, col32, col33, col34, col35], start=1):
            session_state_key = f"body3_current_state{i}"
            checkbox_state_key = f"body3_checkbox_state{i}"
            text_state_key = f"body3_text_state{i}"

            current_state = st.session_state.get(session_state_key, 0)
            checkbox_state = st.session_state.get(checkbox_state_key, False)

            letter3 = col.text_input("", "", 1, key=f"body3_text{i}")

            entries_list3.append(letter3)

            if col.button("", key=f"body3_button{i}"):
                current_state = (current_state + 1) % num_states

            st.session_state[session_state_key] = current_state

            selected_color = states[current_state]["color"]

            colors_list3.append(states[current_state]["name"])

            colored_checkbox = f'<div style="background-color: {selected_color}; width: 66px; height: 40px;"></div>'
            col.markdown(colored_checkbox, unsafe_allow_html=True)

        for i in range(5):
            done3.write("")

        if done3.button("Done", key="DoneButton3"):
            if (
                all(item is not "" for item in entries_list3)
                and st.session_state["recommended3"] is not None
                and st.session_state["recommended4"] is None
            ):
                entries_list3 = [
                    item.lower() if isinstance(item, str) else item
                    for item in entries_list3
                ]
                st.session_state["recommended4"] = " ".join(
                    char.upper()
                    for char in solver.solve(letters=entries_list3, colors=colors_list3)
                )
                st.session_state["remaining4"] = len(st.session_state["words_array"])

    with body4:
        (
            word4,
            col41,
            col42,
            col43,
            col44,
            col45,
            done4,
        ) = st.columns([2, 1, 1, 1, 1, 1, 2])

        if st.session_state["recommended4"] is not None:
            for i in range(5):
                word4.write("")
            word4.write(f"### {st.session_state['recommended4']}")
            if st.session_state["remaining4"] is not None:
                word4.write(f"Remaining: {st.session_state['remaining4']}")

        entries_list4 = []
        colors_list4 = []

        # Initialize session states and checkboxes
        for i, col in enumerate([col41, col42, col43, col44, col45], start=1):
            session_state_key = f"body4_current_state{i}"
            checkbox_state_key = f"body4_checkbox_state{i}"
            text_state_key = f"body4_text_state{i}"

            current_state = st.session_state.get(session_state_key, 0)
            checkbox_state = st.session_state.get(checkbox_state_key, False)

            letter4 = col.text_input("", "", 1, key=f"body4_text{i}")

            entries_list4.append(letter4)

            if col.button("", key=f"body4_button{i}"):
                current_state = (current_state + 1) % num_states

            st.session_state[session_state_key] = current_state

            selected_color = states[current_state]["color"]

            colors_list4.append(states[current_state]["name"])

            colored_checkbox = f'<div style="background-color: {selected_color}; width: 66px; height: 40px;"></div>'
            col.markdown(colored_checkbox, unsafe_allow_html=True)

        for i in range(5):
            done4.write("")

        if done4.button("Done", key="DoneButton4"):
            if (
                all(item is not "" for item in entries_list4)
                and st.session_state["recommended4"] is not None
                and st.session_state["recommended5"] is None
            ):
                entries_list4 = [
                    item.lower() if isinstance(item, str) else item
                    for item in entries_list4
                ]
                st.session_state["recommended5"] = " ".join(
                    char.upper()
                    for char in solver.solve(letters=entries_list4, colors=colors_list4)
                )
                st.session_state["remaining5"] = len(st.session_state["words_array"])

        with body5:
            (
                word5,
                col51,
                col52,
                col53,
                col54,
                col55,
                done5,
            ) = st.columns([2, 1, 1, 1, 1, 1, 2])

        if st.session_state["recommended5"] is not None:
            for i in range(5):
                word5.write("")
            word5.write(f"### {st.session_state['recommended5']}")
            if st.session_state["remaining5"] is not None:
                word5.write(f"Remaining: {st.session_state['remaining5']}")

        entries_list5 = []
        colors_list5 = []

        # Initialize session states and checkboxes
        for i, col in enumerate([col51, col52, col53, col54, col55], start=1):
            session_state_key = f"body5_current_state{i}"
            checkbox_state_key = f"body5_checkbox_state{i}"
            text_state_key = f"body5_text_state{i}"

            current_state = st.session_state.get(session_state_key, 0)
            checkbox_state = st.session_state.get(checkbox_state_key, False)

            letter5 = col.text_input("", "", 1, key=f"body5_text{i}")

            entries_list5.append(letter5)

            if col.button("", key=f"body5_button{i}"):
                current_state = (current_state + 1) % num_states

            st.session_state[session_state_key] = current_state

            selected_color = states[current_state]["color"]

            colors_list5.append(states[current_state]["name"])

            colored_checkbox = f'<div style="background-color: {selected_color}; width: 66px; height: 40px;"></div>'
            col.markdown(colored_checkbox, unsafe_allow_html=True)

        for i in range(5):
            done5.write("")

        if done5.button("Done", key="DoneButton5"):
            if (
                all(item is not "" for item in entries_list5)
                and st.session_state["recommended5"] is not None
                and st.session_state["recommended6"] is None
            ):
                entries_list5 = [
                    item.lower() if isinstance(item, str) else item
                    for item in entries_list5
                ]
                st.session_state["recommended6"] = " ".join(
                    char.upper()
                    for char in solver.solve(letters=entries_list5, colors=colors_list5)
                )
                st.session_state["remaining6"] = len(st.session_state["words_array"])

        with body6:
            (
                word6,
                col61,
                col62,
                col63,
                col64,
                col65,
                done6,
            ) = st.columns([2, 1, 1, 1, 1, 1, 2])

        if st.session_state["recommended6"] is not None:
            for i in range(5):
                word5.write("")
            word5.write(f"### {st.session_state['recommended6']}")
            if st.session_state["remaining5"] is not None:
                word5.write(f"Remaining: {st.session_state['remaining6']}")

    with st.sidebar:
        st.header("About and Usage")
        st.write(
            "Welcome to Wordle Cheater. This solver can be used to suggest the best word based on guesses you have already made, or solve the puzzle in the fewest number of steps (on average)."
        )
        st.write(
            "1. Load up a wordle puzzle in another tab, and either guess a word or use the suggested word."
        )
        st.write(
            "2. Enter the word you guessed in the text entry box of the first row, and use the buttons to select the corresponding colors."
        )
        st.write(
            "3. Click the 'Done' button when you are finished. A new word will be suggested, along with the remaining number of possible solutions. Use this word, or a different word of your choice."
        )
        st.write(
            "4. Repeat until the puzzle is solved! If you make a mistake, the first button below will reset the session, but keep your text/color entries."
        )
        if st.sidebar.button("Reset"):
            for key in st.session_state.keys():
                del st.session_state[key]
            st.experimental_rerun()


if __name__ == "__main__":
    main()
