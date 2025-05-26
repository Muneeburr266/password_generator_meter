import streamlit as st
import random
import string

# Function to generate a secure password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    selected_chars = []

    if use_digits:
        characters += string.digits
        selected_chars.append(random.choice(string.digits))  

    if use_special:
        characters += string.punctuation
        selected_chars.append(random.choice(string.punctuation))  

    remaining_chars = [random.choice(characters) for _ in range(length - len(selected_chars))]
    final_password = selected_chars + remaining_chars
    random.shuffle(final_password)

    return ''.join(final_password)

# Streamlit UI Configuration
st.set_page_config(page_title="🔐 Secure Password Generator", page_icon="🔑", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
        body {
            background-color: #f4f4f4;
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            border-radius: 10px;
            padding: 8px 15px;
            transition: 0.3s;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
        .password-box {
            font-size: 18px;
            font-weight: bold;
            padding: 12px;
            background-color: #e9ecef;
            border-radius: 10px;
            text-align: center;
            margin: 10px 0;
            border: 2px solid #007bff;
            word-break: break-all;
        }
    </style>
""", unsafe_allow_html=True)

# Title and Input Fields
st.title("🔐 Secure Password Generator")
st.subheader("Generate a strong and secure password in seconds!")

length = st.slider("🔢 Select Password Length", min_value=4, max_value=32, value=12)
use_digits = st.checkbox("✅ Include Digits")
use_special = st.checkbox("🔣 Include Special Characters")

# Generate Password Button
password = ""  # Initialize password variable
if st.button("🔄 Generate Password"):
    password = generate_password(length, use_digits, use_special)

    # Display password in styled box
    st.markdown(f'<div class="password-box">{password}</div>', unsafe_allow_html=True)

# Display password in an input box for easy manual copying
if password:
    st.text_input("🔑 Copy Password", value=password)

st.write("---")
st.write("💡 **Tip:** Use a password manager to securely store your passwords!")
st.write("Made with ❤️ by [Muneeb](https://github.com/Muneeburr266)")
