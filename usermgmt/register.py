import requests

url = "http://192.168.0.29:8004/api/users/register/"
data = {"name": "pragyan", "phone": '9668440893', "email": "ppmohapatra321@gmail.com", "password": "password123"}
req = requests.post( url, data=data )
print( req.json() )
