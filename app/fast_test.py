from typing import Optional
from fastapi import FastAPI , Form
from typing import Optional
from pydantic import BaseModel
import base64
import os
from pydub import AudioSegment
import paddle
from paddlespeech.cli import ASRExecutor
from paddlespeech.cli import TextExecutor

app = FastAPI()

@app.get("/api/audio")
async def audio_help():
    return "send_audio"

class Item_audio(BaseModel):
    lol: Optional[str] = None
    audio_name: Optional[str] = None
    audio_data: Optional[str] = None

@app.post("/api/audio/")
async def create_item(item: Item_audio):
   
    gg=item.audio_data.replace("data:audio/silk;base64,","")
    print(gg)
    audio_data = base64.b64decode(str(gg))
    # dir = "./"+item.audio_name.replace("slk","")
    dir = item.audio_name.replace("slk","")
    fout = open((dir+"silk"),'wb')
    fout.write(audio_data)
    fout.close()  # right
    os.system("bash ./silk-v3-decoder/converter_beta.sh "+"../"+dir+"silk" +" mid.mp3") ## 相对于程序的路径
    song = AudioSegment.from_mp3(dir+"mid.mp3")
    song.export(dir+"wav", format="wav")
    asr_executor = ASRExecutor()
    text = asr_executor(
        model='conformer_wenetspeech',
        lang='zh',
        sample_rate=16000, # 16000
        config=None,  # Set `config` and `ckpt_path` to None to use pretrained model.
        ckpt_path=None,
        audio_file="./"+dir+"wav",
        force_yes=True,
        device=paddle.get_device())
    print('Result: \n{}'.format(text)
    )
    os.system("rm -rf "+dir+"*")
    
    text_executor = TextExecutor()
    result = text_executor(
        text=text,
        task='punc',
        model='ernie_linear_p7_wudao',
        lang='zh',
        config=None,
        ckpt_path=None,
        punc_vocab=None,
        device=paddle.get_device()
        )
    return result
