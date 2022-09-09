from tkinter import *
import tkinter.ttk as ttk
from tkinter import font
from random import shuffle
import json
class Loop:
    def __init__(self):
        global frame
        self.frame = ttk.Frame()
        self.frame.pack(fill=BOTH, pady=0, padx=0)

        self.canvas = Canvas(self.frame, width=1400, height=800, bg="#4169e1")
        self.canvas.create_window(1335, 762,window=ttk.Button(self.canvas, text="終了", command=exit, padding=[5,4,5,4]), anchor="center")
        textbg = self.canvas.create_rectangle(700-300, 250-50, 700+300, 250+60, fill="#668fff", width=0)
        text = self.canvas.create_text(700, 250, text=f'画像生成API', font=("HG丸ｺﾞｼｯｸM-PRO",60), tag="text")
        line = self.canvas.create_line(
            15, 15,
            15, 800-15,
            1400-15, 800-15,
            1400-15, 15,
            15, 15,
            width=3, fill="#ccdaff"
        )


        self.canvas.pack()
        myfont = font.Font(self.canvas, family="System", size=30)
        style = ttk.Style()
        style.configure("office.TButton", font=myfont)

        self.canvas.create_window(420,550,window=ttk.Button(self.canvas, text="APIで遊ぶ", command=self.lloading, padding=[100,30,100,30], style="office.TButton"), anchor="center")
        self.canvas.create_window(920,550,window=ttk.Button(self.canvas, text="APIを使う", command=self.ssab, padding=[100,30,100,30], style="office.TButton"), anchor="center")


        def word(file, test):
            file_fill = open(file, 'w')
            file_fill.write(f'{test}')
        #'''
        word('word_a.txt', self.ramdomWords1())
        word('word_b.txt', self.ramdomWords1())
        word('word_c.txt', self.ramdomWords1())
        #'''
        self.frame.mainloop()

    def ramdomWords1(self):
        building = [ 
            ['図書館','library'], ['塔','tower'], ['学校','school'], 
            ['博物館','museum'], ['病院','hospital'], ['城','castle'], 
            ['駅','station'], ['教会','association'], ['神社','shrine']
        ], ['建物']
        views = [
            ['星空','starry'], ['地平線','horizon'], ['夕焼け','sunset'],
            ['雨','rain'], ['竜巻','turnado'], ['雷','Thunder'], 
            ['日食', 'solareclipse'], ['虹', 'Rainbow'], ['銀河', 'galaxy']
        ]
        styles = [
            ['horror style', 'ホラー風'], ['gothic style', 'ゴシック風'], 
            ['future style', '近未来風'], ['picasso style', 'ピカソ風']
        ]
        state = [
            ['broken', '壊れている'], ['floating', '浮いている'], 
            ['burnubg', '燃えている'], ['melting', '溶けている'], 
        ]
        shuffle(building[0])
        shuffle(views)
        shuffle(styles)
        shuffle(state)
        words = \
            [building[0][0], building[1]], \
            [views[0][0], views[0][1]], \
            [styles[0][0], styles[0][1]], [state[0][0], state[0][1]]
        return json.dumps(words, ensure_ascii=False)

    def lloading(self):
        self.frame.destroy()
        from loading import Loading
        Loading()
    
    def ssab(self):
        self.frame.destroy()
        from sab import Sab
        Sab()