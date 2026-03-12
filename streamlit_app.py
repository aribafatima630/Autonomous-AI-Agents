import streamlit as st
from dotenv import load_dotenv
import time

load_dotenv()

from graph import app
from agents.stateSchema import AgentState


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Deep Research AI",
    page_icon="🧠",
    layout="wide"
)


# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

/* background */

body {
background:#F7F7F5;
}

/* center title */

.center-title{
text-align:center;
font-size:45px;
font-weight:600;
color:#202124;
margin-top:120px;
margin-bottom:40px;
margin-left:-120px;
}

/* search box */

.stTextArea textarea{
text-align:center;
background:white;
border-radius:22px;
border:1px solid #E0E0E0;
box-shadow:0 6px 30px rgba(0,0,0,0.08);
font-size:16px;
padding:18px;
}

/* run button */

.stButton>button{
background:#202124;
color:white;
border:none;
border-radius:22px;
padding:6px 18px;
font-size:14px;
margin-top:15px;
float:right;
}

/* cards */

.result-card{
background:white;
padding:18px;
border-radius:14px;
border:1px solid #E0E0E0;
margin-top:10px;
}

/* final answer */

.final-answer{
background:white;
padding:28px;
border-radius:16px;
border:1px solid #E0E0E0;
font-size:18px;
}

</style>
""", unsafe_allow_html=True)


# ---------------- MAIN LAYOUT ----------------

sidebar, main = st.columns([1.3,6])


# ---------------- SIDEBAR ----------------

with sidebar:

    st.markdown("### Controls")

    max_iteration = st.slider(
        "Iterations",
        1,
        5,
        3
    )

    st.write("")
    st.write("")
    st.write("History coming soon...")


# ---------------- MAIN PAGE ----------------

with main:

    st.markdown(
        '<div class="center-title">Deep Research AI</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([2,5,2])

    with col2:

        search_col, button_col = st.columns([9,2])

        with search_col:
            goal = st.text_area(
                "",
                placeholder="Type your research question...",
                height=110
            )

        with button_col:
            st.write("")
            st.write("")
            run_btn = st.button("Run")


# ---------------- TIMELINE ----------------

timeline = st.empty()


# ---------------- RUN AGENT ----------------

if run_btn and goal:

    timeline.info("🧠 Planner analyzing research goal...")
    time.sleep(0.7)

    timeline.info("🔎 Researcher gathering knowledge...")
    time.sleep(0.7)

    timeline.info("✍️ Writer drafting response...")
    time.sleep(0.7)

    timeline.info("🧪 Critic evaluating answer...")
    time.sleep(0.7)

    with st.spinner("Running autonomous research agents..."):

        initial_state: AgentState = {
            "goal": goal,
            "plan": [],
            "research_notes": [],
            "sources": "",
            "draft_answer": "",
            "critic_notes": None,
            "is_approved": False,
            "iteration": 0,
            "max_iteration": max_iteration,
            "final_answer": ""
        }

        result = app.invoke(initial_state)

    timeline.success("✅ Research completed")

    st.divider()

    # ---------------- FINAL ANSWER ----------------

    st.markdown("## Final Answer")

    st.markdown(
        f'<div class="final-answer">{result["final_answer"]}</div>',
        unsafe_allow_html=True
    )

    st.caption(f"Iterations used: {result['iteration']} / {result['max_iteration']}")

    # ---------------- PROCESS ----------------

    with st.expander("🔍 View Research Process"):

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("### Research Plan")

            for step in result["plan"]:
                st.markdown(
                    f'<div class="result-card">• {step}</div>',
                    unsafe_allow_html=True
                )

            st.markdown("### Research Notes")

            for note in result["research_notes"]:
                st.markdown(
                    f'<div class="result-card">{note}</div>',
                    unsafe_allow_html=True
                )

        with col2:

            st.markdown("### Draft Answer")

            st.markdown(
                f'<div class="result-card">{result["draft_answer"]}</div>',
                unsafe_allow_html=True
            )

            st.markdown("### Critic Feedback")

            if result["critic_notes"]:
                st.markdown(
                    f'<div class="result-card">{result["critic_notes"]}</div>',
                    unsafe_allow_html=True
                )

else:

    st.info("Enter a research question and click **Run**")