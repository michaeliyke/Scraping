from tkinter import ttk, filedialog, Tk, Label, Entry, Button, StringVar
# from pytube import playlist, YouTube #pip install pytube3
folderName = ""

def openPath():
	global folderName, locationError
	folderName = filedialog.askdirectory()
	print(locationError, folderName)

	if len(folderName) > 1:
		locationError.config(text=folderName, fg="green")
	else:
		locationError.config(text="Please choose a folder", fg="red")


def dowloadVideo(choices, entry):
	choice = choices.get()
	url = entry.get()
	urlError.config(text="")
	yt = YouTube(url)

	if choice == choice[0]:
		select = yt.streams.filter(progressive=True).first()
	elif choice == choices[1]:
		select = yt.streams.filter(progressive=True, file_extension="mp4").last()
	elif choice == choices[2]:
		select = yt.streams.filter(only_audio=True).first()
	else:
		urlError.config(text="Paste link again", fg="red")

	# Download function
	select.download(folderName)
	urlError.config(text="Download completed!", fg="green")