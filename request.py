import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Road Surface_Wet or Damp':1, 'Age of Casualty':41, 'Road Surface_Dry':0})

print(r.json())