import requests
import json

# Zapier webhook URL
ZAPIER_WEBHOOK_URL = "https://hooks.zapier.com/hooks/catch/XXXXXXXXX/YYYYYYYYY/"

# Email details
email_data = {
    "to": "recipient@example.com",
    "subject": "Test Email",
    "body": "This is a test email sent via Zapier's API."
}

# Send email via Zapier API
response = requests.post(ZAPIER_WEBHOOK_URL, json=email_data)
print(response.status_code)
print(response.text)
