import smtplib
import time
import imaplib
import email
ORG_EMAIL   = "@gmail.com"
FROM_EMAIL  = "shatheeshrocks" + ORG_EMAIL
FROM_PWD    = "fire01bolt"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT   = 993

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        print(mail.list())
        print("ohk")
        mail.select('[Gmail]/Drafts')

        result, data = mail.uid('search', None, "ALL") # search and return uids instead

        latest_email_uid = data[0].split()[-1]
        
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email.decode('utf-8'))
        print("befor==efetch")
        print (email_message['To'])
 
        print (email.utils.parseaddr(email_message['From'])) # for parsing "Yuji Tomita" <yuji@grovemade.com>
        #print(email_message.items())
        print(*email_message.items(),sep="\n")

        if "Content-Type" in email_message.items():
            print ("\nyeah\n")
         # print all headers
    except Exception as e:
        print (str(e))
 
read_email_from_gmail()