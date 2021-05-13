import requests, json, time
import urllib.request as request

# Personal acess token NTY4OTZlZTYtNjFiYy00ZWYyLWEzOWEtOGU0Y2UwMzJkNDI0NjQyODczYjAtMWJk_P0A1_c1cccb6a-5e2d-4f80-86f9-f0dcefbd12f8
access_token = input("Enter Personal Access Token : ")
# Room Webex Team
room_id = "Y2lzY29zcGFyazovL3VzL1JPT00vNjA5Nzk5NDAtNTU3My0xMWViLWEzNzUtY2JkMGE4ZjAxYTA3"

def GetMessage(access_token, room_id):
    """ Get message from WebEx """
    url = 'https://webexapis.com/v1/messages?roomId={}'.format(room_id)
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
    res = requests.get(url, headers=headers)
    text = res.json()["items"][0]["text"]

    return text

while True:
    text = GetMessage(access_token, room_id)
    print("Received message:" + text)
    if text != "61070038":
        print(text)
        continue
    else:
        message = "Hello, it's me"
        url = 'https://webexapis.com/v1/messages'
        headers = {
            'Authorization': 'Bearer {}'.format(access_token),
            'Content-Type': 'application/json'
        }
        params = {'roomId': room_id, 'markdown': message}
        requests.post(url, headers=headers, json=params)
    time.sleep(1)