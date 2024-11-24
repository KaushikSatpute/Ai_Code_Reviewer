import time
import streamlit as st
import google.generativeai as genai

# Key setup
genai.configure(api_key="AIzaSyAqkwl-QvabZg9yuE_PrihEe6xhn0jpVTs")

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# System Prompt
sys_prompt = """
You are An AI Code Reviewer, an expert AI Python Code Reviewer. Review and Analyze submitted Python code and provide:
1. ## 🐞 Bug Report: Identify potential bugs, syntax errors and logical flaws in the code. Provide concise explanations for each issue in the form of a clear, numbered list.
2. ## 🛠️ Fixed Code: Provide corrected or optimized code snippets, along with explanations of the changes made.
3. ## 💡 Code Insights: Offer clear, concise, and helpful feedback suitable for developers with various levels of experience; in the form of a clear, numbered list.  
Keep the tone professional and the explanations straightforward, aiming for clarity, accuracy, and enhancing the user's understanding of good coding practices.
"""

# Function - To get response
def get_response(sys_prompt, code_input):
    response = model.generate_content([sys_prompt, code_input])
    return response.text

# Frontend part
# Set up the page configuration
st.set_page_config(
    page_title="AI Code Reviewer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Page Header with Style
st.markdown(
    """
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
        }
        .header {
            text-align: center;
            font-size: 2.5em;
            color: #1a73e8;
            margin-bottom: 0.5em;
        }
        .subheader {
            text-align: center;
            font-size: 1.2em;
            color: #4a4a4a;
            margin-bottom: 1.5em;
        }
        .stTextInput > label {
            font-weight: bold;
            color: #333;
        }
        .stButton > button {
            background-color: #1a73e8;
            color: white;
            font-size: 1.1em;
            border-radius: 8px;
            padding: 0.5em 1.5em;
        }
        .stButton > button:hover {
            background-color: #135aba;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='header'>🤖 AI Code Reviewer</div>", unsafe_allow_html=True)
st.markdown("<div class='subheader'>Analyze, fix bugs, and optimize your Python code with AI</div>", unsafe_allow_html=True)

st.markdown("---")

# Intro Section
st.write("### 🔍 How It Works")
st.markdown("""
1. Paste your Python code in the input box below.
2. Click on **Review Code**.
3. Get an in-depth analysis, fixes, and insights instantly!
""")
st.markdown("---")

# Input Section
st.write("#### 📝 Enter Your Code")
code_input = st.text_area(
    "Paste your Python code here: ",
    placeholder="Enter your Python code...",
    height=200,
    label_visibility="collapsed"
)

# Review button
review_button = st.button("💡 Review Code")

if review_button and code_input.strip():
    with st.spinner("Analyzing your code..."):
        time.sleep(2)  # Simulating processing time
        response = get_response(sys_prompt, code_input)
    st.markdown("### 🧾 Review Results")
    st.write(response)
elif review_button:
    st.warning("Please enter some Python code before clicking 'Review Code'.")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; font-size: 0.9em; color: #888;">
        Developed with ❤️ using <strong>Streamlit</strong> and <strong>Generative AI</strong>.
    </div>
    """,
    unsafe_allow_html=True
)
