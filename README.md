# sent2vec
Introducing a service application equipped with an endpoint designed to accept sentences as input and produce sentence vectors—random 500-dimensional arrays—as output.
## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoint](#api-endpoint)
- [Testing](#testing)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/sent2vec.git
   cd sent2vec
   
## Install Dependencies

```pip install -r requirements.txt```

## Usage
1. Run the FastAPI app using Uvicorn:
   - ```uvicorn app.main:app --host 0.0.0.0 --port 8000``` 
2. Access the API : Send a POST request to the API endpoint using your web browser or a tool like curl 

Here are the methods to access the API endpoints
```bash
import requests

url = "http://localhost:8000/generate_random_array/"
headers = {"Accept": "application/json"}
payload = {
    "sentence": "My Name is John",
    "dim": 100
}

response = requests.post(url, headers=headers, json=payload)
print(response.content.decode("utf-8"))  # This will print the response content

```
Access the API from the Terminal
```commandline
http://localhost:8000/generate_random_array/?sentence=<"YourSentenceHere">&dim=500

replace "<YourSentenceHere>" with any sentence (str) you want
```

## API Endpoint
The API endpoint provided by sent2vec allows you to generate random float arrays based on input sentences.

```commandline
Endpoint: /generate_random_array/
```

##### Query Parameters:
```commandline
sentence (str, required): Input sentence for transformation.
dim (int, optional, default=500): Dimension of the generated float array.
```

##### Response:
The response will be a JSON object containing the input sentence and the generated random float array.
```commandline
sentence <str>: "This is an example sentence"
sent_vec <List[float]>: [0.23, 0.033, 0.045, 0.011, 0.097, ....]
```

## Testing
1. Run the test cases using `pytest`:
```commandline
pytest tests/
```
2. Test Coverage:

Measure test coverage using `coverage`:
```commandline
pip install coverage
coverage run -m pytest tests/
coverage report -m
```