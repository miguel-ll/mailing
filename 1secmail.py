import sec
import sys

def get_email():
	email = sec.generate_email(1)[0]
    print(f"your email address is {email}")
    print("waiting for emails...")
    global email
    idd = sec.id_mailinbox(mail=email)[0]
    subject, email, content = sec.email_content(mail=email,idd=idd,html=False)
    print("-------------------- New Message! --------------------")
    print(f"From: {email}")
    print(f"Subject: {subject}")
    print(f"Message: {content}")
    
while True:
    try:
	    get_email()
	    print("Generating new email address...")
    except(KeyboardInterrupt):
        sys.exit("Goodbye.")
