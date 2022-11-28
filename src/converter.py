
from pytube import YouTube
print("downloading, please wait")
url="https://www.youtube.com/watch?v=SzV54nD2uVQ"
video = YouTube(url)
video = video.streams.get_highest_resolution()
video.download()

print("download complete")