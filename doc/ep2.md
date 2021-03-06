# Tkinter入門
## 5. widgetの配置方法について学ぶ part1
Tkinterに限らず，何かを画面に表示させたい場合は，
- 何を
- どこに

を明示することが必ず求められます．

前章で説明を省略した内容について説明します．

```python
    root_frame.pack(expand=True, fill=tk.BOTH)
```

```pack()```とは，同じ階層に配置されているwidgetを単純に縦，あるいは横に並べるために使う関数です．ここでしていしている引数についての詳しい説明は省きますが，この引数は，
- widgetの見た目を引き伸ばすことを許可する
- 引き伸ばす方向は，X方向とY方向

という意味になります．なので，```root_frame```はウィンドウいっぱいに引き伸ばされて表示されることになります．

```python
    my_label.pack(anchor=tk.N, fill=tk.X)
```

こちらも同じく```pack()```を使って配置方法を指定しています．```root_frame```とは違う引数を指定していますが，こちらは，
- 親のwidgetの上側に固定する
- 引き伸ばすのであれば，X方向にのみ引き伸ばす

という意味となります．なので，```my_label```は```root_frame```の上側にくっついており，なおかつ左右いっぱいに引き伸ばされて表示されていると思います．

## 6. widgetの配置方法について学ぶ part2
```pack()```は，widgetを単純に縦や横に並べるものでした．今回の課題のような，縦横に格子状に並べるには少し都合が悪いです．```grid()```は，widgetをN行M列の形で配置することができます．

```python
    widget.grid(row=1, column=2)
```

この例では，widgetを1行2列目に配置するという指定になります．細かい話をすると少し大変になってしまうので，ここでは，```grid()```はN行M列目に配置することができる関数であるということだけ覚えましょう．

## 7. Buttonの作成
Buttonの作成も，labelやframeと大差ありません．

```python
    my_button = tk.Button(master=XXX, text=XXX)
```

強いて言うのであれば，Buttonだけは背景色を変更することができません．