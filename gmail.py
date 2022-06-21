#!/bin/python

import smtplib

gmail_user = 'testing-email@gmail.com'
gmail_password = 'password'

sent_from = gmail_user
to ='2nd-account@gmail.com'
email_text = "hello"


try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, to, email_text)
    server.close()
except:
    print("wrong")