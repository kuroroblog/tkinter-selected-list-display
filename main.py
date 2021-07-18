import tkinter as tk
from tkinter import filedialog
import csv


class Application(tk.Frame):
    # listbox Widgetに関する情報を格納する変数
    listBox = None
    # listBox Widget周りで利用されるデータに関する変数
    listBoxData = {}

    # listbox Widgetの選択肢が変更された場合に、実行する関数を設定。
    def getListFromSelectIdx(self, event):
        # listbox Widgetの現在選択している選択肢の、index(位置番号)を取得
        selectIdx = self.listBox.curselection()
        # csvの取得を完了しておらず、選択肢が表示されていないことを加味する。
        if len(selectIdx) > 0:
            print(self.listBoxData[selectIdx[0]]['list'])

    # ボタンを選択した場合に実行する関数
    # filedialogのaskopenfilenameのdialogを表示する。
    def getAskOpenFileName(self):
        # 単数ファイルを選択するためのdialogになります。
        # filetypes : csvファイルのみを選択できるようにする。
        # initialdir : filedialogを初回表示するディレクトリの設定。
        # 戻り値 : Openを選択してファイルを開いた場合 : ファイルパス, Cancelを選択した場合 : ''
        # filedialogについて : https://kuroro.blog/python/Um9TeIMMJAZdFqTYKVE6/
        filename = filedialog.askopenfilename(
            filetypes=[('csv files', '*.csv')], initialdir='./')

        if not filename == '':
            # 参考 : https://intellectual-curiosity.tokyo/2020/11/29/python%E3%81%A7csv%E8%AA%AD%E3%81%BF%E6%9B%B8%E3%81%8D%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95%EF%BC%88%E3%83%98%E3%83%83%E3%83%80%E3%83%BC%E3%81%AE%E3%81%BF%E3%80%81%E3%83%98%E3%83%83%E3%83%80%E3%83%BC/
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                # ヘッダーの読み込み
                headerList = reader.__next__()
                # 2回目以降に別のcsvファイルを読み込むことを想定して、リセットする。
                self.listBoxData = {}
                # tk.END : 末尾
                self.listBox.delete(0, tk.END)
                for i in range(0, len(headerList)):
                    self.listBoxData[i] = {}
                    self.listBoxData[i]['name'] = headerList[i]
                    self.listBoxData[i]['list'] = []

                    # listbox Widgetへ選択肢を追加する。
                    # tk.END : 末尾
                    self.listBox.insert(tk.END, headerList[i])

                next(reader)
                for rowList in reader:
                    for j in range(0, len(rowList)):
                        self.listBoxData[j]['list'].append(rowList[j])

    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)

        # Windowを親要素とした場合に、frame Widget(Frame)をどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        frame.pack()

        # frame Widget(Frame)を親要素として、listbox Widgetを作成する。
        # height : 選択肢の表示数を設定
        # Listboxについて : https://kuroro.blog/python/XMWVRR2MEZAe4bpPDDXE/
        self.listBox = tk.Listbox(frame, height=5)

        # frame Widget(Frame)を親要素として、listbox Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        self.listBox.pack()

        # frame Widget(Frame)を親要素として、button Widgetを作成する。
        # text : テキスト情報
        # command : ボタンを選択した場合に実行する関数を設定する。self.getAskOpenFileNameとする。
        # Buttonについて : https://kuroro.blog/python/oFju6EngDtcYtIiMIDf1/
        button = tk.Button(frame, text="選択", command=self.getAskOpenFileName)

        # frame Widget(Frame)を親要素とした場合に、button Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        button.pack()

        # listbox Widgetの選択肢が変更された場合に、実行する関数を設定。
        # 第一引数 : sequence(イベント内容(ボタンを選択する、文字を入力するなど)を設定)
        # 第二引数 : func(第一引数のイベント内容(ボタンを選択する、文字を入力するなど)が実行された場合に、呼ばれる関数を設定)
        # bindについて :  https://kuroro.blog/python/eI5ApJE1wkU7bHsuwk0H/
        self.listBox.bind('<<ListboxSelect>>', self.getListFromSelectIdx)


# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    # Windowを生成する。
    # Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
    root = tk.Tk()

    app = Application(master=root)

    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
