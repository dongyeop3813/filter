from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk

from pathlib import Path

SIDE = 140


class GUI:
    def __init__(self):
        self.root = Tk()

        self.root.title("Filtering Images")
        self.root.geometry("800x850")

        self.frm = ttk.Frame(self.root, padding=10)

        self.imgfrm = ttk.Frame(
            self.root,
            padding=20,
            width=800,
            height=800,
            )

        self.imgbox = []
        self.img_fill_empty(0)

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

        self.imgfrm.grid(row=0, column=0, columnspan=5)
        self.frm.grid(row=1, column=0, columnspan=6)

        self.prev_button.grid(row=1, column=0)
        Label(self.frm, text="", width=3).grid(row=1, column=1)

        self.select_button.grid(row=1, column=2)
        Label(self.frm, text="", width=3).grid(row=1, column=3)

        self.delete_button.grid(row=1, column=4)
        Label(self.frm, text="", width=3).grid(row=1, column=5)

        self.next_button.grid(row=1, column=6)

    def prev_button_event(self):
        raise NotImplementedError

    def next_button_event(self):
        raise NotImplementedError

    def select_button_event(self):
        raise NotImplementedError

    def delete_button_event(self):
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


if __name__ == "__main__":
    app = GUI()
    imgs = [
        Image.open(path) for path in Path("./data/dataset1").glob("*.jpg")
        ]
    app.img_show(imgs)
    app.root.mainloop()
