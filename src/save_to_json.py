from abc import ABC, abstractmethod
import json


class Save(ABC):
    @abstractmethod
    def save(self, *args, **kwargs):
        pass


class SaveToJSON(Save):

    def __init__(self, file_path, data_to_save):
        self.data_to_save = data_to_save
        self.file_path = file_path

    def save(self):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            json.dump(self.data_to_save, f)

    def show(self):
        with open(self.file_path, 'r', encoding='utf-8') as f:
            data_to_show = json.load(f)
        return data_to_show