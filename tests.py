try:
	from pytube import YouTube
	from pytube import Playlist
except ImportError as importError:
	print("Some modules are missing {}".format(ImportError))
	exit()

url = "https://www.youtube.com/watch?v=Jf7v0J8aNEQ"
ytd = YouTube(url)

# Streams are various resolutions
streams = ytd.streams.all():
firstStream = ytd.streams.first()
firstStream.download()


"""
Extra

	--High qaulity resolutions available
ytd.streams.filter(adaptive=True).first().download()
	--Highest cutting edge resolutions available
ytd.streams.filter(progressive=True).first().download()
	--Get only audio feed
ytd.streams.filter(audio_only=True).all().download() 
	--Only mp4 subtype
ytd.streams.filter(subtype="mp4").first().download()
"""