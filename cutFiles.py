from pydub import AudioSegment
from main import *

#
maxCutSeconds = 40


def get_duration_pydub(file_path):
    global audio_file
    audio_file = AudioSegment.from_file(file_path)
    duration = audio_file.duration_seconds
    return duration


file_path = "test.mp3"
duration = get_duration_pydub(file_path)
startCut = int((int(duration) // 4)) * 1000
endCut = startCut + (maxCutSeconds * 1000)
editedSong = audio_file[int(startCut) : int(endCut)]
editedSong.export("editedSong.mp3", format="mp3")
