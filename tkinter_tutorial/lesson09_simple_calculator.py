"""
    lesson09 予期しない挙動を制御

    シンプルな計算機の完成形
    四則演算ができるようにする
    状態遷移が増えるので，リファクタリングも行う
"""

import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.display_value = tk.StringVar(value='0')
        self.first_value = '0'
        self.second_value = '0'
        # 演算子ボタンが増えるたびにフラグを増やすのは効率が悪いので，一つのフラグに集約
        self.is_op_button_clicked = False
        # こちらの変数をNoneで初期化して，Noneチェックをすれば上のフラグを使わずに済むが，
        # Noneを取り扱わない予定なので分ける
        self.operator = ''
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
        self.div_button = tk.Button(master=self.root_frame, text='÷', width='2')
        self.div_button.grid(row=1, column=3)
        self.div_button.bind('<Button-1>', self.__op_button_clicked)

        self.multi_button = tk.Button(master=self.root_frame, text='×', width='2')
        self.multi_button.grid(row=2, column=3)
        self.multi_button.bind('<Button-1>', self.__op_button_clicked)

        self.sub_button = tk.Button(master=self.root_frame, text='-', width='2')
        self.sub_button.grid(row=3, column=3)
        self.sub_button.bind('<Button-1>', self.__op_button_clicked)

        self.plus_button = tk.Button(master=self.root_frame, text='+', width='2')
        self.plus_button.grid(row=4, column=3)
        self.plus_button.bind('<Button-1>', self.__op_button_clicked)

        self.equal_button = tk.Button(master=self.root_frame, text='=', width='2')
        self.equal_button.grid(row=5, column=3)
        self.equal_button.config(state=tk.DISABLED)
        self.equal_button.bind('<Button-1>', self.__equal_button_clicked)

        self.clear_button = tk.Button(master=self.root_frame, text='AC', width='2')
        self.clear_button.grid(row=1, column=0)
        self.clear_button.bind('<Button-1>', self.__clear_button_clicked)

    # 番号キーが押された時のコールバック
    def __num_button_clicked(self, event):
        clicked_num = event.widget['text']

        if self.display_value.get() == '0' or self.is_op_button_clicked:
            self.display_value.set(clicked_num)
        else:
            self.display_value.set(self.display_value.get() + clicked_num)

        self.is_op_button_clicked = False

    # 演算子ボタンが押された時のコールバック
    def __op_button_clicked(self, event):
        if self.plus_button['state'] != tk.DISABLED:
            self.first_value = self.display_value.get()
            self.is_op_button_clicked = True

            # 何の演算子が押されたかを変数に格納
            self.operator = event.widget['text']
            self.__change_op_button_state(state=tk.DISABLED)
            self.equal_button.config(state=tk.NORMAL)

    # =ボタンが押された時のコールバック
    def __equal_button_clicked(self, event):
        if self.equal_button['state'] != tk.DISABLED:
            self.second_value = self.display_value.get()
            if self.operator == '+':
                result = int(self.first_value) + int(self.second_value)
            elif self.operator == '-':
                result = int(self.first_value) - int(self.second_value)
            elif self.operator == '×':
                result = int(self.first_value) * int(self.second_value)
            elif self.operator == '÷':
                # 0除算していないかの確認
                if self.second_value != '0':
                    result = int(self.first_value) / int(self.second_value)
                else:
                    result = 'Error'
            else:
                result = 'Unknown'

            self.display_value.set(str(result))
            self.equal_button.config(state=tk.DISABLED)

    # クリアーキーが押された時のコールバック
    def __clear_button_clicked(self, event):
        self.display_value.set('0')
        self.first_value = '0'
        self.second_value = '0'
        self.__change_op_button_state(state=tk.NORMAL)
        self.equal_button.config(state=tk.DISABLED)
        self.is_op_button_clicked = False
        self.operator = ''

    # 演算子ボタンの状態を一括で変更する
    def __change_op_button_state(self, state=tk.NORMAL):
        self.plus_button.config(state=state)
        self.sub_button.config(state=state)
        self.multi_button.config(state=state)
        self.div_button.config(state=state)


if __name__ == '__main__':
    my_calculator = Calculator()
    my_calculator.mainloop()