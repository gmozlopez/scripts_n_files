#!/usr/bin/python

import argparse
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--to", dest='toaddress')
parser.add_argument("-f", "--from", dest='fromaddress')
parser.add_argument("-a", "--attachment", dest='attachment')
args = parser.parse_args()

fromaddress = args.fromaddress
toaddress = args.toaddress
attachment = args.attachment

msg = MIMEMultipart()
msg['Subject'] = attachment
msg['From'] = fromaddress
msg['To'] = toaddress

part = MIMEBase('application', "octet-stream")
part.set_payload(open(attachment, "rb").read())
Encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename=' + attachment)

msg.attach(part)

s = smtplib.SMTP('localhost')
s.sendmail(fromaddress, [toaddress], msg.as_string())
s.quit()