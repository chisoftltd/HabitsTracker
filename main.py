from datetime import date, timedelta

import requests

USERNAME = "chisoft"
TOKEN = "qp10WO#&%$eo4789iuY@?"
today = date.today()
daybe4 = today - timedelta(days=2)
yesterday = today - timedelta(days=1)
GRAPH_ID = "graph2"

# Create User
pixela_endpoint = "https://pixe.la/v1/users"

user_paraments = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#   response = requests.post(url=pixela_endpoint, json=user_paraments)
#   print(response.text)

#   Insert pixela
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Python Graph",
    "unit": "Day",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


value_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

graph_value = {
    "date": yesterday.strftime('%Y%m%d'),
    "quantity": "34",
}

# Insert API
new_graph_value = {
    "quantity": "100"
}
put_pixela_value = f"{value_endpoint}/{yesterday.strftime('%Y%m%d')}"
# response = requests.put(url=put_pixela_value, json=new_graph_value, headers=headers)
# print(response.text)

# delete API
response = requests.delete(url=put_pixela_value, headers=headers)
print(response.text)
