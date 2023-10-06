def create_label(text, font=()):
    return ttk.Label(text=text, foreground="white", background="gray10", font=font)


true = True
false = False

import tkinter as tk
from tkinter import ttk, Tk

import config as cfg

import pyautogui as gui
import keyboard as key


class MainApp(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

        self.geometry("500x300")
        self.title("AutoClick")
        self.configure(cfg.win_cfg)
        self.resizable(false, false)

        def start():
            if var.get() == false:

                def a_click():
                    a = 1
                    while a == 1:
                        gui.click(clicks=cfg.click_per_second_num,
                                  interval=cfg.click_per_second_dur)
                        if key.is_pressed('l'):
                            break

                cfg.click_per_second_num = int(click_per_second.get())
                cfg.click_per_second_dur = float(click_per_second_dur.get())
                key.add_hotkey("ctrl+b", lambda: a_click())

            elif var.get() == true:
                def b_click():
                    for i in range(cfg.click_per_second_num):
                        gui.click(clicks=1,
                                  interval=cfg.click_per_second_dur)

                cfg.click_per_second_num = int(click_per_second.get())
                cfg.click_per_second_dur = float(click_per_second_dur.get())
                key.add_hotkey("b", lambda: b_click())

        create_label("клик/сек", ('Arial', 15)).grid(sticky="n", row=3, column=0)

        def change():
            global click_per_second_label_text
            if var.get() == False:
                create_label("  клик/сек   ", ('Arial', 15)).grid(sticky="n", row=3, column=0)
            else:
                create_label("кол-во/клик", ('Arial', 15)).grid(sticky="n", row=3, column=0)

        create_label("SasMo", ('Arial', 25)).grid(column=1, row=1, sticky="e")

        # Нажна кнопка для конфиг окна

        # config_btn = ttk.Button(self,text="Config", command=self.new_window)
        # config_btn.grid(column=2, row=4, pady=(50, 0))

        click_per_second = ttk.Entry(self)
        click_per_second.config(cfg.click_per_second_cfg)
        click_per_second.grid(padx=10, column=0, row=2)

        var = tk.BooleanVar()
        var.set(False)

        anwait = ttk.Radiobutton(self, text="Определённое кол-во кликов", variable=var, value=True, command=change)
        anwait.config(cfg.anwait_cfg)
        anwait.grid(column=2, row=2)

        wait = ttk.Radiobutton(self, text="Беспрерывные клики", variable=var, value=False, command=change)
        wait.config(cfg.wait_cfg)
        wait.grid(column=2, row=3)

        click_per_second_dur = ttk.Entry(self)
        click_per_second_dur.config(cfg.click_per_second_cfg)
        click_per_second_dur.grid(padx=10, column=0, row=4)

        create_label("задержка", ('Arial', 15)).grid(sticky="n", row=5, column=0)

        start_btn = ttk.Button(self, text="Начать", command=start)
        start_btn.config(cfg.start_btn_cfg)
        start_btn.grid(column=2, row=4)

        self.grid_columnconfigure(0, minsize=125)
        self.grid_columnconfigure(1, minsize=125)
        self.grid_columnconfigure(2, minsize=125)

        self.grid_rowconfigure(1, minsize=60)
        self.grid_rowconfigure(2, minsize=60)
        self.grid_rowconfigure(3, minsize=60)
        self.grid_rowconfigure(4, minsize=60)
        self.grid_rowconfigure(5, minsize=60)

    def new_window(self):
        Window().mainloop()


class Window(Tk):
    def __init__(self, *arg, **kwarg):
        super().__init__(*arg, **kwarg)

        self.geometry("500x500")
        label = ttk.Label(self, text='Second Window')
        label.pack()


if __name__ == '__main__':
    MainApp().mainloop()