import requests 
from bs4 import BeautifulSoup
import smtplib


headers = {"User-Agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'} 

def check_price():
    which_site = int(input("Which site do u want to track prices on, Lazada or Amazon? For Lazada press 1, for Amazon press 2:    "))
    if which_site == 2:
        URL =  input("Please give us the link to the object")
        page = requests.get(URL , headers = headers)    
        soup =BeautifulSoup(page.content , 'html.parser')        
        title = soup.find(id = "productTitle").get_text()#to find out what id to use, use the ispect elements on google instead of pressing f12 to geenrate the script, Yes it raises issues
        title = title.strip()#clean out blank spaces from html tag
        price = (soup.find(id = "priceblock_ourprice").get_text())
        price = float(price[2:])#to remove the pricing signs i.e s$. You will have to configure it based on your location 
        print(price)
        print("Product name: " , title)
        if price < 600:
            send_mail()
    else:
        print("working on attaching to other sites")

        
        
        
 
#before you do this, head on to  https://myaccount.google.com/lesssecureapps to allow less secure apps, if not email will not be sent
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com' , 587    ) 
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('' , '') # fill in username and pw
    subject = "price tracker notif"
    body = "check , https://www.amazon.sg/Sony-WH-1000XM3-Bluetooth-Cancelling-Headphones/dp/B07H2DBFQZ/ref=sr_1_1?keywords=sony&qid=1575814267&s=gateway&sr=8-1"
    msg = f"Subject: {subject} \n\n{body}" #formatting of notification email
    server.sendmail('','',msg) #sender and recepient
    print("email sent")
    server.quit()
check_price()