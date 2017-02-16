"""
send-status.py

Sends the latest OPM status to the e-mail address in the script.
"""
import requests
import os

from twilio.rest import TwilioRestClient


TO_NUMBER = os.environ['TO_NUMBER']
FROM_NUMBER = '+12025172178'

def main():
	curr_status = requests.get('https://www.opm.gov/json/operatingstatus.json').json()
	print(curr_status['AppliesTo'],curr_status['ShortStatusMessage'])


def get_current_status():
    url = 'https://www.opm.gov/json/operatingstatus.json'
    return requests.get(url).json()


def send_latest_status_on_twilio():
    status = get_current_status()
    msg = '{AppliesTo} {ShortStatusMessage}'.format(**status)
    send_msg_on_twilio(msg)


def send_msg_on_twilio(msg):
    account_sid = "AC00c9739a1539392c4a97f5dc3f5d94c2"
    auth_token  = "a69a488ffa451e2e7c70c5c5ec69b08e"

    client = TwilioRestClient(account_sid, auth_token)
    client.messages.create(
        body=msg,
        to=TO_NUMBER,
        from_=FROM_NUMBER,
    )


def get_last_historical_status():
    """
    Get historical status, limit to one

    >>> status = get_last_historical_status()
    >>> status['Title']
    'Federal Government Operating Status in the Washington, DC, Area'
    """
    url = 'https://www.opm.gov/json/operatingstatushistory.json?count=1'
    statuses = requests.get(url).json()
    return statuses[0]


if __name__ == '__main__':
    send_latest_status_on_twilio()
