import tkinter
from pytube import YouTube

root = tkinter.Tk()
root.geometry('500x500')
root.resizable(0,0)
root.title(" Youtube Video Downloader")


tkinter.Label(root, text ='Youtube Video Downloader', font ='arial 20 bold').pack()




##enter link
link = tkinter.StringVar()

#youtube URL

tkinter.Label(root, text ='Paste Link Here:', font ='arial 18 bold').place(x= 160, y = 60)
link_enter = tkinter.Entry(root, width = 70, textvariable = link).place(x = 32, y = 90)



#function to download video


def Downloader():
     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    tkinter.Label(root, text ='DOWNLOADED', font ='arial 18').place(x= 180, y = 210)


tkinter.Button(root, text ='DOWNLOAD', font ='arial 18 bold', bg ='red', padx = 2, command = Downloader).place(x=180, y = 150)



root.mainloop()

