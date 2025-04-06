import smtplib
from email.message import EmailMessage

def send_email_alert(data):
    msg = EmailMessage()
    msg.set_content(f"🚨 Emergency!\n\n{data}")
    msg["Subject"] = "Health Emergency Alert"
    msg["From"] = "venkatamahith@gmail.com"
    msg["To"] = "cse21733015@matrusri.edu.in"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("venkatamahith@gmail.com", "kxte cgho lpcr aqsq")
            server.send_message(msg)
            print("✅ Email sent!")
    except Exception as e:
        print("❌ Email failed:", e)
