import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import sender_email, sender_password, recipient_emails

def send_email(subject, html_body):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ', '.join(recipient_emails)
    msg['Subject'] = subject
    msg.attach(MIMEText(html_body, 'html'))

    # Connect to the SMTP server
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(sender_email, sender_password)
        server.sendmail(
            sender_email, recipient_emails, msg.as_string()
        )