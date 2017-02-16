
from twilio.rest import TwilioRestClient
# put your own credentials here
ACCOUNT_SID = '<SID>'
AUTH_TOKEN = '<TOKEN>'
import requests

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

status = requests.get('https://www.opm.gov/json/operatingstatus.json').json()['ShortStatusMessage']

client.messages.create(
    to = '<TO PHONE>',
    from_ = '<FROM PHONE>',
    body = status,
)

