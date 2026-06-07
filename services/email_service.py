import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()


def send_review_email(
    recipient_email,
    intern_name,
    score,
    status,
    feedback,
    pending_topics,
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

    msg = MIMEText(message)

    msg["Subject"] = f"Performance Review - {intern_name}"
    msg["From"] = os.getenv("EMAIL_USERNAME")
    msg["To"] = recipient_email

    server = smtplib.SMTP(
        os.getenv("EMAIL_HOST"),
        int(os.getenv("EMAIL_PORT"))
    )

    server.starttls()

    server.login(
        os.getenv("EMAIL_USERNAME"),
        os.getenv("EMAIL_PASSWORD")
    )

    server.send_message(msg)
    server.quit()