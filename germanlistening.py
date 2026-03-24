# IMPORTS
import yt_dlp
from pydub import AudioSegment
import random 
import pathlib
from pathlib import Path
from playsound import playsound



audio = AudioSegment.from_file("Fabrik-Besuch.webm")

URL = 'https://www.youtube.com/watch?v=XYC3mXpQ9zI'

ydl_opts = {
    'format': 'bestaudio/best',
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    file_path = Path("Fabrik-Besuch.webm")
    if not file_path.exists():
     ydl.download([URL])

segment_duration = 10 * 1000

max_start = len(audio) - segment_duration
random_start = random.randint(0, max_start)

random_segment = audio[random_start : random_start + segment_duration]
random_segment.export("random_segment.mp3", format="mp3")

playsound('random_segment.mp3')

