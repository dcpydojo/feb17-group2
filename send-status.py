"""
send-status.py

Sends the latest OPM status to the e-mail address in the script.
"""
import requests


TARGET_EMAILS = ['jaraco@jaraco.com']
"""
The e-mails to receive the notifications
"""

def main():
	curr_status = requests.get('https://www.opm.gov/json/operatingstatus.json').json()
	print(curr_status['AppliesTo'],curr_status['ShortStatusMessage'])


if __name__ == '__main__':
    main()
