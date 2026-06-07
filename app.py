import streamlit as st

from data.week_kpis import WEEK_KPIS
from data.advisors import ADVISORS

from prompts.feedback_prompt import build_prompt

from services.review_service import calculate_score
from services.ai_service import generate_feedback
from services.email_service import send_review_email
from services.whatsapp_service import generate_whatsapp_link

st.set_page_config(
    page_title="Intern Review Generator",
    layout="wide"
)

st.title("Intern Review Generator")

# =========================
# Intern Details
# =========================

name = st.text_input("Intern Name")

week = st.selectbox(
    "Week",
    list(WEEK_KPIS.keys())
)

# =========================
# Advisor Selection
# =========================

advisor = st.selectbox(
    "Advisor",
    list(ADVISORS.keys())
)

advisor_email = ADVISORS[advisor]["email"]
advisor_phone = ADVISORS[advisor]["phone"]

st.info(
    f"""
Advisor: {advisor}

Email: {advisor_email}

WhatsApp: {advisor_phone}
"""
)

# =========================
# KPI Ratings
# =========================

ratings = {}

st.subheader("KPI Ratings")

for kpi in WEEK_KPIS[week]:

    ratings[kpi] = st.slider(
        kpi,
        min_value=0,
        max_value=10,
        value=5
    )

# =========================
# Pending Topics
# =========================

pending_topics = st.text_area(
    "Pending Topics",
    height=150,
    key="pending_topics_input"
)

# =========================
# Generate Review
# =========================

if st.button("Generate Review"):

    score, status = calculate_score(
        ratings
    )

    prompt = build_prompt(
        week=week,
        score=score,
        status=status,
        ratings=ratings,
        pending_topics=pending_topics
    )

    feedback = generate_feedback(
        prompt
    )

    st.session_state["name"] = name
    st.session_state["advisor"] = advisor
    st.session_state["advisor_email"] = advisor_email
    st.session_state["advisor_phone"] = advisor_phone
    st.session_state["score"] = score
    st.session_state["status"] = status
    st.session_state["feedback"] = feedback
    st.session_state["pending_topics"] = pending_topics

# =========================
# Generated Review
# =========================

if "feedback" in st.session_state:

    st.divider()

    st.subheader("Generated Review")

    st.write(
        f"**Name:** {st.session_state['name']}"
    )

    st.write(
        f"**Advisor:** {st.session_state['advisor']}"
    )

    st.write(
        f"**Score:** {st.session_state['score']}"
    )

    st.write(
        f"**Status:** {st.session_state['status']}"
    )

    feedback_text = st.text_area(
        "Feedback",
        value=st.session_state["feedback"],
        height=220,
        key="feedback_output"
    )

    pending_text = st.text_area(
        "Pending Topics",
        value=st.session_state["pending_topics"],
        height=150,
        key="pending_topics_output"
    )

    st.session_state["feedback"] = feedback_text
    st.session_state["pending_topics"] = pending_text

    col1, col2 = st.columns(2)

    # =========================
    # Email Button
    # =========================

    with col1:

        if st.button("📧 Send Email"):

            send_review_email(
                recipient_email=st.session_state[
                    "advisor_email"
                ],
                intern_name=st.session_state["name"],
                score=st.session_state["score"],
                status=st.session_state["status"],
                feedback=st.session_state["feedback"],
                pending_topics=st.session_state[
                    "pending_topics"
                ]
            )

            st.success(
                f"Email sent to {st.session_state['advisor_email']}"
            )

    # =========================
    # WhatsApp Button
    # =========================

    with col2:

        whatsapp_url = generate_whatsapp_link(
            phone_number=st.session_state[
                "advisor_phone"
            ],
            intern_name=st.session_state["name"],
            score=st.session_state["score"],
            status=st.session_state["status"],
            feedback=st.session_state["feedback"],
            pending_topics=st.session_state[
                "pending_topics"
            ]
        )

        st.link_button(
            "💬 Send via WhatsApp",
            whatsapp_url
        )