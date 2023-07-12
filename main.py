from contextlib import nullcontext
import os
from fastapi import FastAPI
from starlette.responses import FileResponse
import pyttsx3
import time
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()

file_name = "example.txt"

app.mount("/static", StaticFiles(directory="audio"), name="static")


class Item(BaseModel):
    userId: int
    message: str


@app.get("/")
async def root() : 
    return {"app" : "voice"}

@app.get("/file")
async def download_file() : 
    return FileResponse(file_name, media_type='application/octet-stream',filename=file_name)

@app.post("/audio/")
async def get_audio(item : Item) :
    curr_time = round(time.time()*1000) # getting the time in milliseconds
    file_audio_name = 'audio_file_{}'.format(curr_time) #creating a file name with current time
    file_audio_path = "audio/{}.flac".format(file_audio_name) # I had to save the file as flac in order to convert it then using ffmpeg
    url = "/static/"+file_audio_name+".mp3"
    try : 
        engine = pyttsx3.init() #init the speech engine
        # engine.setProperty('rate',160)
        # engine.setProperty('volume',1.0)
        engine.save_to_file(item.message,file_audio_path )
        engine.runAndWait()
    except :
        print('Could not generate voice ')
        url = nullcontext

    try :
        convertAudio(file_audio_path, file_audio_name)
    except Exception as msg_error:
        print(f"ERROR:{msg_error}")

    return { "userId" : "{}".format(item.userId), "link": url , "message" : item.message}

# trying to convert from flac to mp3, cuz if I had some issues saving it as mp3
#so, i am using ffmpeg to make it compatible and you can play
mp3_cmd = 'ffmpeg -i "{file_name}" -c:a mp3 -b:a 128k ./audio/{output_name}.mp3'

def convertAudio(input,output) :
    os.system(mp3_cmd.format(file_name=input, output_name=output.__str__()))