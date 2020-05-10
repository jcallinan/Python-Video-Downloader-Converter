'''
A simple python based gui application to download videos from youtube.
- By B.Shubankar
'''

import tkinter as tk
import os
import youtube_dl
import tkinter.font as tkfont
from tkinter import *
from tkinter.ttk import *

root = tk.Tk()
root.title('Video Downloader')
root.resizable(width=FALSE, height=FALSE)

canvas1 = tk.Canvas(root, height=600, width=600, bg="#cdcbcb")
canvas1.pack()
bold_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
label1 = tk.Label(root, text="YouTube video URL or playlist URL:", bg="#cdcbcb")
label1.config(font=bold_font)
canvas1.create_window(200, 50, window=label1)
download_entry = tk.Entry(root, width=75)
canvas1.create_window(300, 100, window=download_entry)


def get_video_url():
    search_item = download_entry.get()
    ydl_opts = {
        'format': 'best',
        'extract-audio': True,
        'ignoreerrors': True
    }

    os.chdir('C:/YouTubeDownloads')
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_item])
    bold_font2 = tkfont.Font(family="Helvetica", size=10, weight="bold")
    label_done = tk.Label(root, text="Video Downloaded", width=200, bg="#cdcbcb")
    label_done.config(font=bold_font2)
    canvas1.create_window(600, 600, window=label_done)


download = tk.Button(text="Download", padx=5, pady=5, width=50, command=get_video_url)
canvas1.create_window(300, 150, window=download)
root.mainloop()
