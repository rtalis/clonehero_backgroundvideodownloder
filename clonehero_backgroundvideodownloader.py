# youtube_dl and googlesearch are required. You can install them with pip.
import glob
import os
from googlesearch import search
import youtube_dl
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askdirectory

print('Select CH \'songs\' folder')
Tk().withdraw()
path = askdirectory(title='Select CH \'songs\' folder')
#open select folder dialog

text_files = glob.glob(path + "/**/song.ini", recursive=True)
#get the songs from their folder name looking for the .ini files
print(len(text_files), " songs found")

for s in text_files:
    dirname = os.path.dirname(s)
    song = os.path.basename(dirname)
    busca = "Youtube {} (Official Music Video)".format(song)
    #Query used on the google search


    for n in search(busca, tld="com", num=1, start=0, stop=1, lang='en'):
        url = n;
        #Search for the first google result and retrieve its url

    ydl_opts = {'outtmpl': os.path.join(dirname,'video.mp4'),
                #'quiet': 1,
                'nooverwrites': 0,
                'noplaylist': 1,
                #username:,
                #password:
                }
    #Donwload with ydl_opts options.
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

