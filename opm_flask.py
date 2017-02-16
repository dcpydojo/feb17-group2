import requests
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    status = requests.get('https://www.opm.gov/json/operatingstatus.json').json()
    return status['ShortStatusMessage']

if __name__ == "__main__":
    app.run()

