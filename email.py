import smtplib 
import pyautogui
import schedule
import time


#Your Personel Info
your_mail = "Your Gmail "
your_password = "Your Pass"

#Reciver Gmail
reciver_mail = pyautogui.prompt("Enter Reciver's Gmail")

#Message
message = """From: Your Name
To:        Recivers Name
Subject:   Your Subject"""

#main
def send_mail():
    
    s = smtplib.SMTP('smtp.gmail.com', 587) 

    s.starttls()

    s.login( your_mail , your_password) 

    s.sendmail( your_mail ,reciver_mail+ "@gmail.com", message) 
    
    print("message Sent to : " +reciver_mail+ "@gmail.com")
    
    s.quit() 

#schedule mail to send
schedule.every().day.at("10:00").do(send_mail)

while 1:
    schedule.run_pending()
    time.sleep(1)
