# url="http://www.google.com"   (200# request successful)
# response=requests.get(url)
# print(response.status_code)

# url="https://icanhazdadjoke.com/"
# response = requests.get(url, headers={"Accept":"application/json"})
# data = response.text
# print(type(data))
# data = response.json()
# print(data)
# print(type(data))
# print(data["joke"])
# print(data.get('idd'))
