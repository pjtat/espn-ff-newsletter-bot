import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os
from config import sender_email, sender_password, NEWSLETTER_PERSONALITY_NAME

def send_email(subject, html_body, recipient_emails):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ', '.join(recipient_emails)
        msg['Subject'] = subject

        # Attach the logo with a unique identifier
        logo_path = 'logo.png'
        with open(logo_path, 'rb') as f:
            img_data = f.read()
        image = MIMEImage(img_data, name=os.path.basename(logo_path))
        logo_cid = f'logo_{os.path.getmtime(logo_path)}'  # Use file modification time as part of CID
        image.add_header('Content-ID', f'<{logo_cid}>')
        msg.attach(image)
        
        # Modify html_body to include logo with the unique identifier
        centered_logo_html = f'<div style="text-align: center;"><img src="cid:{logo_cid}" alt="Logo"></div>'

        newsletter_personality_signature = f"Best, <br>{NEWSLETTER_PERSONALITY_NAME}<br>"

        html_body = f'{centered_logo_html}<br>{html_body}<br>{newsletter_personality_signature}'
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