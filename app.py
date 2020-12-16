import os
import email
import imaplib
import base64

email_user = "thomasward9898@gmail.com"
email_pass = "Meztec$25"

mail = imaplib.IMAP4_SSL("imap.gmail.com",993)

mail.login(email_user, email_pass)

mail.select('Inbox')

type, data = mail.search(None, 'FROM', 'noreply@post.xero.com')
mail_ids = data[0]
id_list = mail_ids.split()
counter = 1

# gets all payslips

def getAllPaySlips():

    for num in data[0].split():
        typ, data = mail.fetch(num, '(RFC822)' )
        raw_email = data[0][1]
    # converts byte literal to string removing b''
        raw_email_string = raw_email.decode('utf-8')
        email_message = email.message_from_string(raw_email_string)
        weekEndingTitle = ("W_E_" + (str(email_message).split("Week ending ")[1])[:11]).replace(" ", "_")

        for part in email_message.walk():
            # this part comes from the snipped I don't understand yet...
            if part.get_content_maintype() == 'multipart':
                continue
            if part.get('Content-Disposition') is None:
                continue

            fileName = part.get_filename()
            if bool(fileName):
                newFileName = weekEndingTitle + ".pdf"
                print(newFileName)
                filePath = os.path.join('payslips', newFileName)
                if not os.path.isfile(filePath) :
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()


# get latest payslip

def getLatestPayslip(idlist):
    lastId = len(idlist)-1
    num = idlist[lastId]
    typ, data = mail.fetch(num, '(RFC822)' )
    raw_email = data[0][1]
# converts byte literal to string removing b''
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
    weekEndingTitle = ("W_E_" + (str(email_message).split("Week ending ")[1])[:11]).replace(" ", "_")

    for part in email_message.walk():
        # this part comes from the snipped I don't understand yet...
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        fileName = part.get_filename()
        if bool(fileName):
            newFileName = weekEndingTitle + ".pdf"
            print(newFileName)
            filePath = os.path.join('payslips', newFileName)
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()

getLatestPayslip(id_list)
