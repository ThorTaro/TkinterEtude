"""
    lesson01 ウィンドウの生成
"""


import tkinter as tk

if __name__ == '__main__':
    # ウィンドウのインスタンスを作成
    root = tk.Tk()
    root.title('simple window')

    # ウィンドウサイズを指定．出現位置も指定可能
    root.geometry('400x600')

    # ウィンドウの実質main処理
    root.mainloop()