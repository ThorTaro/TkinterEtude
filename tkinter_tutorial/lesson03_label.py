"""
    lesson03 ラベルの作成
"""

import tkinter as tk

if __name__ == '__main__':
    my_window = tk.Tk()
    my_window.title('simple label')
    my_window.geometry('250x300')

    root_frame = tk.Frame(master=my_window, bg='black')
    root_frame.pack(expand=True, fill=tk.BOTH)

    # labelについての参考文献 https://www.tutorialspoint.com/python/tk_label.htm
    # fontについての参考文献 https://memopy.hatenadiary.jp/entry/2017/06/11/112619
    # text alignmentについて，複数行ならjustify，一行ならanchorで設定
    result_label = tk.Label(master=root_frame,
                            bg='gray',
                            anchor=tk.E,
                            text='hello wolrd',
                            font=('Hiragino Sans', '20'),
                            pady='5')
    result_label.pack(anchor=tk.N, fill=tk.X)

    my_window.mainloop()