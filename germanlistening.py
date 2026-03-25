# IMPORTS
import yt_dlp
from pydub import AudioSegment
import random 
import pathlib
from pathlib import Path
from playsound import playsound

rounds = 10 


URL = 'https://www.youtube.com/watch?v=XYC3mXpQ9zI'

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'audio.webm'
}

url = input("Which video do you want to listen to?")

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    file_path = Path('audio.webm')
    if not file_path.exists():
     ydl.download([url])

audio = AudioSegment.from_file('audio.webm')

for i in range(rounds):
    segment_duration = 10 * 1000
    max_start = len(audio) - segment_duration
    random_start = random.randint(0, max_start)
    random_segment = audio[random_start : random_start + segment_duration]
    random_segment.export(f"random_segment_{i}.mp3", format="mp3")

playsound('random_segment.mp3')

