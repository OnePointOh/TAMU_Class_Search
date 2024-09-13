"""
Author: Trevor Hatch
Last Modified: 09/13/2024
Use of this software must follow the GPLv3 licence.
https://www.gnu.org/licenses/gpl-3.0.en.html
"""

import requests
import smtplib
import time
import configparser

def send_message(phone_number, carrier, message, gmail, password):
    recipient = phone_number + CARRIERS[carrier]
    auth = (gmail, password)
 
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(auth[0], auth[1])
 
    server.sendmail(auth[0], recipient, message)

def clean_line(line):
    return line[33:-17]


if __name__ == "__main__":

    config = configparser.ConfigParser()
    config.read('config.ini')

    term_in = config['Settings']['term_in']
    phone_number = config['Settings']['phone_number']
    gmail = config['Settings']['gmail']
    password = config['Settings']['password']
    carrier = config['Settings']['password']
    rest_time = int(config['Settings']['rest_time'])

    CARRIERS = {
        "att": "@mms.att.net",
        "tmobile": "@tmomail.net",
        "verizon": "@vtext.com",
        "sprint": "@messaging.sprintpcs.com"
    }

    base_url = 'https://compass-ssb.tamu.edu/pls/PROD/bwykschd.p_disp_detail_sched?term_in=' + term_in + '&crn_in='

    crn_list = []

    for key, crn in config.items( "classes" ):
        crn_list.append(crn)

    class_status = []

    for crn in crn_list:
        class_status.append(False)
    
        count = 0
        send_message(phone_number, carrier, 'checking classes')

    while True:
        
        for i in range(len(crn_list)):
            crn = crn_list[i]
            URL = base_url + crn
            #print(URL)
            try:
                r = requests.get(url = URL)
            
                if r.text.split('\n')[143] != '<td CLASS="dddefault">0</td>':
                    if class_status[i] == False:
                        send_str = "AVAILABLE: " + clean_line(r.text.split('\n')[112])
                        send_message(phone_number, carrier, r.text.split('\n')[112])
                        class_status[i] = True
                else:
                    if class_status[i] == True:
                        send_str = "TAKEN: " + clean_line(r.text.split('\n')[112])
                        send_message(phone_number, carrier, send_str)
                        class_status[i] = False
                    
            
            except:
                print('error on crn=' + crn)
        print(count)
        time.sleep(10)
        count+=1