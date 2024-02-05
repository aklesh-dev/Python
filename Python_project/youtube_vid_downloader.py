from pytube import YouTube

link = 'https://www.youtube.com/watch?v=gwUz3E9AW0w'

youtube = YouTube(link)
# youtube title
# print(youtube.title)

# youtube thumbnail image url
# print(youtube.thumbnail_url)

videos = youtube.streams.all() # All formate

# videos = youtube.streams.filter(only_audio=True) # audio formate

vid = list(enumerate(videos))
for i in vid:
    print(i)
print()
strm = int(input("Enter : "))
videos[strm].download()
print('Download successfull.')

# ============Playlist download==============
# from pytube import Playlist

# py = Playlist('')

# print(f'downloading : , {py.title}')
# for video in py.videos:
#     video.streams.first().download()
# print("Download Sucessfull")
