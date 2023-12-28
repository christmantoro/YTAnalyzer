from pytube import YouTube

youtube_url = "https://www.youtube.com/watch?v=UiYXwUg23Yw" 

yt=YouTube(youtube_url)

if(yt):
    print("Title: ", yt.title)