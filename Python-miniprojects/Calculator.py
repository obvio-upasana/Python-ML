import streamlit as st
import math

# --- Page and Theme Configuration ---
st.set_page_config(layout="centered", initial_sidebar_state="collapsed")

# Custom CSS for the dark pink and black/white theme.
st.markdown(
    """
    <style>
    .reportview-container {
        background: #1c1c1c;
        color: white;
    }
    .stTextInput>div>div>input {
        background-color: #333333;
        color: white;
        border-radius: 10px;
        border: 2px solid #ff69b4;
        font-size: 24px;
        text-align: right;
        padding: 10px;
    }
    .stButton>button {
        background-color: #ff69b4; /* Dark Pink */
        color: white;
        border-radius: 10px;
        border: none;
        font-size: 20px;
        font-weight: bold;
        padding: 15px 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.2s;
        margin: 5px;
        width: 100%;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        background-color: #ff3399;
    }
    .st-emotion-cache-1ky94j9 {
        padding: 1rem 0rem;
    }
    .main-header {
        color: #ff69b4;
        text-align: center;
        font-size: 40px;
        font-weight: bold;
    }
    .result-display {
        background-color: #333333;
        color: white;
        border-radius: 10px;
        padding: 20px;
        font-size: 30px;
        text-align: right;
        margin-top: 20px;
        min-height: 70px;
        display: flex;
        align-items: center;
        justify-content: flex-end;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<h1 class='main-header'>Pink! Calculator</h1>", unsafe_allow_html=True)

# --- Session State for Calculator Logic ---
# Initialize session state variables to store the current number, operator, and the result.
if 'current_value' not in st.session_state:
    st.session_state.current_value = ""
if 'operand1' not in st.session_state:
    st.session_state.operand1 = None
if 'operator' not in st.session_state:
    st.session_state.operator = None
if 'result' not in st.session_state:
    st.session_state.result = None

# Function to handle button presses.
def on_button_click(label):
    if label.isdigit() or label == ".":
        # Append digits or decimal point to the current value.
        st.session_state.current_value += label
    elif label in [" + ", " -  ", " * ", "/", "**", "%"]:
        # Store the first operand and the operator.
        if st.session_state.current_value:
            try:
                st.session_state.operand1 = float(st.session_state.current_value)
                st.session_state.operator = label
                st.session_state.current_value = ""
            except ValueError:
                st.session_state.result = "Error"
    elif label == "=":
        # calculation.
        if st.session_state.operand1 is not None and st.session_state.operator is not None and st.session_state.current_value:
            try:
                operand2 = float(st.session_state.current_value)
                if st.session_state.operator == " + ":
                    st.session_state.result = st.session_state.operand1 + operand2
                elif st.session_state.operator == "-":
                    st.session_state.result = st.session_state.operand1 - operand2
                elif st.session_state.operator == "*":
                    st.session_state.result = st.session_state.operand1 * operand2
                elif st.session_state.operator == "/":
                    if operand2 == 0:
                        st.session_state.result = "Error: Division by zero"
                    else:
                        st.session_state.result = st.session_state.operand1 / operand2
                elif st.session_state.operator == "**":
                    st.session_state.result = st.session_state.operand1 ** operand2
                elif st.session_state.operator == "%":
                    st.session_state.result = st.session_state.operand1 % operand2
                st.session_state.current_value = str(st.session_state.result)
                st.session_state.operand1 = None
                st.session_state.operator = None
            except ValueError:
                st.session_state.result = "Error"
    elif label == "C":
        # Clear all state.
        st.session_state.current_value = ""
        st.session_state.operand1 = None
        st.session_state.operator = None
        st.session_state.result = None
    elif label == "!":
        # Factorial operation
        if st.session_state.current_value:
            try:
                num = int(st.session_state.current_value)
                if num >= 0:
                    st.session_state.result = math.factorial(num)
                    st.session_state.current_value = str(st.session_state.result)
                else:
                    st.session_state.result = "Error: Factorial of negative number"
            except ValueError:
                st.session_state.result = "Error: Not an integer"

# Display the current value or result.
display_value = st.session_state.result if st.session_state.result is not None else st.session_state.current_value
st.markdown(f"<div class='result-display'>{display_value}</div>", unsafe_allow_html=True)


buttons = [
    ("C", "C", "clear"), ("!", "!", "op"), ("**", "**", "op"), ("/", "/", "op"),
    ("7", "7", "num"), ("8", "8", "num"), ("9", "9", "num"), ("_*_", "*", "op"),
    ("4", "4", "num"), ("5", "5", "num"), ("6", "6", "num"), ("--", "--", "op"),
    ("1", "1", "num"), ("2", "2", "num"), ("3", "3", "num"), ("_+_", "+", "op"),
    ("0", "0", "num"), (".", ".", "op"), ("=", "=", "eq"), ("%", "%", "op")
]

#button grid.
cols = st.columns(4)
for i, (label, value, _type) in enumerate(buttons):
    with cols[i % 4]:
        st.button(label, on_click=on_button_click, args=(value,), key=f"btn_{i}")

