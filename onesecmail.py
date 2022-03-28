import pyperclip
import requests
import random
import string
import time
import re
import os

API = 'https://www.1secmail.com/api/v1/'
domainList = ['1secmail.com', '1secmail.net', '1secmail.org']
domain = random.choice(domainList)

if os.path.exists("mail_inbox"):
	pass
else:
    print("Creating mail directory....")
    os.mkdir("mail_inbox")

def generateUserName():
    name = string.ascii_lowercase + string.digits
    username = ''.join(random.choice(name) for i in range(10))
    return username

def extract():
    getUserName = re.search(r'login=(.*)&',newMail).group(1)
    getDomain = re.search(r'domain=(.*)', newMail).group(1)
    return [getUserName, getDomain]

def checkMails():
    reqLink = f'{API}?action=getMessages&login={extract()[0]}&domain={extract()[1]}'
    req = requests.get(reqLink).json()
    length = len(req)
    if length == 0:
        print("Your mailbox is empty. Hold tight. Mailbox is refreshed automatically every 5 seconds.\n")
    else:
        idList = []
        for i in req:
            for k,v in i.items():
                if k == 'id':
                    mailId = v
                    idList.append(mailId)

        x = 'mails' if length > 1 else 'mail'
        print(f"You received {length} {x}. (Mailbox is refreshed automatically every 5 seconds.\n)")

        for i in idList:
            msgRead = f'{API}?action=readMessage&login={extract()[0]}&domain={extract()[1]}&id={i}'
            req = requests.get(msgRead).json()
            for k,v in req.items():
                if k == 'from':
                    sender = v
                if k == 'subject':
                    subject = v
                if k == 'date':
                    date = v
                if k == 'textBody':
                    content = v

            mail_cont = f"From: {sender}\nTo: {mail}\nSubject: {subject}\nDate: {date}\nContent: {content}"
            print(mail_cont)
            with open(f"mail_inbox/{i}.txt", 'w') as f:
                f.write(mail_cont)

userInput1 = input("----------------Welcome to 1secmail!----------------\nDo you wish to use to a custom username? (Y/N): ").capitalize()

try:
    if userInput1 == 'Y':
        userInput2 = input("\nEnter the username: ")
        newMail = f"{API}?login={userInput2}&domain={domain}"
        reqMail = requests.get(newMail)
        mail = f"{extract()[0]}@{extract()[1]}"
        pyperclip.copy(mail)
        print("\nYour temporary email is " + mail + " (Email address copied to clipboard.)" +"\n")
        print(f"---------------------------- | Inbox of {mail}| ----------------------------\n")
        while True:
            checkMails()
            time.sleep(5)

    if userInput1 == 'N':
        newMail = f"{API}?login={generateUserName()}&domain={domain}"
        reqMail = requests.get(newMail)
        mail = f"{extract()[0]}@{extract()[1]}"
        pyperclip.copy(mail)
        print("\nYour temporary email is " + mail + " (Email address copied to clipboard.)" + "\n")
        print(f"---------------------------- | Inbox of {mail} | ----------------------------\n")
        while True:
            checkMails()
            time.sleep(5)

except(KeyboardInterrupt):
    opts = input("\nDelete mails? (Y/N): ").capitalize()
    if opts == 'Y':
        files = os.listdir("mail_inbox")
        for file in files:
            file_path = os.path.join("mail_inbox", file)
            os.unlink(file_path)
        os.rmdir("mail_inbox")
        print("\nAll mails have been deleted.")
    print("\nGoodbye.")