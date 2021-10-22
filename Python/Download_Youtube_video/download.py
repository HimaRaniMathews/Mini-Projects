from pytube import YouTube
link=input("Enter a youtube link : ")
url=YouTube(link)
print(f'{url.title} is downloading please wait .... ')
video=url.streams.first()
video.download()
print(f'Video is downloaded as ',url.title,'mp4')