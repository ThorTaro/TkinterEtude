"""
    lesson02 親viewの生成
"""

import tkinter as tk

if __name__ == '__main__':
    my_window = tk.Tk()
    my_window.title('simple root frame')
    my_window.geometry('400x600')

    # 親ViewとなるFrameをウィンドウ内に配置
    root_frame = tk.Frame(master=my_window, bg='black')
    # pack()はwidgetを単純に縦や横に並べるメソッド
    # expand : 描画領域に余白があった場合にその領域を埋めるかどうかのフラグ．
    # fill : viewを広げる際に，縦横どちらに広げるかの設定
    root_frame.pack(expand=True, fill=tk.BOTH)
    my_window.mainloop()