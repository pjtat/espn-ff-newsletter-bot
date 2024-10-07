import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os
from config import sender_email, sender_password, recipient_emails

def send_email(subject, html_body):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ', '.join(recipient_emails)
        msg['Subject'] = subject

        # Attach the logo
        with open('logo.png', 'rb') as f:
            img_data = f.read()
        image = MIMEImage(img_data, name=os.path.basename('logo.png'))
        image.add_header('Content-ID', '<logo>')
        msg.attach(image)

        # Modify html_body to include the centered logo
        centered_logo_html = '<div style="text-align: center;"><img src="cid:logo" alt="Logo"></div>'
        html_body = f'{centered_logo_html}<br>{html_body}'
        msg.attach(MIMEText(html_body, 'html'))

        # Connect to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)
            server.sendmail(
                sender_email, recipient_emails, msg.as_string()
            )
        return True
    except smtplib.SMTPAuthenticationError:
        print("SMTP Authentication Error: Failed to authenticate with the SMTP server.")
        return False
    except smtplib.SMTPException as e:
        print(f"SMTP Error: An error occurred while sending the email: {str(e)}")
        return False
    except Exception as e:
        print(f"Unexpected Error: An unexpected error occurred: {str(e)}")
        return False