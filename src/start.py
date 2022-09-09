from tkinter import *
from random import shuffle
import json
from tkinter import font
import tkinter.ttk as ttk
from loading import Loading
from sab import Sab
class Start:
    def __init__(self):
        print('Menu_frame-Start')
        self.root = Tk()
        self.root.title("Text to Image API")
        self.root.geometry("1400x800")
        self.root.resizable(False, False)
        global frame
        self.frame = ttk.Frame(self.root)
        self.frame.pack(fill = BOTH, pady=False)

        self.canvas = Canvas(self.frame, width=1400, height=800, bg="#4169e1")
        self.canvas.create_window(1335, 762,window=ttk.Button(self.canvas, text="終了", command=self.root.destroy, padding=[5,4,5,4]), anchor="center")
        textbg = self.canvas.create_rectangle(700-380, 250-60, 700+380, 250+80, fill="#668fff", width=0)
        text = self.canvas.create_text(700, 250, text=f'画像生成API', font=("HG丸ｺﾞｼｯｸM-PRO",90), tag="text")
        line = self.canvas.create_line(
            15, 15,
            15, 800-15,
            1400-15, 800-15,
            1400-15, 15,
            15, 15,
            width=3, fill="#ccdaff"
        )


        self.canvas.pack()
        myfont = font.Font(self.root, family="System", size=30)
        style = ttk.Style()
        style.configure("office.TButton", font=myfont)

        self.canvas.create_window(420,550,window=ttk.Button(self.canvas, text="APIで遊ぶ", command=self.loading, padding=[100,30,100,30], style="office.TButton"), anchor="center")
        self.canvas.create_window(920,550,window=ttk.Button(self.canvas, text="APIを使う", command=self.sab, padding=[100,30,100,30], style="office.TButton"), anchor="center")

        def word(file, test):
            file_fill = open(file, 'w')
            file_fill.write(f'{test}')
        word('word_a.txt', self.ramdomWords1())
        word('word_b.txt', self.ramdomWords1())
        word('word_c.txt', self.ramdomWords1())

        self.root.mainloop()

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

    def loading(self):
        # self.frame.destroy()
        self.frame.destroy()
        Loading()

    def sab(self):
        self.frame.destroy()
        Sab()
Start()

'''
    if __name__ == "__main__":
        global root

        def word(file, test):
            file_fill = open(file, 'w')
            file_fill.write(f'{test}')
        word('word_a.txt', "noneeeeeeeeee")
        word('word_b.txt', "eeeee")
        word('word_c.txt', "eee")

        root = Tk()
        root.title("test")
        root.geometry("1400x800")
        root.resizable(False, False)
        global frame
        frame = ttk.Frame(root)
        frame.pack(fill = BOTH, pady=False)

        canvas = Canvas(root, width=1400, height=800, bg="blue")
        canvas.pack()
        canvas.create_window(300,650,window=ttk.Button(canvas, text="window", command=loading, padding=[200,60,200,60]), anchor="center")

        root.mainloop()
'''
