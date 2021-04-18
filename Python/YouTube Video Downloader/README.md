# YouTube Video Downloader Using Python

Inport necessary modules and make sure to install __pytube3__.<br>
Pytybe is a python package used for downloading Youtube videos mainly and __tkinter__ is one the simple GUI Library of Python and __pathlib__ is used for directory related operation.

```
from tkinter import *
import pathlib
from pytube import YouTube
# pip install pytube3
from tkinter import messagebox, filedialog
```

## Creating Mainwindow

The last step is to create a root window and call the important function and create text variables.

```
root = Tk()
root.geometry("400x110")
root.resizable(0,0)
root.title("YouTube Video Downloader")
root.config(background = "#000000")
# Creating the tkinter Variables
video_Link = StringVar()
download_Path = StringVar()
# Calling the Widgets() function
Widgets()
root.mainloop()
```

## Adding Widgets

```
def Widgets():
    link_label = Label(root,text="YouTube link :",bg="#E8D579",width=20)
    link_label.grid(row=1,colum=0,pady=5,padx=5)

    linkText = Entry(root,width=55,textVariable = video_Link)
    linkText.grid(row=1,colum=1,pady=5,padx=5,columnspan=2)

    destination_label = Label(root,text="Destination :",bg="#E8D579",width=20)
    destination_label.grid(row=2,column=0,pady=5,padx=5)

    browse_B = Button(root,text="Browse",command=Browse,width=10,bg="#05E8E0")
    browse_B.grid(row=2,column=2,pady=1,padx=1)

    Download_B = Button(root,text="Download",command=Download,width=20,bg="#05E8E0")
    Download_B.grid(row=3,column=1,pady=3,padx=3)
```

## Browse Function

This function is for changing the path of directory where we want to save our video.

```
# destination folder to save the video
def Browse():
    download_Directory = filedialog.askdirector(initialdir=pathlib.Path.cwd())
    # Displaying the directory in the directory
    #textbox
    download_Path.set(download_Directory)
```

## Download Function

You can use this function directly in any python script for downloading youtube videos but after a little modification.

```
def Download():
    #getting user-input Youtube Link
    YouTube_link = video_Link.get()
    download_Folder = download_Path.get()
    # Creating objext of YouTube()
    getVideo = YouTube(YouTUbe_link)
    # Getting alla the available streams of the youtube video and selecting the first
    videoStream = getVideo.streams.first()
    # Downloading the video to destination
    videoStream.downloas(download_Folder)
    # Displaying the message
    messagebox.showinfo("SUCCESSFULLY","DOWNLOADED AND SAVED IN\n" + download_Folder)
```

## Output

This Downloader Downloads one youtube Video at a time and save the video on a specific folder selected by user.

![Cattura](https://user-images.githubusercontent.com/57859960/115160109-bd83c480-a096-11eb-8a73-cdb3e8350b02.PNG)
