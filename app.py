import streamlit as st
import json
import os
import time
import pandas as pd

# Page Config
st.set_page_config(page_title="Zenvesting Live", layout="wide")

# Custom CSS for Premium Look & High Contrast
st.markdown("""
    <style>
    /* Global Styles */
    .stApp {
        background-color: #0e1117 !important;
        color: #ffffff !important;
    }
    
    /* Sidebar Specific Fixes */
    section[data-testid="stSidebar"] {
        background-color: #1a1c23 !important;
        border-right: 1px solid #d4af37;
    }
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    /* Ensure ALL text is white except on buttons */
    .stMarkdown, p, span, label, h1, h2, h3, h4, h5, h6 {
        color: #ffffff !important;
    }
    
    /* Radio Button Fix */
    div[role="radiogroup"] label {
        color: #ffffff !important;
    }
    
    /* Button Styling */
    .stButton>button {
        background-color: #d4af37 !important;
        color: #000000 !important;
        border-radius: 5px;
        font-weight: bold;
        border: none;
    }
    
    /* Quiz & Persona Containers */
    .quiz-container {
        border: 2px solid #d4af37;
        padding: 20px;
        border-radius: 10px;
        background-color: #1a1c23;
        color: #ffffff;
    }
    
    /* Progress Box Styles */
    .progress-box {
        display: inline-block;
        width: 15px;
        height: 15px;
        margin: 2px;
        border-radius: 3px;
        border: 1px solid #333;
    }
    .box-right { background-color: #28a745; }
    .box-wrong { background-color: #dc3545; }
    .box-pending { background-color: #333; }
    </style>
    """, unsafe_allow_html=True)

# File Paths
QUIZ_FILE = "data/quiz.json"
SCORES_FILE = "data/scores.json"

# Helper Functions
def load_json(file_path, default=[]):
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return default
    return default

def save_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def init_files():
    if not os.path.exists("data"):
        os.makedirs("data")
    if not os.path.exists(SCORES_FILE):
        save_json(SCORES_FILE, {})

init_files()

# Sidebar: Identity & Navigation
st.sidebar.title("🏗️ Zenvesting")

# --- AUTHENTICATION ---
if "user_email" not in st.session_state:
    st.session_state.user_email = None

if not st.session_state.user_email:
    st.header("🔐 Welcome to Zenvesting")
    st.write("Please enter your unique ID (email) to start.")
    email_input = st.text_input("ID:")
    if st.button("Enter Portal"):
        if email_input:
            st.session_state.user_email = email_input.strip().lower()
            st.rerun()
    st.stop()

# User is logged in
user_email = st.session_state.user_email
st.sidebar.markdown(f"👤 Investor: **{user_email}**")
if st.sidebar.button("Logout"):
    st.session_state.user_email = None
    for key in list(st.session_state.keys()):
        if key.startswith("answered_"):
            del st.session_state[key]
    st.rerun()

st.sidebar.divider()
mode = st.sidebar.radio("Navigate", ["Take Quiz", "Leaderboard"])

# Load Quiz Data
quiz_data = load_json(QUIZ_FILE)
scores = load_json(SCORES_FILE, {})

# Initialize User Progress if not exists
if user_email not in scores:
    scores[user_email] = {
        "current_index": 0,
        "score": 0,
        "answers": {},
        "completed": False
    }
    save_json(SCORES_FILE, scores)

user_data = scores[user_email]

# --- TAKE QUIZ ---
if mode == "Take Quiz":
    st.header("🔥 Your Journey")
    
    if not quiz_data:
        st.warning("No quiz data found.")
    elif user_data.get("completed", False):
        st.balloons()
        st.markdown("<div class='quiz-container' style='text-align: center;'>", unsafe_allow_html=True)
        st.header("🏆 Completed!")
        st.subheader(f"Final Score: {user_data.get('score', 0)}")
        st.markdown("</div>", unsafe_allow_html=True)
        if st.button("Restart"):
            scores[user_email] = {"current_index": 0, "score": 0, "answers": {}, "completed": False}
            save_json(SCORES_FILE, scores)
            st.rerun()
    else:
        current_idx = user_data.get("current_index", 0)
        total_q = len(quiz_data)
        q = quiz_data[current_idx]
        
        st.progress(current_idx / total_q)
        st.write(f"Question {current_idx + 1} of {total_q}")
        
        st.markdown(f"<div class='quiz-container'><h4>{q['question']}</h4></div>", unsafe_allow_html=True)
        
        answered_key = f"answered_{current_idx}"
        if answered_key not in st.session_state:
            st.session_state[answered_key] = False

        if not st.session_state[answered_key]:
            choice = st.radio("Choose:", q["options"], key=f"radio_{current_idx}")
            if st.button("🚀 Submit"):
                is_correct = choice == q["answer"]
                if is_correct: user_data["score"] += 10
                user_data["answers"][str(current_idx)] = {"choice": choice, "is_correct": is_correct}
                save_json(SCORES_FILE, scores)
                st.session_state[answered_key] = True
                st.rerun()
        else:
            ans = user_data["answers"].get(str(current_idx), {})
            if ans.get("is_correct", False):
                st.success("✅ Correct!")
            else:
                st.error(f"❌ Wrong. Correct: {q['answer']}")
            
            c1, c2 = st.columns(2)
            with c1:
                st.markdown(f"<div style='background-color:#1a1c23; border-left:4px solid #d4af37; padding:10px; color:white;'><b>🏗️ Khan:</b><br><i>{q['explanation']['khan']}</i></div>", unsafe_allow_html=True)
            with c2:
                st.markdown(f"<div style='background-color:#1a1c23; border-left:4px solid #ff4b4b; padding:10px; color:white;'><b>🔥 Zara:</b><br><i>{q['explanation']['zara']}</i></div>", unsafe_allow_html=True)
            
            if st.button("Next ➡️"):
                if current_idx + 1 < total_q: user_data["current_index"] += 1
                else: user_data["completed"] = True
                save_json(SCORES_FILE, scores)
                if answered_key in st.session_state: del st.session_state[answered_key]
                st.rerun()

# --- LEADERBOARD ---
elif mode == "Leaderboard":
    st.header("🏆 Leaderboard & Progress")
    
    if not scores:
        st.write("No scores yet.")
    else:
        # Sort scores by the score value
        sorted_scores = sorted(scores.items(), key=lambda x: x[1].get('score', 0) if isinstance(x[1], dict) else 0, reverse=True)
        
        for name, data in sorted_scores:
            if not isinstance(data, dict): continue
            
            with st.container():
                col1, col2 = st.columns([1, 2])
                with col1:
                    st.write(f"**{name}**")
                    st.write(f"Score: {data.get('score', 0)}")
                with col2:
                    # Generate Red/Green boxes
                    boxes_html = ""
                    for i in range(len(quiz_data)):
                        ans = data.get("answers", {}).get(str(i))
                        if ans is None:
                            status_class = "box-pending"
                        elif isinstance(ans, bool):
                            # Handle legacy boolean data
                            status_class = "box-right" if ans else "box-wrong"
                        elif isinstance(ans, dict):
                            # Handle new dictionary data
                            status_class = "box-right" if ans.get("is_correct", False) else "box-wrong"
                        else:
                            status_class = "box-pending"
                        
                        boxes_html += f"<div class='progress-box {status_class}'></div>"
                    st.markdown(boxes_html, unsafe_allow_html=True)
                st.divider()
        
    if st.button("Refresh Table"):
        st.rerun()
