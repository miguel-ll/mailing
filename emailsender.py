import smtplib
from email.message import EmailMessage
import sys
from os import path

host = "smtp.gmail.com"
port = 587
server = smtplib.SMTP(host, port)
msg = EmailMessage()

if len(sys.argv) < 6:
	sys.exit("Provide the arguments correctly!\nExample: python emailsender.py py@gmail.com python123 receiver@gmail.com subject (your message, in quotation marks)\nIf you want to attach a file, it will be the sixth argument.\nThe fifth argument can also be a text file (it will send what is written inside the file).")

def get_file_type(x):
    return str(x).rsplit('.')[1]

def is_txt(y):
    if path.exists(y) and get_file_type(y) == "txt":
        f = open(y)
        content = f.read()
        f.close()
        return content
    else:
        return y

def add_file(filename):
    if path.exists(str(filename)):
        with open(str(filename), 'rb') as f:
            file_data = f.read()
            file_type = get_file_type(filename)
            msg.add_attachment(file_data, maintype=file_type, subtype=file_type, filename=filename)
    else:
        sys.exit(f"The file {filename} does not exist")

def send_email():
    FROM = str(sys.argv[1])
    PASSWORD = str(sys.argv[2])
    msg["From"] = FROM
    msg["To"] = str(sys.argv[3])
    msg["Subject"] = str(sys.argv[4])
    msg.set_content(is_txt(str(sys.argv[5])))
    if len(sys.argv) > 6:
        for x in range(6, len(sys.argv)):
            add_file(sys.argv[x])
    server.starttls()
    server.login(FROM, PASSWORD)
    server.send_message(msg)
    server.quit()
    print("Email Sent")
try:
    send_email()
except:
    print("Error.\nUse: python emailsender.py py@gmail.com python123 receiver@gmail.com subject (your message, in quotation marks)\nIf you want to attach a file, it will be the sixth argument.\nThe fifth argument can also be a text file (it will send what is written inside the file)")
