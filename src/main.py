import tkinter as tk
import json 
import tkinter.ttk as ttk
import json
from time import sleep
from PIL import Image, ImageTk
from loop import Loop
class Main:
    def __init__(self):
        print('Game_frame-Start')
        fo = open('word_a.txt', 'r')
        self.data1 = json.loads(fo.read())
        fo.close()

        go = open('word_b.txt', 'r')
        self.data2 = json.loads(go.read())
        go.close()

        co = open('word_c.txt', 'r')
        self.data3 = json.loads(co.read())
        co.close()

        self.Life = 3
        self.Life_text = ""
        self.b1,self.b2,self.b3,self.b4 = 1,1,1,1
        self.lv = 1

        global top_frame
        top_frame = ttk.Frame()
        top_frame.pack(fill=tk.BOTH, pady=0, padx=0)

        self.canvas = tk.Canvas(top_frame, width=1400, height=800, bg="#4169e1")
        self.main()
    
    def func(self):
        top_frame.destroy()
        Loop()

    def main(self):
        #print(self.data1)

        building = [ 
            ['図書館','library'], ['塔','tower'], ['学校','school'], 
            ['博物館','museum'], ['病院','hospital'], ['城','castle'], 
            ['駅','station'], ['教会','association'], ['神社','shrine']
        ]

        # 変数
        img1 = Image.open('word_a.jpg')
        tk1_imgUL = ImageTk.PhotoImage(img1.crop((0,0,256,256)))
        tk1_imgUR = ImageTk.PhotoImage(img1.crop((256,0,512,256)))
        tk1_imgDL = ImageTk.PhotoImage(img1.crop((0,256,256,512)))
        tk1_imgDR = ImageTk.PhotoImage(img1.crop((256,256,512,512)))

        img2 = Image.open('word_b.jpg')
        tk2_imgUL = ImageTk.PhotoImage(img2.crop((0,0,256,256)))
        tk2_imgUR = ImageTk.PhotoImage(img2.crop((256,0,512,256)))
        tk2_imgDL = ImageTk.PhotoImage(img2.crop((0,256,256,512)))
        tk2_imgDR = ImageTk.PhotoImage(img2.crop((256,256,512,512)))

        img3 = Image.open('word_c.jpg')
        tk3_imgUL = ImageTk.PhotoImage(img3.crop((0,0,256,256)))
        tk3_imgUR = ImageTk.PhotoImage(img3.crop((256,0,512,256)))
        tk3_imgDL = ImageTk.PhotoImage(img3.crop((0,256,256,512)))
        tk3_imgDR = ImageTk.PhotoImage(img3.crop((256,256,512,512)))
        
        # パッケージ
        self.canvas.pack()

        line = self.canvas.create_line(
            15, 15,
            15, 800-15,
            1400-15, 800-15,
            1400-15, 15,
            15, 15,
            width=3, fill="#ccdaff"
        )

        rect1bg = self.canvas.create_rectangle(62*1, 63, 256+82, 256+82+1, fill = "#0e1833")
        rect2bg = self.canvas.create_rectangle(62*2+266, 63, (256+77)*2+1, 256+82, fill = "#0e1833")
        rect3bg = self.canvas.create_rectangle(62*3+266*2, 63, (256+75)*3+2, 256+82, fill = "#0e1833")
        rect4bg = self.canvas.create_rectangle(62*4+266*3, 63, (256+74.5)*4+3, 256+82, fill = "#0e1833")
        
        #3img
        self.canvas.create_image(73*1, 73 , anchor = tk.NW, image=tk3_imgUL, tag='3UL')        
        self.canvas.create_image(73*2+256*1, 73 , anchor = tk.NW, image=tk3_imgUR, tag='3UR')        
        self.canvas.create_image(73*3+256*2, 73 , anchor = tk.NW, image=tk3_imgDL, tag='3DL')        
        self.canvas.create_image(73*4+256*3, 73 , anchor = tk.NW, image=tk3_imgDR, tag='3DR')
        #2img
        self.canvas.create_image(73*1, 73 , anchor = tk.NW, image=tk2_imgUL, tag='2UL')        
        self.canvas.create_image(73*2+256*1, 73 , anchor = tk.NW, image=tk2_imgUR, tag='2UR')        
        self.canvas.create_image(73*3+256*2, 73 , anchor = tk.NW, image=tk2_imgDL, tag='2DL')        
        self.canvas.create_image(73*4+256*3, 73 , anchor = tk.NW, image=tk2_imgDR, tag='2DR')
        #1img
        self.canvas.create_image(73*1, 73 , anchor = tk.NW, image=tk1_imgUL, tag='1UL')        
        self.canvas.create_image(73*2+256*1, 73 , anchor = tk.NW, image=tk1_imgUR, tag='1UR')        
        self.canvas.create_image(73*3+256*2, 73 , anchor = tk.NW, image=tk1_imgDL, tag='1DL')        
        self.canvas.create_image(73*4+256*3, 73 , anchor = tk.NW, image=tk1_imgDR, tag='1DR')

        rect1 = self.canvas.create_rectangle(72*1, 73, 256+71, 256+72+1, fill = "white")
        rect2 = self.canvas.create_rectangle(72*2+256, 73, (256+72)*2+1, 256+72, fill = "white")
        rect3 = self.canvas.create_rectangle(72*3+256*2, 73, (256+72)*3+2, 256+72, fill = "white")
        rect4 = self.canvas.create_rectangle(72*4+256*3, 73, (256+72)*4+3, 256+72, fill = "white")

        def del_b_all(): 
            button_list = [self.b1, self.b2, self.b3, self.b4, button1, button2, button3, button4]
            for i in range(4):
                if button_list[i] == 1:
                    self.canvas.move(button_list[i+4], 800,800)

        def set_buttun():
            print('All_Reset')
            button_list = [self.b1, self.b2, self.b3, self.b4, button1, button2, button3, button4]
            for i in range(4):
                if button_list[i] == 1:
                    self.canvas.move(button_list[i+4], -800,-800)
            
                    
                
            
        def del_rect1():
            print('Image_1-open')
            self.canvas.move(rect1, 800, 800)
            self.b1 = 0
            del_b_all()
            self.canvas.move(button1, 800,800)
        def del_rect2():
            print('Image_2-open')
            self.canvas.move(rect2, 800, 800)
            self.b2 = 0
            del_b_all()
            self.canvas.move(button2, 800,800)
        def del_rect3():
            print('Image_3-open')
            self.canvas.move(rect3, 800, 800)
            self.b3 = 0
            del_b_all()
            self.canvas.move(button3, 800,800)
        def del_rect4():
            print('Image_4-open')
            self.canvas.move(rect4, 800, 800)
            self.b4 = 0
            del_b_all()
            self.canvas.move(button4, 800,800)

        def failed():
            self.canvas.delete("all")
            def lop(evt):
                top_frame.destroy()
                Loop()
            self.canvas.create_text(700,390, text="GAME OVER", font=("HG丸ｺﾞｼｯｸM-PRO", 90))
            self.canvas.create_text(700,455, text="enter to main menu", font=("HG丸ｺﾞｼｯｸM-PRO", 30))
            self.canvas.bind_all("<KeyPress-Return>", lop)

        def clear(evt):
            b_list = [self.b1, self.b2, self.b3, self.b4]
            rect_list = [rect1, rect2, rect3, rect4]
            button_list = [button1, button2, button3, button4]
            self.Life = 3

            #sleep(10)
            self.canvas.delete('rect_load')

            for i in range(4):
                if b_list[i] == 0:
                    self.canvas.move(rect_list[i], -800, -800)
                self.canvas.move(button_list[i], -800, -800)
            self.b1, self.b2, self.b3, self.b4 =1,1,1,1
            if self.lv == 3:
                def lop(evt):
                    top_frame.destroy()
                    Loop()
                self.canvas.create_text(700,455, text="enter to main menu", font=("HG丸ｺﾞｼｯｸM-PRO", 30))
                self.canvas.bind_all("<KeyPress-Return>", lop)

            if self.lv == 2:
                self.canvas.delete('2UL')
                self.canvas.delete('2UR')
                self.canvas.delete('2DL')
                self.canvas.delete('2DR')
                self.canvas.move(text2, -800, -800)
                self.canvas.move(text3, 800, 800)
                self.canvas.move(combo, 800, 800)
                self.canvas.delete('clear')
                self.canvas.delete('lvc')

                self.lv = 3

            if self.lv == 1:
                self.canvas.delete('1UL')
                self.canvas.delete('1UR')
                self.canvas.delete('1DL')
                self.canvas.delete('1DR')
                self.canvas.move(text1, -800, -800)
                self.canvas.move(text2, 800, 800)
                self.canvas.move(combo, 800, 800)
                self.canvas.delete('clear')
                self.canvas.delete('lvc')
                
                self.lv = 2

            self.canvas.delete(self.stage_lv_date)
            self.stage_lv_date = self.canvas.create_text(1100, 573, text=f'    Lv. {self.lv}', font=("HG丸ｺﾞｼｯｸM-PRO",40))
            self.canvas.delete(self.Life_data)
            self.Life_data = self.canvas.create_text(1100, 653, text=f'     {"♥" * self.Life}', font=("HG丸ｺﾞｼｯｸM-PRO",40), fill="red")
            

        




        #canvas.move(rect4, 10000, 10000)
        button1 = self.canvas.create_window(256*0+72*0+73+13,73+15,window=ttk.Button(self.canvas, command=del_rect1, padding=[72, 130, 80, 72], ), anchor="nw")
        button2 = self.canvas.create_window(256*1+72*1+73+13,73+15,window=ttk.Button(self.canvas, command=del_rect2, padding=[72, 130, 80, 72], ), anchor="nw")
        button3 = self.canvas.create_window(256*2+72*2+73+15,73+15,window=ttk.Button(self.canvas, command=del_rect3, padding=[72, 130, 80, 72], ), anchor="nw")
        button4 = self.canvas.create_window(256*3+72*3+73+15,73+15,window=ttk.Button(self.canvas, command=del_rect4, padding=[72, 130, 80, 72], ), anchor="nw")

        textbg = self.canvas.create_rectangle(100, 390, 1300, 460, fill="#668fff", width=0)
        datebg = self.canvas.create_rectangle(720, 510, 1325, 730, fill="#ccd9ff", width=3, outline="#334680")
        text1 = self.canvas.create_text(700, 420, text=f'{self.data1[1][0]}の映る<建物>', font=("HG丸ｺﾞｼｯｸM-PRO",40))
        text2 = self.canvas.create_text(700-800, 420-800, text=f'{self.data2[2][1]}の{self.data2[1][0]}の映る<建物>', font=("HG丸ｺﾞｼｯｸM-PRO",36))
        text3 = self.canvas.create_text(700-800, 420-800, text=f'{self.data3[2][1]}の{self.data3[1][0]}の映る{self.data3[3][1]}<建物>', font=("HG丸ｺﾞｼｯｸM-PRO",36))
        self.Life_text = self.canvas.create_text(943, 650, text=f'  Life  =', font=("HG丸ｺﾞｼｯｸM-PRO",40))
        self.Life_data = self.canvas.create_text(1100, 653, text=f'     {"♥" * self.Life}', font=("HG丸ｺﾞｼｯｸM-PRO",40), fill="red")
        self.stage_lv = self.canvas.create_text(918, 570, text=f'  Stage  =', font=("HG丸ｺﾞｼｯｸM-PRO",40))
        self.stage_lv_date = self.canvas.create_text(1100, 573, text=f'    Lv. {self.lv}', font=("HG丸ｺﾞｼｯｸM-PRO",40))
        
        style = ttk.Style()
        style.theme_use('default')
        allTheme = style.theme_names()
        print(allTheme)
        style.configure("office.TCombobox", foreground = "black")

        comboboxx = ttk.Combobox(
            self.canvas, values=building, state='readonly',
            font=("HG丸ｺﾞｼｯｸM-PRO",26), height=9, justify="center", 
            style="office.TCombobox", 
            )

        combo = self.canvas.create_window(400,540,window=comboboxx, anchor="center")
        def word_test(evt):
            if comboboxx.get().split()[0] == self.data1[0][0][0] and self.lv == 1:
                print("Stage_Lv1-clear")
                self.canvas.create_rectangle(0, 0, 1400 , 800, fill='#668fff', tag='rect_load')
                self.canvas.create_text(700,380, text="STAGE CLEAR", font=("HG丸ｺﾞｼｯｸM-PRO", 90), tag='clear')
                self.canvas.create_text(700,455, text="enter to next level", font=("HG丸ｺﾞｼｯｸM-PRO", 30), tag="lvc")
                self.canvas.move(combo, -800, -800)
                self.canvas.bind_all("<KeyPress-Return>", clear)

            elif comboboxx.get().split()[0] == self.data2[0][0][0] and self.lv == 2:
                print("Stage_Lv2-clear")
                self.canvas.create_rectangle(0, 0, 1400 , 800, fill='#668fff', tag='rect_load')
                self.canvas.create_text(700,380, text="STAGE CLEAR", font=("HG丸ｺﾞｼｯｸM-PRO", 90), tag='clear')
                self.canvas.create_text(700,455, text="enter to next level", font=("HG丸ｺﾞｼｯｸM-PRO", 30), tag="lvc")
                self.canvas.move(combo, -800, -800)
                self.canvas.bind_all("<KeyPress-Return>", clear)
            
            elif comboboxx.get().split()[0] == self.data3[0][0][0] and self.lv == 3:
                print("Stage_Lv3-clear")
                self.canvas.delete("all")
                self.canvas.create_text(700,380, text="congratulations!!", font=("HG丸ｺﾞｼｯｸM-PRO", 90))
                self.canvas.create_text(700,455, text="enter to main menu", font=("HG丸ｺﾞｼｯｸM-PRO", 30))
                def lop(evt):
                    top_frame.destroy()
                    Loop()
                self.canvas.bind_all("<KeyPress-Return>", lop)


            else:
                print("Damage 'Life -1'")
                self.Life -= 1
                self.canvas.delete(self.Life_data)
                #self.Life_text = self.canvas.create_text(930, 670, text=f'Life : ', font=("HG丸ｺﾞｼｯｸM-PRO",40))
                self.Life_data = self.canvas.create_text(1100, 653, text=f'     {"♥" * self.Life}', font=("HG丸ｺﾞｼｯｸM-PRO",40), fill="red")
                set_buttun()
                if self.Life == 0:
                    print('GAME OVER') 
                    failed()

        comboboxx.bind('<<ComboboxSelected>>', word_test)

        top_frame.mainloop()
