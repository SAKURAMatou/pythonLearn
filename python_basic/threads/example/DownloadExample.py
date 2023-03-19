import time
import tkinter as tk
from threading import Thread
from tkinter import messagebox


# import tkinter.messagebox


def download():
    # 模拟下载的操作
    time.sleep(10)
    messagebox.showinfo('提示', '下载完成!')


def show_about():
    messagebox.showinfo('关于', '作者: DML(v1.0)')


def main():
    top = tk.Tk()
    top.title('单线程')
    top.geometry('230x150')
    top.wm_attributes('-topmost', True)

    panel = tk.Frame(top)
    button1 = tk.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tk.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tk.mainloop()


def download_thread():
    # 模拟下载的操作
    dt = Thread(target=download)
    dt.start()


def main_thread():
    top = tk.Tk()
    top.title('多线程')
    top.geometry('230x150')
    top.wm_attributes('-topmost', True)
    panel = tk.Frame(top)
    button1 = tk.Button(panel, text='下载', command=download_thread)
    button1.pack(side='left')
    button2 = tk.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tk.mainloop()
    pass


def main_with_thread():
    class DownloadTaskHandler(Thread):
        def run(self):
            time.sleep(10)
            messagebox.showinfo('提示', '下载完成!')
            button1.config(state=tk.NORMAL)

    def download():
        # 模拟下载的操作
        button1.config(state=tk.DISABLED)
        DownloadTaskHandler(daemon=True).start()

    def show_about():
        messagebox.showinfo('关于', '作者: DML(v1.0)')

    top = tk.Tk()
    top.title('单线程')
    top.geometry('230x150')
    top.wm_attributes('-topmost', 1)

    panel = tk.Frame(top)
    button1 = tk.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tk.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')
    tk.mainloop()


if __name__ == '__main__':
    main_with_thread()
