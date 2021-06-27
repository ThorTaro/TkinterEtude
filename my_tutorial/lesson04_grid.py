"""
    lesson04 gridによる二次元配置
"""

import tkinter as tk

if __name__ == '__main__':
    my_window = tk.Tk()
    my_window.title('simple grid')

    # windowのサイズを固定にすると，gridの制御がとても大変になるため却下
    # widthやheightがピクセルかと思いきや，文字の数に合わせたサイズらしい
    root_frame = tk.Frame(master=my_window)
    root_frame.grid(row=0, column=0, sticky=tk.NSEW, pady='5', padx='5')

    display_label = tk.Label(master=root_frame, bg='white')
    display_label.grid(row=0, column=0, columnspan=4, sticky=tk.EW)

    # buttonの背景色はos依存らしいので変更が困難
    button1 = tk.Button(master=root_frame, text='C', width='2')
    button1.grid(row=1, column=0)

    # button2 = tk.Button(master=root_frame)
    # button2.grid(row=1, column=1)

    # button3 = tk.Button(master=root_frame)
    # button3.grid(row=1, column=2)

    # button4 = tk.Button(master=root_frame)
    # button4.grid(row=1, column=3)

    button5 = tk.Button(master=root_frame, text='7', width='2')
    button5.grid(row=2, column=0)

    button6 = tk.Button(master=root_frame, text='8', width='2')
    button6.grid(row=2, column=1)

    button7 = tk.Button(master=root_frame, text='9', width='2')
    button7.grid(row=2, column=2)

    # button8 = tk.Button(master=root_frame)
    # button8.grid(row=2, column=3)

    button9 = tk.Button(master=root_frame, text='4', width='2')
    button9.grid(row=3, column=0)

    button10 = tk.Button(master=root_frame, text='5', width='2')
    button10.grid(row=3, column=1)

    button11 = tk.Button(master=root_frame, text='6', width='2')
    button11.grid(row=3, column=2)

    # button12 = tk.Button(master=root_frame)
    # button12.grid(row=3, column=3)

    button13 = tk.Button(master=root_frame, text='1', width='2')
    button13.grid(row=4, column=0)

    button14 = tk.Button(master=root_frame, text='2', width='2')
    button14.grid(row=4, column=1)

    button15 = tk.Button(master=root_frame, text='3', width='2')
    button15.grid(row=4, column=2)

    button16 = tk.Button(master=root_frame, text='+', width=2)
    button16.grid(row=4, column=3)

    button17 = tk.Button(master=root_frame, text='0')
    button17.grid(row=5, column=0, columnspan=2, sticky=tk.EW)

    # button18 = tk.Button(master=root_frame)
    # button18.grid(row=5, column=1)

    # button19 = tk.Button(master=root_frame)
    # button19.grid(row=5, column=2)

    button20 = tk.Button(master=root_frame, text='=', width='2')
    button20.grid(row=5, column=3)

    my_window.mainloop()