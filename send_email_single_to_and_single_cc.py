import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time

def send_email(customer_email):
    try:
        server = smtplib.SMTP('corp-new.lankacom.net', 587)
        server.starttls()
        server.login('servicealert@corp-new.lankacom.net', 'Ser.Lcs@2022@#')
        subject = "To Inform Regading an Urgent Manintaince"
       
        with open('./email-templates/downtime_alert.html', 'r') as file:
            html = file.read()

        message = MIMEMultipart()
        message.attach(MIMEText(html, 'html'))

        message['Subject'] = subject
        message['From'] = 'LankaCom Service Alert <servicealert@corp-new.lankacom.net>'
        message['To'] = customer_email
        message['Content-Type'] = 'text/html'
        message['CC'] = 'LankaCom Service Alert <servicealert@corp-new.lankacom.net>'

        to_list = [customer_email] + ["servicealert@corp-new.lankacom.net"]

        server.sendmail('servicealert@corp-new.lankacom.net', to_list , message.as_string())

        server.quit()
    except Exception as e:
        print(f"Error sending email: {e}")

def main_function():

    with open('./for_single_to_single_cc.txt', 'r') as file:
        for line in file:
            line = line.split()[0]
            print(f"Sending an Email to {line}...", end="\t")
            send_email(line)
            print("Done")
            time.sleep(2)

main_function()
