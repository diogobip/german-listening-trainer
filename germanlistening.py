# IMPORTS
import yt_dlp
from pydub import AudioSegment
import random 
from pathlib import Path
from playsound import playsound
from youtube_transcript_api import YouTubeTranscriptApi

transcription_entries = []




rounds = 10 


ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'audio.webm'
}

url = input("Which video do you want to listen to?")

video_id = url.split("v=")[1]

# Transcript 
try:
    # Fetch transcript data
    ytt_api = YouTubeTranscriptApi()
    transcript = ytt_api.fetch(video_id, languages=['de'])

    for entry in transcript:
        
        
        transcription_entries.append(entry)

except Exception as e:
    print(f"An error occurred: {e}")

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    file_path = Path('audio.webm')
    if not file_path.exists():
     ydl.download([url])

audio = AudioSegment.from_file('audio.webm')

for i in range(rounds):
    segment_duration = 10 * 1000
    max_start = len(audio) - segment_duration
    random_start = random.randint(0, max_start)
    random_start_seconds = random_start / 1000
    random_segment = audio[random_start : random_start + segment_duration]
    random_segment.export(f"random_segment_{i}.mp3", format="mp3")
    playsound(f"random_segment_{i}.mp3")

    entry_text = []

    for entry in transcription_entries:
        if entry.start >= random_start_seconds and entry.start <= random_start_seconds + 10:
            entry_text.append(entry.text)
    
    correct_answer = " ".join(entry_text)

    print(f"Correct answer: {correct_answer}")

# Decoys
decoys = random.sample([s.text for s in transcription_entries if s.text != correct_answer], 3)

        






