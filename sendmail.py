from datetime import date
import smtplib
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate
import os

def main():
    # Check if there is a file for today
    todayFilename = date.today().strftime("%Y-%m-%d") + ".mobi"
    if (os.path.isfile(todayFilename) == True):
        # If so, send it
        sendMail()

def sendMail():
    # Adjust these lines for your mail server setup
    smtpServer = "YOUR SMTP SERVER HERE"
    smtpPort = 587
    smtpUser = "YOUR SMTP USER HERE"
    smtpPassword = "YOUR SMTP PASSWORD HERE"
    messageFrom = "SENDER MAIL ADDRESS"
    messageTo = "RECIPIENT MAIL ADDRESS"

    server = smtplib.SMTP(smtpServer, smtpPort)

    #Next, log in to the server
    server.login(smtpUser, smtpPassword)

    #Send the mail
    msg = MIMEMultipart()
    msg['From'] = messageFrom
    msg['To'] = messageTo
    msg['Date']= formatdate(localtime = True)
    msg['Subject'] = "NHK News"
    server.sendmail(messageFrom, messageTo, msg.as_string())

main()