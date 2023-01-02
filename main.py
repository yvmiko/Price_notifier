# 'requests' library for making HTTP requests 
import requests

# 'BeautifulSoup' is a Python library for parsing HTML and XML documents
# it creates parse trees that are helpful to extract data easily
from bs4 import BeautifulSoup

# 'smtplib' is a Python library for sending email using the Simple Mail
# Transfer Protocol.
import smtplib

# 'time' is a built-in Python library for working with time-related functions
# It provides functions for getting the current time, converting between different
# time representations, and measuring elapsed time.
import time

# While loop will make sure the code runs (once a day)
while True:
    re = requests.get('http://books.toscrape.com/catalogue/finders-keepers-bill-hodges-trilogy-2_807/index.html')
    res = re.content

    soup = BeautifulSoup(res, 'html.parser')
    price = float(soup.find('p', class_='price_color').text[1:])

# Checking if the price is less than 40


    if price < 40:
        smt = smtplib.SMTP('smtp.mail.yahoo.com', 587) # creates an SMTP objective using Yahoo's SMTP server and port number
        smt.ehlo() # sends the EHLO command to the SMTP server, which initiates the SMTP session.
        smt.starttls() # this line starts Transport Layer Security (TLS) for the SMTP connection, which allows for encryted communication
        # Use your credentials
        smt.login('YourEmail@yahoo.com', 'YourPassword') # this line logs in to the SMTP server using the provided email and password
        # this line sends an email with the specified subject and body to the receiver's email address. The f before the string indicates that it is an f-string, 
        # which allows for the evaluation of expressions inside string literals. In this case, the value of the price variable is included in the body of the email
        smt.sendmail('Sender@yahoo.com', 
                 'Receiver@yahoo.com', 
                 f"Subject: Book Price Notifier\n\nHi, price has dropped to {price}.") 
        smt.quit() # this lin ends the SMTP session and closes the connection.
    time.sleep(24*60*60) # this line causes the script to pause for 24 hours 
                         # (24hours * 60 minutes * 60 seconds/minute) before continuing.
            

    

    