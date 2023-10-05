import os, shutil

class FileHelper:

    @classmethod
    def get_filepaths_from_folder(cls, folder_path):
        files_path = []
        for filename in os.listdir(folder_path):
            complete_path = os.path.join(folder_path, filename)
            if os.path.isfile(complete_path):
                files_path.append(filename)
            elif os.path.isdir(complete_path):
                pass

        return files_path


    @classmethod
    def deep_folder_delete(cls, folder_path):
        try:
            shutil.rmtree(folder_path)
        except Exception as e:
            print(f"Can't delete {folder_path}. Reason: {e}")