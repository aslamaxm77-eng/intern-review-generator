import urllib.parse


def generate_whatsapp_link(
    phone_number,
    intern_name,
    score,
    status,
    feedback,
    pending_topics
):
    message = f"""
Name: {intern_name}

Score: {score}
Status: {status}

Feedback:
{feedback}

Pending Topics:
{pending_topics}
"""

    encoded_message = urllib.parse.quote(message)

    return (
        f"https://wa.me/{phone_number}"
        f"?text={encoded_message}"
    )