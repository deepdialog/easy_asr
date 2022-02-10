import base64
import requests
import json

audio = open('/storage/lol/chatbot_api/fastapi/Juzibot_asr/test/input.slk', 'rb')  # open binary file in read mode
audio_read = audio.read()
audio_encode = base64.encodestring(audio_read)

url = 'http://127.0.0.1:61112/api/audio/'
post_body = {
    'lol': "1",
    'audio_name': "input.slk",  # wechat audio is end up with .slk
    'audio_data':  "data:audio/silk;base64,"+audio_encode.decode()
}

x = requests.post(url, data=json.dumps(post_body,indent=None))

print(x)
