#!/usr/bin/python3

import smtplib
from email.message import EmailMessage
import os

def sendMail(receiver, sender, subject, text, files=[]):
    assert type(receiver)==list
    assert type(files)==list

    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = ', '.join(receiver)
    msg['Subject'] = subject

    msg.set_content( text )

    for f in files or []:
    with open(f, "rb") as fil:
        part = MIMEApplication(
            fil.read(),
            Name=basename(f)
        )
    # After the file is closed
    part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
    msg.attach(part)

    try:
        with smtplib.SMTP('localhost') as s:
            s.set_debuglevel(1)
            s.send_message(msg)
            s.quit()
        print ("Successfully sent email")
    except smtplib.SMTPException:
	    print ("Error: unable to send email")


sender = 'ogoranskyy@epages.com' # Email that will be shown as a sender
receiver = ['ogoranskyy@epages.com'] # Person taht should receive this email

subject = 'Test new mail server'
reply_to = sender

text = """
Does this email look authentic?
"""

# Example:
sendMail(receiver, sender, subject, text, [])
