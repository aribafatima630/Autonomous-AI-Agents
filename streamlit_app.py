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


# ---------------- CUSTOM STYLE ----------------
st.markdown(
    """
<style>

body {
    background-color: #0E1117;
}

.main-title {
    font-size:40px;
    font-weight:700;
    color:#E6E8EF;
}

.subtitle {
    color:#9CA3AF;
}

.result-card {
    background:#161B22;
    padding:20px;
    border-radius:12px;
    margin-top:10px;
    border:1px solid #30363D;
}

.final-answer {
    background:linear-gradient(180deg,#141A24,#0E1117);
    padding:30px;
    border-radius:14px;
    border:1px solid #2A3142;
    font-size:18px;
}

.stButton>button {
    background: linear-gradient(90deg,#7C5CFF,#4F8BFF);
    color:white;
    border:none;
    padding:12px 20px;
    border-radius:10px;
    font-weight:600;
}

</style>
""",
    unsafe_allow_html=True,
)

# ---------------- HEADER ----------------
st.markdown('<div class="main-title">🧠 Deep Research AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Autonomous multi-agent research system powered by LangGraph</div>', unsafe_allow_html=True)

st.divider()

# ---------------- INPUT ----------------
goal = st.text_area(
    "Research Question",
    placeholder="Ask a deep research question...",
    height=120
)

max_iteration = st.slider(
    "Max Critic Iterations",
    1,
    5,
    3
)

run_btn = st.button("Run Deep Research")


# ---------------- AGENT TIMELINE ----------------
timeline = st.empty()


# ---------------- RUN AGENT ----------------
if run_btn and goal:

    timeline.info("🧠 Planner analyzing research goal...")
    time.sleep(0.8)

    timeline.info("🔎 Researcher gathering knowledge...")
    time.sleep(0.8)

    timeline.info("✍️ Writer drafting response...")
    time.sleep(0.8)

    timeline.info("🧪 Critic evaluating answer...")
    time.sleep(0.8)

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

    # ---------------- OPTIONAL DETAILS ----------------
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
    st.info("Enter a research question and click **Run Deep Research**")