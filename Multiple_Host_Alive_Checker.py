# Simple Multiple  Host Alive Monitor

import subprocess,time
import datetime

IP_Address_File_Path = "IP_Address_File.txt"
NOTIFIED_IP_Addresses = []

flag = True

def check(IP_Address):
    flag = True
    current_datetime = datetime.datetime.now()

    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    PING = "timeout 2 ping -c 1 " + IP_Address

    output = subprocess.getoutput(PING)

    try:
        if f"64 bytes from {IP_Address}:" in output.split("\n")[1]:
            print("-" * 62)
            print(f"{formatted_datetime}\t{IP_Address}\tConnectivity is Successful..")
            print("-" * 62)
        
    except KeyboardInterrupt:
        print("Cancelled")
        exit()
    except:
        print("-" * 62)
        print(f"{formatted_datetime}\t{IP_Address}\tConnectivity is Lost..")
        print("-" * 62)
        flag = False

    return flag

def send_sms():
    print("SMS was sent")

def main():   

    with open(IP_Address_File_Path, 'r') as IPFP:
        IP_Addresses = IPFP.readlines()
        for IP_Address in IP_Addresses:
            IP_Address = IP_Address.strip("\n")
            flag = check(IP_Address)
            if not flag:
                if IP_Address not in NOTIFIED_IP_Addresses:
                    NOTIFIED_IP_Addresses.append(IP_Address)
                    send_sms()
    
    print(NOTIFIED_IP_Addresses)
            
while flag:
    flag = main()
    time.sleep(60)