from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

from pathlib import Path

SIDE = 140


class GUI:
    def __init__(self):
        self.root = Tk()

        self.root.title("Filtering Images")
        self.root.geometry("800x900")

        self.init_imgfrm()
        self.init_ui()
        self.text_ui()

        self.imgfrm.grid(row=0, column=0, columnspan=5)
        self.vid_title.grid(row=1, column=0, columnspan=5)
        self.frm.grid(row=2, column=0, columnspan=6)
        self.ui_grid()
        self.frm.focus_set()
        self.frm.bind("<Key>", self.key_event)

    def text_ui(self):
        self.vid_title = Label(self.root, text="This is title", width=80)

    def ui_grid(self):
        self.move_ibox1.grid(row=0, column=2)
        self.move_ibox2.grid(row=0, column=4)
        self.prev_button.grid(row=1, column=0)
        Label(self.frm, text="", width=3).grid(row=1, column=1)
        self.select_button.grid(row=1, column=2)
        self.move_button.grid(row=1, column=3)
        self.delete_button.grid(row=1, column=4)
        Label(self.frm, text="", width=3).grid(row=1, column=5)
        self.next_button.grid(row=1, column=6)

    def init_imgfrm(self):
        self.imgfrm = ttk.Frame(
            self.root,
            padding=20,
            width=800,
            height=800,
            )

        self.imgbox = []
        self.img_fill_empty(0)

    def init_ui(self):
        self.frm = ttk.Frame(self.root, padding=10)

        self.move_ibox1 = Text(self.frm, height=2, width=10)
        self.move_ibox2 = Text(self.frm, height=2, width=10)
        self.move_button = ttk.Button(
            self.frm,
            command=self.move_button_event,
            text="Move",
            width=10
            )

        self.prev_button = ttk.Button(
            self.frm,
            command=self.prev_button_event,
            width=10,
            text="Prev",
        )
        self.select_button = ttk.Button(
            self.frm,
            command=self.select_button_event,
            width=10,
            text="Select",
        )
        self.delete_button = ttk.Button(
            self.frm,
            command=self.delete_button_event,
            width=10,
            text="Delete",
        )
        self.next_button = ttk.Button(
            self.frm,
            command=self.next_button_event,
            width=10,
            text="Next",
        )

    def prev_button_event(self):
        raise NotImplementedError

    def next_button_event(self):
        raise NotImplementedError

    def select_button_event(self):
        raise NotImplementedError

    def delete_button_event(self):
        raise NotImplementedError

    def move_button_event(self):
        raise NotImplementedError

    def key_event(self, event):
        raise NotImplementedError

    def img_fill_empty(self, idx):
        empty_img = ImageTk.PhotoImage(
            Image.open("empty.jpg").resize((SIDE, SIDE))
        )

        while idx < 25:
            img_label = Label(
                self.imgfrm,
                width=SIDE,
                height=SIDE,
                image=empty_img
            )
            img_label.grid(
                row=idx//5,
                column=idx % 5,
            )
            self.imgbox.append(img_label)
            idx += 1

    def img_hide(self):
        for label in self.imgbox:
            label.grid_forget()
            label.destroy()

    def img_show(self, images):
        images = [img.resize((SIDE, SIDE)) for img in images]
        tk_imgs = [ImageTk.PhotoImage(img) for img in images]

        idx = -1
        self.img_hide()
        self.imgbox = []
        for idx, img in enumerate(tk_imgs):
            if idx >= 25:
                break
            img_label = Label(
                self.imgfrm,
                image=img,
                width=SIDE,
                height=SIDE,
                )
            img_label.image = img
            img_label.grid(
                row=idx//5,
                column=idx % 5,
            )
            self.imgbox.append(img_label)
        self.img_fill_empty(idx+1)

    def ibox1_set(self, text):
        self.move_ibox1.delete('1.0', END)
        self.move_ibox1.insert(END, text)

    def ibox2_set(self, text):
        self.move_ibox2.delete('1.0', END)
        self.move_ibox2.insert(END, text)

    def set_title(self, text):
        self.vid_title.configure(text=text)


if __name__ == "__main__":
    app = GUI()
    path_list = list(Path("./data/dataset1").glob("*.jpg"))
    imgs = [
        Image.open(path) for path in path_list[0:10]
        ]

    app.img_show(imgs)
    app.root.mainloop()
