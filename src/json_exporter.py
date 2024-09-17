import os
import json

class JsonExporter:
    def __init__(self):
        self.files_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'json files')
        os.makedirs(self.files_dir, exist_ok=True)

    def save_file(self, filename, data):
        file_path = os.path.join(self.files_dir, filename)
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def save_files(self, files_to_save):
        for filename, data in files_to_save.items():
            self.save_file(filename, data)