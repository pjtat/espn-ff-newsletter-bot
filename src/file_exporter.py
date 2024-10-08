import os
import json

class FileExporter:
    def __init__(self):
        # Set the directory for JSON files
        self.files_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'temp files')
        # Create the directory if it doesn't exist
        os.makedirs(self.files_dir, exist_ok=True)

    def save_txt_file(self, filename, data):
        # Construct the full file path
        file_path = os.path.join(self.files_dir, filename)
        # Open the file and write the JSON data
        with open(file_path, 'w') as f:
            f.write(data)

    def save_json_file(self, filename, data):
        # Construct the full file path
        file_path = os.path.join(self.files_dir, filename)
        # Open the file and write the JSON data
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def save_json_files(self, files_to_save):
        # Iterate through the dictionary of files to save
        for filename, data in files_to_save.items():
            # Save each file using the save_file method
            self.save_file(filename, data)