import requests

# URL
url = 'http://localhost:5001/api'

# Change the value of experience that you want to test
payload = {
    'pregnancy':6,
    'glucoes':148,
    'bloodpres':72,
    'skin':35,
    'insulin':0,
    'bmi':33.6,
    'diabetesPedi':0.627,
    'age':50
    
}

r = requests.post(url,json=payload)

print(r.json())
