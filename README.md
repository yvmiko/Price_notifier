

# Book Price Notifier. 

This Python script uses the requests library to scrape the price of a particular book from a website and sends an email notification using smtplib when the price falls below a specified threshold.

Requirements

* Python 3.6 or higher
* requests library
* BeautifulSoup library
* smtplib library

## Setup

1. Clone the repository and navigate to the directory:
   git clone https://github.com/your-username/book-price-notifier.git
   cd book-price-notifier



2. Edit the script to specify the book URL, email addresses, and password

   url = 'http://books.toscrape.com/catalogue/finders-keepers-bill-hodges-trilogy-2_807/index.html'

   sender = 'Sender@yahoo.com'

   password = 'YourPassword'

   recipient = 'Receiver@yahoo.com'
   
 


