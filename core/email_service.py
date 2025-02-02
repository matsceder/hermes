import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def send_secret_email(recipient_email, secret_url):
    message = Mail(
        from_email=os.getenv("DEFAULT_FROM_EMAIL"),
        to_emails=recipient_email,
        subject="You've received a secure message",
        html_content=f"""
            <p>Someone has shared a secure message with you.</p>
            <p>Click the button below to unlock it:</p>
            <a href="{secret_url}" style="background-color:#007bff;color:white;padding:10px 20px;text-decoration:none;border-radius:5px;">Unlock Secret</a>
            <p>Or copy this link into your browser:</p>
            <p><a href="{secret_url}">{secret_url}</a></p>
        """
    )

    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        response = sg.send(message)
        return response.status_code
    except Exception as e:
        print(f"Error sending email: {e}")
