import requests
import base64
encoded_bytes = base64.b64encode("nagendra:Chinna@14345".encode())
encoded_str = encoded_bytes.decode()
headers = {'Authorization': f'Basic {encoded_str}'}
r = requests.get('http://127.0.0.1:8000/usermynotes_rest/', headers=headers)
j=r.json()
# print(j)
if r.status_code==200:
    for data in j:
        print(data['title'])
else:
    print("Error!!!")