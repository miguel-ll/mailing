import requests as req
import json

def generate_email(n:int = 1):
    first_ = "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count={0}"
    emails_list = json.loads(req.get(first_.format(str(n))).text)

    return emails_list

def id_mailinbox(mail:str):
    login, domain = mail.split("@")
    second_ = f'https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}'
    resp = json.loads(req.get(second_).text)
    while len(resp) == 0:
        resp = json.loads(req.get(second_).text)
    idd = int(resp[0]["id"])
    return idd, resp

def email_content(mail:str,idd:int, html:bool = False):
    login, domain = mail.split("@")
    third_ = f'https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={idd}'
    idd = str(idd)
    response = json.loads(req.get(third_).text)
    sender = response["from"]
    subject = response["subject"]
    if html: content = response["htmlBody"]
    else: content = response["textBody"]
        
    return subject, sender, content
