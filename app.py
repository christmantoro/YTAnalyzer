from pytube import YouTube

youtube_url = "https://www.youtube.com/watch?v=UiYXwUg23Yw" 

yt=YouTube(youtube_url)

try:
    if(yt):
        print("Title: ", yt.title)
        print("Views: ", yt.views)
        print("Author: ", yt.author)
        print("Description: ", yt.description)
except:
    print("There is some problem .....")
