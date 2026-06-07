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

    
    return f"""
    You are a senior technical mentor reviewing intern performance.

    Review Details:

    Week: {week}
    Score: {score}/10
    Status: {status}

    KPI Ratings:
    {ratings}

    Pending Topics:
    {pending_topics}

    Instructions:

    * Write feedback in simple and easy-to-understand English.
    * Write like a technical mentor giving review comments.
    * Generate 5 to 8 sentences.
    * Keep the tone professional and constructive.
    * Focus more on improvement areas than strengths.
    * Mention strengths briefly if present.
    * Mention practical performance if weak.
    * Mention communication if weak.
    * Mention project explanation if weak.
    * Mention task execution if weak.
    * Mention confidence if weak.
    * Mention code quality or coding standards if relevant.
    * Suggest areas that need improvement.
    * Encourage continuous learning and practice.
    * Do not mention KPI names.
    * Do not mention KPI scores.
    * Do not mention percentages.
    * Do not mention pass or fail in the feedback.
    * Do not repeat pending topics as a list.
    * Do not use corporate or HR-style language.
    * Avoid words such as:
    demonstrated,
    showcased,
    exhibited,
    proficiency,
    competency,
    hindered,
    facilitated,
    leveraged,
    utilized,
    exceptional,
    remarkable

    Preferred phrases:

    * Overall performance is good.
    * Overall performance is average.
    * Below average performance.
    * Theory understanding is good.
    * Practical implementation needs improvement.
    * Communication should improve.
    * Project explanation needs improvement.
    * Task execution is slow.
    * More hands-on practice is required.
    * Confidence while answering should improve.
    * Continue learning and practicing.
    * Focus on improving weak areas.
    * Maintain coding standards.
    * Ensure timely completion of tasks.
    * Develop a deeper understanding of the concepts.

    Feedback Examples:

    Example 1:
    Overall performance is average. Theory understanding is satisfactory, but practical implementation needs improvement. Communication and explanation skills should improve further. Task execution is slower than expected and requires better planning. More hands-on practice is required to improve confidence while solving problems. Focus on strengthening weak areas and completing tasks on time. Continue learning and practicing consistently.

    Example 2:
    Good performance overall. Theory and practical understanding are satisfactory. Task execution and project progress are moving in the right direction. Communication can be improved further while explaining implementations. Continue focusing on pending areas and maintain proper coding standards. Also spend more time understanding the tools used in the project.

    Example 3:
    Below average performance. Practical implementation is not satisfactory and requires significant improvement. Communication and problem-solving skills need more practice. Confidence while answering should improve through regular revision and coding exercises. More effort is required to understand the concepts deeply and apply them effectively. Focus on completing the assigned tasks and improving overall consistency.

    Generate only the feedback paragraph.
    """
