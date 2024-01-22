import json
import requests

payload={
    "name": "shubh" ,"job":"api testing"
}

resp=requests.put("https://reqres.in/api/users/2" ,data=payload)

print(resp)
print(resp.json())

print(resp.headers.get("content-type"))

assert resp.json()['job']== 'api testing'