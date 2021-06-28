"""
    lesson05 自作クラスの作成
"""

import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.__set_widget()

    def __set_widget(self):
        self.title('my class')

        # root frame
        self.root_frame = tk.Frame(master=self)
        self.root_frame.grid(row=0,
                            column=0,
                            sticky=tk.NSEW,
                            padx='5',
                            pady='5')

        # 出力結果表示用ラベル
        self.display_label = tk.Label(master=self.root_frame,
                                    anchor=tk.E,
                                    fg='black',
                                    bg='white',
                                    font=('', '20'))
        self.display_label.grid(row=0,column=0,columnspan=4,sticky=tk.EW)

        # 各種ボタン
        self.button9 = tk.Button(master=self.root_frame, text='9', width='2')
        self.button9.grid(row=2, column=2)

        self.button8 = tk.Button(master=self.root_frame, text='8', width='2')
        self.button8.grid(row=2, column=1)

        self.button7 = tk.Button(master=self.root_frame, text='7', width='2')
        self.button7.grid(row=2, column=0)

        self.button6 = tk.Button(master=self.root_frame, text='6', width='2')
        self.button6.grid(row=3, column=2)

        self.button5 = tk.Button(master=self.root_frame, text='5', width='2')
        self.button5.grid(row=3, column=1)

        self.button4 = tk.Button(master=self.root_frame, text='4', width='2')
        self.button4.grid(row=3, column=0)

        self.button3 = tk.Button(master=self.root_frame, text='3', width='2')
        self.button3.grid(row=4, column=2)

        self.button2 = tk.Button(master=self.root_frame, text='2', width='2')
        self.button2.grid(row=4, column=1)

        self.button1 = tk.Button(master=self.root_frame, text='1', width='2')
        self.button1.grid(row=4, column=0)

        self.button0 = tk.Button(master=self.root_frame, text='0')
        self.button0.grid(row=5, column=0, columnspan=2, sticky=tk.EW)

        self.equal_button = tk.Button(master=self.root_frame, text='=', width='2')
        self.equal_button.grid(row=5, column=3)

        self.clear_button = tk.Button(master=self.root_frame, text='C', width='2')
        self.clear_button.grid(row=1, column=0)


if __name__ == '__main__':
    my_calculator = Calculator()
    my_calculator.mainloop()