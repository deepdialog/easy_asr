# easy_asr


|  Name   | API  | Method | Func | State |
|  ----  | ----  | ----  | ----  |----|
| asr  | /api/audio |get|test|✅|
| ... | /api/audio/ |post |audio->text|✅|


## Deploy

### Way 1 Docker 

Simply copy code below
```
docker run -d -p 61111:81 tianrking/fastapi_asr:v0.2
```


### Way 2 Clone code run on localhost

```
git clone https://github.com/deepdialog/easy_asr
sudo apt-get update && sudo apt-get install python3 python3-pip
pip install -r requirements.txt
uvicorn app.fat_test:app --reload --host 0.0.0.0 --port 61112
```
Then the server is running on localhost:61112

## Server test

- curl -X GET "127.0.0.1:61111//api/audio"
- curl -X POST -k "127.0.0.1:61111/api/audio/" -H 'Content-Type: application/json' -d'
{
    "lol": 1   //whatever u wanna sent
    "audio_name": "name" //name
    "audio_data": "audio.silk" //silk file (Wehcat , Skype)
}
'

** More audio formats will be supported
