from pydub import AudioSegment

from checkReqs import *


maxCutSeconds = 40


def convert_file_to_send(file_path, filename):
    audio_file = AudioSegment.from_file(file_path)
    duration = audio_file.duration_seconds
    # return duration
    startCut = int((int(duration) // 4)) * 1000
    endCut = startCut + (maxCutSeconds * 1000)
    editedSong = audio_file[int(startCut) : int(endCut)]
    editedSong.export(f"{editedFolder}/{filename}", format="mp3")
