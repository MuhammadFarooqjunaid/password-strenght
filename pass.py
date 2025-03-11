import streamlit as st
import re

# Page title and description
st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")

st.title("🔒 Password Strength Meter")
st.markdown("""
    <style>
    .main {text-align: center;}
    .stTextInput > label {
        font-size: 18px;
    }
    .stTextInput > div > div > input {
        width: 60% !important;
        margin: auto;
        display: block;
    }
    .stButton button {
        width: 50%;
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        border-radius: 5px;
        margin: auto;
        display: block;
    }
    .stButton button:hover {background-color: #45a049;}
    .stSuccess {color: green;}
    .stInfo {color: orange;}
    .stError {color: red;}
    .stExpander {background-color: #f0f2f6; border-radius: 5px; padding: 10px;}
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    ## Welcome to the Ultimate Password Strength Meter!
    Use this simple tool to check the strength of your password and get suggestions on how to make it stronger.
    We will give you helpful tips to create a **Strong Password** 🔒
""")

# Centered password input box
password = st.text_input("Enter your password", type="password", placeholder="Enter your password here...")

feedback = []
score = 0

if password:
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Uppercase and lowercase check
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase characters.")

    # Digit check
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")

    # Special character check
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (e.g., !@#$%^&*).")

    # Feedback based on score
    if score == 4:
        feedback.append("✅ Your password is strong! Keep it up!")
    elif score == 3:
        feedback.append("🟡 Your password is medium strength. Consider making it stronger.")
    else:
        feedback.append("🔴 Your password is weak. Please make it stronger.")

    # Display feedback
    if feedback:
        st.markdown("##  Improving Password Suggestions")
        for tip in feedback:
            st.write(tip)

        # Progress bar to visualize password strength
        st.markdown("### Password Strength Meter")
        strength_level = score / 4  # Normalize score to a range of 0 to 1
        st.progress(strength_level)

else:
    st.info("Please enter your password to get started.")