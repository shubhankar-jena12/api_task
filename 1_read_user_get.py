import json
import requests

resp=requests.get("https://reqres.in/api/users?page=2")
code=resp.status_code
assert code==200 ,"code doesn't match"
print(resp)
#print(resp.text)
#print(resp.content)
json_response=resp.json()

print(json_response["total_pages"])
assert json_response["total_pages"]==2,"total pages count is not matching"

print(json_response["total"])
assert json_response["total"]==12,"total count is not matching"