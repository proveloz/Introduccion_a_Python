import json
import requests

######### DESAFÍO 1 ##############

def request(method,requested_url, payload = ""):
    
    headers = {
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.13.0",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "1b0c8c91-446d-4359-82a9-38882f4a0cef,8e06124b-ea83-4124-a3e6-0111cb812cf7",
    'Host': "reqres.in",
    'cookie': "__cfduid=de36e63f3f4c8ec21532aedf6373e27381560114393",
    'accept-encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

    response = requests.request(method, requested_url, data= payload, headers=headers)
    if method == "DELETE":
        return(response)
    else:
        return json.loads(response.text)

######### DESAFÍO 2 ##############

desafio_2 = request("GET", "https://reqres.in/api/unknown")

print(desafio_2)

######### DESAFÍO 3 ##############

desafio_3 = request("POST", "https://reqres.in/api/users/1","{\n\t\"name\" : \"Pablo\",\n\t\"job\": \"Profesor\"\n}")

print(desafio_3)

######### DESAFÍO 4 ##############

desafio_4 = request("PUT","https://reqres.in/api/users/2","{\n\t\"name\" : \"Nuevo Usuario\",\n\t\"job\": \"Nuevo trabajo\"\n}")

print(desafio_4)

######### DESAFÍO 5 ##############

desafio_5 = request("DELETE","https://reqres.in/api/users/2","{\n\t\"name\" : \"Nuevo Usuario\",\n\t\"job\": \"Nuevo trabajo\"\n}")

print(desafio_5)