from re import I
from time import sleep
from tkinter import *
import requests
import json
from random import shuffle
import tkinter.ttk as ttk
import threading
from main import Main
class Loading:
    def __init__(self):
        #self.tk = Tk()
        #self.tk.resizable(False, False)

        fo = open('word_a.txt', 'r')
        self.data1 = json.loads(fo.read())
        fo.close()

        go = open('word_b.txt', 'r')
        self.data2 = json.loads(go.read())
        go.close()

        co = open('word_c.txt', 'r')
        self.data3 = json.loads(co.read())
        co.close()


        self.windows()

    def windows(self):
        global loading_frame
        print('loading_frame-Start')
        loading_frame = ttk.Frame()
        loading_frame.pack(fill=BOTH, pady=0, padx=0)
        canvas = Canvas(loading_frame, width=1400, height=800, bg="#4169e1")
        canvas.create_text(1130, 730, text='LoadingNow...', font=("Arial Black", 50))
        #canvas.create_window(300,650,window=ttk.Button(canvas, text="window", command=self.sled, padding=[200,60,200,60]), anchor="center")

        line = canvas.create_line(
            15, 15,
            15, 800-15,
            1400-15, 800-15,
            1400-15, 15,
            15, 15,
            width=3, fill="#ccdaff"
        )
        canvas.pack()
        loading_frame.after(3000, self.sled)
        loading_frame.mainloop()
 
    def sled(self):
        print(self.data1[0][0])
        print(self.data2[0][0])
        print(self.data3[0][0])
        thread1 = threading.Thread(target=self.imageAPI, args=(f'{self.data1[0][0][1]} with {self.data1[1][1]} ', 'word_a.jpg'))
        thread2 = threading.Thread(target=self.imageAPI, args=(f'{self.data2[0][0][1]} with {self.data2[1][1]} {self.data2[2][0]} ', 'word_b.jpg'))
        thread3 = threading.Thread(target=self.imageAPI, args=(f'{self.data3[2][0]} {self.data3[2][1]}{self.data3[0][0][1]} with {self.data3[1][1]} {self.data3[2][0]} ', 'word_c.jpg'))
        thread1 = threading.Thread(target=self.imageAPI('vocaloid[anime style]'))
        thread1.start()
        thread2.start()
        thread3.start()
        
        thread1.join()
        thread2.join()
        thread3.join()
        loading_frame.destroy()
        Main()

    def imageAPI(self,text, jpg):
        print('imageAPI-Start')
        #'''
        r = requests.post(
            "https://api.deepai.org/api/text2img",
            data={
                'text': text,
            },
            headers={'api-key': '3513466b-158b-4fca-98e7-b212f5aa25f7'}
        )

        APIdata = r.json()
        print(APIdata)
        imageURL = APIdata['output_url']

        response = requests.get(imageURL)

        file = open(jpg,"wb")
        for chunk in response.iter_content(100000):
            file.write(chunk)
        file.close()
        #'''
