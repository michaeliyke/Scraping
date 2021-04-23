from youtubedownloader.definitions import *


root = Tk()
root.title("YTD Downloader")
root.geometry("350x400")

root.columnconfigure(0, weight=1) # Set all contents to the center
# Downloader link label

downloaderLabel = Label(
	root, 
	text="Enter the url of the video", 
	font=("jost", 15)
)

downloaderLabel.grid() # Put lable to grid

entry = Entry(
	root, 
	width=50, 
	textvariable=StringVar()
	) # Establish input entry box

entry.grid() # entry to grid

# Set up error
urlError = Label(
	root, 
	text="Error: invalid url", 
	fg="red", 
	font=("jost", 10)
)

urlError.grid() # Align to grid

# Ask to choose file path
choosePathLabel = Label(
	root, 
	text="Save the video file", 
	font=("jost", 15, "bold")
	)
choosePathLabel.grid()

# Save button
choosePathButton = Button(
	root, 
	width=10, 
	bg="red", 
	fg="white", 
	text="Choose path", 
	command=openPath
	)
choosePathButton.grid()

# Location error
locationError = Label(root, text="Invalid path", fg="red", font=("jost", 10))
locationError.grid()

# Download quality
quality = Label(root, text="Select quality", font=("jost", 15))
quality.grid()

# Combo box - this is the select drop drop-down menu box
choices = ["750p", "144P", "Audio only"]
menu = ttk.Combobox(root, values=choices)
menu.grid()

# Download button
downloadButton = Button(
	root, 
	width=10, 
	bg="red", 
	fg="white", 
	text="Download",
	command=dowloadVideo
	)
downloadButton.grid()

# Developer label
developer = Label(root, text="Dream Developers", font=("jost", 15))
developer.grid()




root.mainloop()