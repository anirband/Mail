#!/usr/bin/env python
import smtplib 
 
To=['name1@domain1.com','name2@domain2.com']
From='name3@domain3.com'
Subject='Test mail'
Content='Sent from python'

message='Subject: %s\n\n%s'%(Subject,Content)
 
mail=smtplib.SMTP('mailserver.com',25)

mail.ehlo()

mail.starttls()

mail.login('username','password')

mail.sendmail(From,To,message)

mail.close()
