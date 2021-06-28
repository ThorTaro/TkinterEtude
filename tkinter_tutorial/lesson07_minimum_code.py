"""
    lesson07 最小限の計算機

    今回の課題の最低ゴールライン(想定)
    足し算のみ，かつ，ボタン連打の結果の正常性は担保しない状態
    課題の順番としては，
    1. 足し算のみの計算機の作成
    2. 他の演算にも対応させる
    3. ボタン連打を防げるようにする
    4. その他(演算過程をディスプレイに表示する，小数点対応，など実際の計算機に寄せていく)
    といったレベルを想定
"""

import tkinter as tk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.display_value = tk.StringVar(value='0')
        self.first_value = '0'
        self.second_value = '0'
        self.is_plus_button_clicked = False
        self.__set_widget()

    # view関連の初期化処理
    def __set_widget(self):
        self.title('Simple Calculator')

        # root frame
        self.root_frame = tk.Frame(master=self)
        self.root_frame.grid(row=0,
                            column=0,
                            sticky=tk.NSEW,
                            padx='5',
                            pady='5')

        # 出力結果表示用ラベル
        self.display_label = tk.Label(master=self.root_frame,
                                    textvariable=self.display_value,
                                    anchor=tk.E,
                                    fg='black',
                                    bg='white',
                                    font=('', '20'))
        self.display_label.grid(row=0,column=0,columnspan=4,sticky=tk.EW)

        # 数字ボタン
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

        # 演算子ボタン
        self.plus_button = tk.Button(master=self.root_frame, text='+', width='2')
        self.plus_button.grid(row=4, column=3)
        self.plus_button.bind('<Button-1>', self.__plus_button_clicked)

        self.equal_button = tk.Button(master=self.root_frame, text='=', width='2')
        self.equal_button.grid(row=5, column=3)
        self.equal_button.bind('<Button-1>', self.__equal_button_clicked)

        self.clear_button = tk.Button(master=self.root_frame, text='AC', width='2')
        self.clear_button.grid(row=1, column=0)
        self.clear_button.bind('<Button-1>', self.__clear_button_clicked)

    # 番号キーが押された時のコールバック
    def __num_button_clicked(self, event):
        clicked_num = event.widget['text']

        if self.display_value.get() == '0' or self.is_plus_button_clicked:
            self.display_value.set(clicked_num)
        else:
            self.display_value.set(self.display_value.get() + clicked_num)

        self.is_plus_button_clicked = False

    # 演算子ボタンが押された時のコールバック
    def __plus_button_clicked(self, event):
        self.first_value = self.display_value.get()
        self.is_plus_button_clicked = True

    # =ボタンが押された時のコールバック
    def __equal_button_clicked(self, event):
        self.second_value = self.display_value.get()
        result = int(self.first_value) + int(self.second_value)
        self.display_value.set(str(result))

    # クリアーキーが押された時のコールバック
    def __clear_button_clicked(self, event):
        self.display_value.set('0')
        self.first_value = '0'
        self.second_value = '0'
        self.is_plus_button_clicked = False


if __name__ == '__main__':
    my_calculator = Calculator()
    my_calculator.mainloop()