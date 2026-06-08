# def build_prompt(
#     week,
#     score,
#     status,
#     ratings,
#     pending_topics
# ):

#     return f"""
# You are a technical reviewer.

# Generate internship feedback.

# Week:
# {week}

# Score:
# {score}/10

# Status:
# {status}

# KPI Ratings:
# {ratings}

# Pending Topics:
# {pending_topics}

# Rules:

# 1. Generate exactly 4 sentences.
# 2. Professional tone.
# 3. Mention strengths.
# 4. Mention weaknesses.
# 5. Mention practical performance.
# 6. Mention communication if weak.
# 7. Do not mention KPI numbers.
# """


def build_prompt(
    week,
    score,
    status,
    ratings,
    pending_topics
    ):

    strengths = [
        kpi for kpi, value in ratings.items()
        if value >= 7
    ]

    weaknesses = [
        kpi for kpi, value in ratings.items()
        if value <= 5
    ]

    return f"""

    You are a senior technical reviewer.

    Week: {week}

    Score: {score}
    Status: {status}

    Strong Areas:
    {', '.join(strengths) if strengths else 'None'}

    Weak Areas:
    {', '.join(weaknesses) if weaknesses else 'None'}

    Pending Topics:
    {pending_topics}

    Instructions:

    * Generate 5 to 8 sentences.
    * Write simple English.
    * Feedback must be different based on strengths and weaknesses.
    * Focus mainly on weak areas.
    * If Communication is weak, mention communication improvement.
    * If Practical Coding, Practical Implementation, Feature Completion, Task Execution, ORM Operations, Problem Solving or DSA topics are weak, mention more hands-on practice.
    * If Confidence is weak, mention confidence improvement.
    * If Project Explanation is weak, mention explanation skills.
    * If Code Quality is weak, mention coding standards and clean code.
    * If Testing is weak, mention testing.
    * If Deployment is weak, mention deployment practice.
    * Mention strong areas briefly.
    * Do not mention KPI scores.
    * Do not mention KPI names as a list.
    * Generate a unique review based on the weak and strong areas.

    Generate only the feedback paragraph.
    """
