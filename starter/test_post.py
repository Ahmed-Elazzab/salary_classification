import requests

data = {
    "age": 30,
    "workclass": "State-gov",
    "fnlgt": 141297,
    "education": "Bachelors",
    "education-num": 13,
    "marital-status": "Married-civ-spouse",
    "occupation": "Prof-specialty",
    "relationship": "Husband",
    "race": "Asian-Pac-Islander",
    "sex": "Male",
    "capital-gain": 0,
    "capital-loss": 0,
    "hours-per-week": 40,
    "native-country": "India"
}

response = requests.post("https://immense-dusk-54638-1cdf10467aa5.herokuapp.com/inference", json=data)

print(response.status_code)
print(response.text)