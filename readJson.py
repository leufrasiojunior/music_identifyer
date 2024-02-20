import json, eyed3

with open("resposta.json") as arquivo_json:
    dados = json.load(arquivo_json)

title = dados["result"]["track"]["title"]
subtitle = dados["result"]["track"]["subtitle"]
album = dados["result"]["track"]["sections"][0]["metadata"][0]["text"]
release = dados["result"]["track"]["sections"][0]["metadata"][2]["text"]
genres = dados["result"]["track"]["genres"]["primary"]

print(title)
print(subtitle)
print(album)
print(release)
print(genres)

audiofile = eyed3.load("03 Papin.mp3")
audiofile.tag.title = str(title)
audiofile.tag.artist = str(subtitle)
audiofile.tag.album = str(album)
audiofile.tag.album_artist = "Various Artists"


audiofile.tag.save()
