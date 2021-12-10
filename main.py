from pathlib import Path
from PIL import Image
import numpy as np

from dataset import Dataset
from gui import GUI


OUTCOME_DIR = "./dataset"
INPUT_DATA_DIR = "./data"


class App(GUI):
    def __init__(self):
        super(App, self).__init__()
        self.outcome = Dataset(Path(OUTCOME_DIR))
        self.dataset_dir = list(Path(INPUT_DATA_DIR).iterdir())

        self.input_data = []
        for subdir in self.dataset_dir:
            self.input_data.append(Dataset(subdir))

        self.cur_dataset_idx = 0
        self.cur_hash_idx = 0
        self.cur_dataset = self.input_data[self.cur_dataset_idx]
        self.hash_list = self.get_hash_from_cur()

        self.img_show(self.get_imgs_from_cur())

    def get_hash_from_cur(self):
        return self.cur_dataset.get_hash()

    def get_imgs_from_cur(self):
        cur_hash = self.hash_list[self.cur_hash_idx]
        return self.cur_dataset.get_imgs(cur_hash)

    def next_file(self):
        self.cur_hash_idx += 1
        if self.cur_hash_idx >= len(self.hash_list):
            self.cur_dataset_idx += 1
            if self.cur_dataset_idx >= len(self.input_data):
                self.cur_dataset_idx = len(self.input_data) - 1
                self.cur_hash_idx = len(self.hash_list) - 1
                raise IndexError

            self.cur_dataset = self.input_data[self.cur_dataset_idx]
            self.hash_list = self.get_hash_from_cur()
            self.cur_hash_idx = 0

    def prev_file(self):
        self.cur_hash_idx -= 1
        if self.cur_hash_idx < 0:
            self.cur_dataset_idx -= 1
            if self.cur_dataset_idx < 0:
                self.cur_hash_idx = 0
                self.cur_dataset_idx = 0
                raise IndexError

            self.cur_dataset = self.input_data[self.cur_dataset_idx]
            self.hash_list = self.get_hash_from_cur()
            self.cur_hash_idx = len(self.hash_list) - 1

    def prev_button_event(self):
        try:
            self.prev_file()
        except IndexError:
            pass
        images = self.get_imgs_from_cur()
        self.img_show(images)

    def next_button_event(self):
        try:
            self.next_file()
        except IndexError:
            pass
        images = self.get_imgs_from_cur()
        self.img_show(images)

    def select_button_event(self):
        hash = self.hash_list[self.cur_hash_idx]
        data = self.cur_dataset.get_pairs(hash)
        self.outcome.append(hash, data)

    def delete_button_event(self):
        hash = self.hash_list[self.cur_hash_idx]
        self.outcome.delete(hash)


if __name__ == "__main__":
    app = App()
    app.root.mainloop()
