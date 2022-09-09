from curses.ascii import isalnum
import tkinter as tk
import tkinter.ttk as ttk
from loop import Loop
from PIL import Image, ImageTk
import threading
import requests
import json
import os

class Sab:
    def __init__(self):
        print('API_frame-Start')
        global sab_frame
        sab_frame = ttk.Frame()
        sab_frame.pack(fill=tk.BOTH, pady=0, padx=0)
        self.canvas = tk.Canvas(sab_frame, width=1400, height=800, bg="#4169e1")
        self.canvas.pack()

        self.file = ""

        self.main()
    
    def lop(self):
        sab_frame.destroy()
        Loop()
    def main(self):
        self.canvas.create_window(1335, 762,window=ttk.Button(self.canvas, text="終了", command=self.lop, padding=[5,4,5,4]), anchor="center")

        rect1bg = self.canvas.create_rectangle(62*1, 63, 256+82, 256+82+1, fill = "#0e1833")
        rect2bg = self.canvas.create_rectangle(62*2+266, 63, (256+77)*2+1, 256+82, fill = "#0e1833")
        rect3bg = self.canvas.create_rectangle(62*3+266*2, 63, (256+75)*3+2, 256+82, fill = "#0e1833")
        rect4bg = self.canvas.create_rectangle(62*4+266*3, 63, (256+74.5)*4+3, 256+82, fill = "#0e1833")

       
        textbg = self.canvas.create_rectangle(100, 390+60, 1300, 460+60, fill="#668fff", width=0)
        text = self.canvas.create_text(700, 420, text=f'', font=("HG丸ｺﾞｼｯｸM-PRO",40), tag="text")
        self.img = Image.open('word_n.jpg')
        self.tk_imgUL = ImageTk.PhotoImage(self.img.crop((0,0,256,256)))
        self.tk_imgUR = ImageTk.PhotoImage(self.img.crop((256,0,512,256)))
        self.tk_imgDL = ImageTk.PhotoImage(self.img.crop((0,255,257,512)))
        self.tk_imgDR = ImageTk.PhotoImage(self.img.crop((255,256,513,513)))

        self.canvas.create_image(73*1, 73 , anchor = tk.NW, image=self.tk_imgUL, tag='UL')        
        self.canvas.create_image(73*2+256*1-1, 73 , anchor = tk.NW, image=self.tk_imgUR, tag='UR')        
        self.canvas.create_image(73*3+256*2-2, 73 , anchor = tk.NW, image=self.tk_imgDL, tag='DL')        
        self.canvas.create_image(73*4+256*3-3, 73 , anchor = tk.NW, image=self.tk_imgDR, tag='DR')

        rect1 = self.canvas.create_rectangle(72*1, 73, 256+71, 256+72+1, fill = "#ccdaff")
        rect2 = self.canvas.create_rectangle(72*2+256, 73, (256+72)*2+1, 256+72, fill = "#ccdaff")
        rect3 = self.canvas.create_rectangle(72*3+256*2, 73, (256+72)*3+2, 256+72, fill = "#ccdaff")
        rect4 = self.canvas.create_rectangle(72*4+256*3, 73, (256+72)*4+3, 256+72, fill = "#ccdaff")

        def imageSET():
            self.img = Image.open('word_n.jpg')
            self.tk_imgUL = ImageTk.PhotoImage(self.img.crop((0,0,256,256)))
            self.tk_imgUR = ImageTk.PhotoImage(self.img.crop((256,0,512,256)))
            self.tk_imgDL = ImageTk.PhotoImage(self.img.crop((0,255,257,512)))
            self.tk_imgDR = ImageTk.PhotoImage(self.img.crop((255,256,513,513)))
            self.canvas.create_image(73*1, 73 , anchor = tk.NW, image=self.tk_imgUL, tag='UL')        
            self.canvas.create_image(73*2+256*1-1, 73 , anchor = tk.NW, image=self.tk_imgUR, tag='UR')        
            self.canvas.create_image(73*3+256*2-2, 73 , anchor = tk.NW, image=self.tk_imgDL, tag='DL')        
            self.canvas.create_image(73*4+256*3-3, 73 , anchor = tk.NW, image=self.tk_imgDR, tag='DR')

            self.canvas.delete(rect1)
            self.canvas.delete(rect2)
            self.canvas.delete(rect3)
            self.canvas.delete(rect4)

            b1 = self.canvas.create_window(200*1+130*0,390-1500,window=ttk.Button(self.canvas, text="保存", command=lambda:imgb1(0,0,256,256), padding=[15,8,15,8]), anchor="center")
            b2 = self.canvas.create_window(200*2+130*1,390-1500,window=ttk.Button(self.canvas, text="保存", command=lambda:imgb1(256,0,512,256), padding=[15,8,15,8]), anchor="center")
            b3 = self.canvas.create_window(200*3+130*2,390-1500,window=ttk.Button(self.canvas, text="保存", command=lambda:imgb1(0,256,256,512), padding=[15,8,15,8]), anchor="center")
            b4 = self.canvas.create_window(200*4+130*3,390-1500,window=ttk.Button(self.canvas, text="保存", command=lambda:imgb1(256,256,512,512), padding=[15,8,15,8]), anchor="center")

            self.canvas.move(b1, 0, 1500)
            self.canvas.move(b2, 0, 1500)
            self.canvas.move(b3, 0, 1500)
            self.canvas.move(b4, 0, 1500)
            k = tk.Entry(self.canvas, width=42, justify="center" ,font=("HG丸ｺﾞｼｯｸM-PRO",30))
            k.place(x=620, y=580, anchor=tk.CENTER)

            k.insert(tk.END, "保存するファイル名を指定してください")

            def file_set():
                self.file = k.get()
                k.delete(0, tk.END)
                k.insert(tk.END, f'指定済 >> {self.file}.jpg')
        

            l = self.canvas.create_window(
            1180, 580-1500, window=tk.Button(self.canvas, text='指定', command=file_set,padx=50, pady=20 )
            )

            self.canvas.move(l, 0, 1500)
        
            def imgb1(a,b,c,d):
                if self.file == "":
                    k.delete(0, tk.END)
                    k.insert(tk.END, "英数字のみでファイル名を指定してください")
                elif self.file.isalnum():
                    img = Image.open('word_n.jpg')
                    trimmed = img.crop((a,b,c,d))
                    trimmed.save(f'API_image/{self.file}.jpg')
                    k.delete(0, tk.END)
                    k.insert(tk.END, "保存完了：別のファイル名を指定してください")
                else:
                    k.delete(0, tk.END)
                    k.insert(tk.END, "英数字のみでファイル名を指定してください")


            b1 = self.canvas.create_window(200*1+130*0,390-1500,window=ttk.Button(self.canvas, text="保存", command=lambda:imgb1(0,0,256,256), padding=[15,8,15,8]), anchor="center")
            b2 = self.canvas.create_window(200*2+130*1,390-1500,window=ttk.Button(self.canvas, text="保存", command=lambda:imgb1(256,0,512,256), padding=[15,8,15,8]), anchor="center")
            b3 = self.canvas.create_window(200*3+130*2,390-1500,window=ttk.Button(self.canvas, text="保存", command=lambda:imgb1(0,256,256,512), padding=[15,8,15,8]), anchor="center")
            b4 = self.canvas.create_window(200*4+130*3,390-1500,window=ttk.Button(self.canvas, text="保存", command=lambda:imgb1(256,256,512,512), padding=[15,8,15,8]), anchor="center")



        def imageAPI(text, jpg):
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
            e.delete(0, tk.END)
            e.insert(tk.END , '生成完了')
            imageSET()
        
            

        def translation():
            api_url = f'https://script.google.com/a/std.it-college.ac.jp/macros/s/AKfycbyoy0_JhHrFtWb5GF_m6eDYbGGvQSZe16aHu9W8QQaw4e5p4LUE/exec?text={e.get()}&source=ja&target=en'
            res = requests.get(api_url)
            text = res.text
            data = json.loads(text)
            print(data)
            thread1 = threading.Thread(target=imageAPI, args=(data['text'], 'word_n.jpg'))
            thread1.start()
            e.delete(0, tk.END)
            e.insert(tk.END, '生成中')


        def entry():
            self.canvas.delete("text")
            print(e.get())
            text = self.canvas.create_text(700, 480, text=f'{e.get()}', font=("HG丸ｺﾞｼｯｸM-PRO",40), tag="text")
            translation()


        e = tk.Entry(self.canvas, width=42, justify="center" ,font=("HG丸ｺﾞｼｯｸM-PRO",30))
        e.place(x=620, y=670, anchor=tk.CENTER)
        e.insert(tk.END, '画像生成する文字列を入力してください')

        b = self.canvas.create_window(
            1180, 670, window=tk.Button(self.canvas, text='生成', command=entry,padx=50, pady=20 )
            )


        self.canvas.create_line(
            15, 15,
            15, 800-15,
            1400-15, 800-15,
            1400-15, 15,
            15, 15,
            width=3, fill="#ccdaff"
        )

        sab_frame.mainloop()