import requests 
from bs4 import BeautifulSoup
import smtplib

#TESTED USING : https://www.amazon.sg/UltraShell-QuietComfort-Headphones-Replacement-Accessories/dp/B07R5LMJ2S/ref=pd_sim_23_3/357-5779832-6503746?_encoding=UTF8&pd_rd_i=B07R5LMJ2S&pd_rd_r=0c352e66-8284-40f3-880d-d3060fc5e7ee&pd_rd_w=j1M16&pd_rd_wg=YSMMM&pf_rd_p=a14a3793-cae8-4ef0-87fc-ede72710fb36&pf_rd_r=TS8EW3ZFQHPWTTDDB67B&psc=1&refRID=TS8EW3ZFQHPWTTDDB67B

headers = {"User-Agent" : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'} 

def check_price():
    which_site = int(input("Which site do u want to track prices on, Lazada or Amazon? For Lazada press 1, for Amazon press 2: "))
    if which_site == 2:
        target = input("What is the highest price that you're willing to pay for this product ? ")
        URL =  input("Please give us the link to the product")
        try:
            target = int(target)
            page = requests.get(URL , headers = headers)    
            soup =BeautifulSoup(page.content , 'html.parser')        
            
            title = soup.find(id="productTitle").get_text().strip()#to find out what ID to use, use the inspect elements on google instead of pressing f12 to geenrate the script, Yes it raises issues
            
            price = soup.find(id = "priceblock_ourprice").get_text().strip()
            price = float(price[2:])#to remove the pricing signs i.e s$. You will have to configure it based on your location 
            print(price , title)
            
            print("Product name: " , title)
            if price < 600:
                send_mail(URL)

        except NameError:
            print("Please provide integer values excluding the sign of your local currency.")
            target = input("What is the highest price that you're willing to pay for this product ? ")
            target = int(target)
            page = requests.get(URL , headers = headers)    
            soup =BeautifulSoup(page.content , 'html.parser')        
            
            title = soup.find(id="productTitle").get_text().strip()#to find out what ID to use, use the inspect elements on google instead of pressing f12 to geenrate the script, Yes it raises issues
            
            price = soup.find(id = "priceblock_ourprice").get_text().strip()
            price = float(price[2:])#to remove the pricing signs i.e s$. You will have to configure it based on your location 
            print(price , title)
            
            print("Product name: " , title)
            if price < target:
                send_mail(URL)
        except :
            print("Sorry try again later.")

    else:
        print("working on attaching to other sites")
        
        
        
 
#before you do this, head on to  https://myaccount.google.com/lesssecureapps to allow less secure apps, if not email will not be sent
def send_mail(url):
    server = smtplib.SMTP('smtp.gmail.com' , 587    ) 
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('' , '') # fill in username and pw
    subject = "price tracker notif"
    body = 'check ,{}'.format(url)
    msg = f"Subject: {subject} \n\n{body}" #formatting of notification email
    server.sendmail('','',msg) #sender and recepient
    print("email sent")
    server.quit()
    
    
check_price()

