import requests
import json

def request(requested_url,apikey):
    headers = {
    "app_id": "pvelozm@gmail.com",
    "app_key": apikey,
    }
    response = requests.request("GET", requested_url, headers=headers)
    return json.loads(response.text)

data=request("https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY","DEMO_KEY")

def build_web_page(a):
    a=a["photos"]
    html = ""   
    for i in range(0,15):
        html += "<img src=\"{}\">\n".format(a[i]["img_src"])
## Este recurso nos permite crear un archivo y escribir contenido en él
    with open("output.html", "w") as f:
        f.write(html)
    return f.close()

build_web_page(data)
