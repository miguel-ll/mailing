import requests
from gen import *
from mailtm import Email
import pyperclip

def domains():
    base_url = "https://api.mail.tm/"
    header = {"Accept": "application/json", "Content-Type": "application/json"}
    available_domains = requests.get(base_url + "domains", headers=header).json()
    return available_domains

def listener(message):
    print("---------- New Message! ----------")
    print("\nSubject: " + message['subject'])
    print("Content: " + message['text'] if message['text'] else message['html'])

def main():
    print("Welcome to Temp Mail.")
    get_dom = domains()

    print("\nAvailable domains:", len(get_dom))
    dom_list = list()

    for c in range(len(get_dom)):
        dom_list.append(get_dom[c].get('domain'))
        print(f"\n[ {c} ] {dom_list[c]}\n")

    sel_dom = input("Choose domain key: ")

    try:
        domain_mail = dom_list[int(sel_dom)]
    except:
        print(f"Key 0 will be used.")
        domain_mail = dom_list[0]
    username = input("\nSet username for temp mail (username only, enter for random): ")

    if len(username) == 0:
        username = gen_user()
    password = gen_pass()
    addr = f"{username}@{domain_mail}"
    print(f"Your email address: \nE-Mail: {addr}")
    pyperclip.copy(addr)
    mail(username, password, domain_mail)

def mail(username, password, domain_mail):
    test = Email()
# make new email address
    test.register(username=username, password=password, domain=domain_mail)
# start listening
    test.start(listener, interval=1)
    print("\nWaiting for new emails...")


main()
