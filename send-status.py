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
    print(curr_status['AppliesTo'],curr_status['Location'], curr_status['ShortStatusMessage'])


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
    main()
