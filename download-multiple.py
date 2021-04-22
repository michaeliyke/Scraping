from bs4 import BeautifulSoup
import requests

archive = "http://www-personal.umich.edu/~csev/books/py4inf/media/"

def getVideoLinks(archive):
	r = requests.get(archive)
	soup = BeautifulSoup(r.content, "html5lib")
	links = soup.findAll("a")
	videoLinks = [
		archive + link["href"] for link in links if link["href"].endswith("mp4")
	]

	return videoLinks


def downloadVideoSeries(videoLinks):
	for videoLink in videoLinks:
		fileName = videoLink.split("/")[-1]
		print("Downloading file: %s"%fileName)
		r = requests.get(videoLink, stream=True)
		with open(fileName, "wb") as file:
			for chunk in r.iter_content(chunk_size=1024*1024):
				if chunk:
					file.write(chunk)
		print("%s downloaded"%fileName)
	print("All videos downloaded")
	return