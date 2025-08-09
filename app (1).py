
import streamlit as st
import google.generativeai as genai
import os
import random

# Configure Gemini API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# Page Config
st.set_page_config(page_title="Ozhivukazhiv App", page_icon="🤥", layout="wide")

# Custom Elegant CSS
st.markdown(
    '''
    <style>
        .stApp {
            background: linear-gradient(to bottom right, #00172D, #00498D);
            font-family: 'Segoe UI', sans-serif;
            padding: 2em;
        }
        .main-title {
            font-size: 3em;
            font-weight: bold;
            text-align: center;
            color: #D5F3FE;
        }
        .subtitle {
            text-align: center;
            font-size: 1.2em;
            color: #7f8c8d;
            margin-bottom: 2em;
        }
        .stTextInput > div > div > input {
            background-color: white;
            color: black;
            border-radius: 8px;
            font-size: 16px;
        }
        .stButton button {
            background-color: #34495e;
            color: white;
            font-size: 16px;
            border-radius: 10px;
            padding: 0.6em 1.2em;
            transition: 0.3s;
        }
        .stButton button:hover {
            background-color: #2c3e50;
        }
        .excuse-box {
            background-color: #fff;
            padding: 1em;
            border-radius: 10px;
            margin: 1em 0;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
            color: #2c3e50;
            font-size: 1.1em;
        }
        /* New CSS for white labels */
        [data-baseweb="select"] > div > label,
        [data-baseweb="input"] > div > label {
            color: white !important;
            font-weight: bold;
            font-size: 1.1em;
        }
        .stMarkdown b,
        .stMarkdown strong {
            color: white !important;
        }
    </style>
    ''',
    unsafe_allow_html=True
)

# App title
st.markdown("<div class='main-title'>🏃🏻Ozhivukazhiv App</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Funny excuses at your fingertips 😂</div>", unsafe_allow_html=True)

# Extra features
tone = st.selectbox("🎭 Choose excuse style:", ["Funny", "Sarcastic", "Over-the-top", "Polite"])
language = st.selectbox("🌍 Choose language:", ["English", "Malayalam", "Hindi", "Tamil"])

if "daily_excuse" not in st.session_state:
    st.session_state.daily_excuse = model.generate_content(
        f"Give me the funniest {tone.lower()} excuse in {language}"
    ).text.strip()

st.markdown(f"💡 <b>Excuse of the Day:</b> {st.session_state.daily_excuse}", unsafe_allow_html=True)

# Input
prompt = st.text_input("💡 Enter that kayyinn poya situation (or leave blank for a surprise):")

# Button action
if st.button("✨ Generate Excuses"):
    with st.spinner("Cooking up some hilarious excuses...🍳"):
        if not prompt.strip():
            prompt = random.choice([
                "Why I didn't do my homework",
                "Why I was late to work",
                "Why I missed the party",
                "Why I forgot my friend's birthday"
            ])
        
        response = model.generate_content(
            f"Give me 3 very short {tone.lower()} excuses in {language} for: {prompt}"
        )
        excuses = response.text.strip().split("\n")

        for excuse in excuses:
            if excuse.strip():
                st.markdown(f"<div class='excuse-box'>{excuse.strip()}</div>", unsafe_allow_html=True)

        # Copy to clipboard feature
        st.code("Tip: Double click the text above to copy easily!", language="")
