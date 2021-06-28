"""
    lesson06 ボタンのイベントハンドリング
"""

import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        # StringVarはtk.Frame系列の値をバインドして使えるクラス
        # entryなどの入力に応じてStringVarが変わったり，StringVarの値を変更することでframeの表示が自動で変更される．
        # intやfloatも用意されているか，今回はstring
        self.display_value = tk.StringVar(value='0')
        self.__set_widget()

    def __set_widget(self):
        self.title('event handling')

        # root frame
        self.root_frame = tk.Frame(master=self)
        self.root_frame.grid(row=0,
                            column=0,
                            sticky=tk.NSEW,
                            padx='5',
                            pady='5')

        # 出力結果表示用ラベル
        # StringVarをバインドさせるためには，textvariableの引数として渡す必要がある
        self.display_label = tk.Label(master=self.root_frame,
                                    textvariable=self.display_value,
                                    anchor=tk.E,
                                    fg='black',
                                    bg='white',
                                    font=('', '20'))
        self.display_label.grid(row=0,column=0,columnspan=4,sticky=tk.EW)

        # 各種ボタン
        # bind()でイベントとコールバックを紐づけることができる
        # 第一引数の'<Button-1>'は，イベントのトリガーとなる動作の定義，この場合は左クリックを意味する．
        # 第二引数は紐づけられるコールバック
        self.button9 = tk.Button(master=self.root_frame, text='9', width='2')
        self.button9.grid(row=2, column=2)
        self.button9.bind('<Button-1>', self.__num_button_clicked)

        self.button8 = tk.Button(master=self.root_frame, text='8', width='2')
        self.button8.grid(row=2, column=1)
        self.button8.bind('<Button-1>', self.__num_button_clicked)

        self.button7 = tk.Button(master=self.root_frame, text='7', width='2')
        self.button7.grid(row=2, column=0)
        self.button7.bind('<Button-1>', self.__num_button_clicked)

        self.button6 = tk.Button(master=self.root_frame, text='6', width='2')
        self.button6.grid(row=3, column=2)
        self.button6.bind('<Button-1>', self.__num_button_clicked)

        self.button5 = tk.Button(master=self.root_frame, text='5', width='2')
        self.button5.grid(row=3, column=1)
        self.button5.bind('<Button-1>', self.__num_button_clicked)

        self.button4 = tk.Button(master=self.root_frame, text='4', width='2')
        self.button4.grid(row=3, column=0)
        self.button4.bind('<Button-1>', self.__num_button_clicked)

        self.button3 = tk.Button(master=self.root_frame, text='3', width='2')
        self.button3.grid(row=4, column=2)
        self.button3.bind('<Button-1>', self.__num_button_clicked)

        self.button2 = tk.Button(master=self.root_frame, text='2', width='2')
        self.button2.grid(row=4, column=1)
        self.button2.bind('<Button-1>', self.__num_button_clicked)

        self.button1 = tk.Button(master=self.root_frame, text='1', width='2')
        self.button1.grid(row=4, column=0)
        self.button1.bind('<Button-1>', self.__num_button_clicked)

        self.button0 = tk.Button(master=self.root_frame, text='0')
        self.button0.grid(row=5, column=0, columnspan=2, sticky=tk.EW)
        self.button0.bind('<Button-1>', self.__num_button_clicked)

        self.plus_button = tk.Button(master=self.root_frame, text='+', width='2')
        self.plus_button.grid(row=4, column=3)

        self.equal_button = tk.Button(master=self.root_frame, text='=', width='2')
        self.equal_button.grid(row=5, column=3)

        self.clear_button = tk.Button(master=self.root_frame, text='C', width='2')
        self.clear_button.grid(row=1, column=0)
        self.clear_button.bind('<Button-1>', self.__clear_button_clicked)

    # 番号キーが押された時のコールバック
    def __num_button_clicked(self, event):
        # イベントの発火元のwidgetのテキストを取得可能
        clicked_num = event.widget['text']

        # StringVarはget(),set()でしかアクセスができない
        self.display_value.set(self.display_value.get() + clicked_num)

    # クリアーキーが押された時のコールバック
    # eventは使わないが，この形式でないとbindができないため定義しておく
    def __clear_button_clicked(self, event):
        self.display_value.set('0')


if __name__ == '__main__':
    my_calculator = Calculator()
    my_calculator.mainloop()