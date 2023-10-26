# Day 34 - Creating a GUI Quiz App using API
#### References
1. [[Day 17 - The quiz project]]

## Challenge 1 - Create a Trivia App
API Website Link: [Opentdb](https://opentdb.com/api_config.php)
API Request Link: [Opentdb API](https://opentdb.com/api.php)

>[!note]- Reference
>This uses the same quiz used in [[Day 17 - The quiz project]]

In the quiz app we hard coded the questions. Here, we get the questions from an API.

```py
import requests


PARAMETERS = {
	"amount": 10,
	"type": "boolean"
}
question_data = []

data = request(url="https://opentdb.com/api.php", params=PARAMETERS)
data_json = data.json()

for item in data_json:
	question_data.append(item)
```
