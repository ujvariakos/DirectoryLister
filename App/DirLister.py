import os

class DirLister:

    def __init__(self,):
        pass

    def show_dir(self, dir: str):
        # print("show dir ", dir)
        path = os.path.normpath(dir)
        # print(path, os.path.isdir(path))
        # print(r'--', end='')
        if os.path.isdir(path):
            # print(path)
            # print(r'--', end='')
            print(os.path.basename(path))
            dirs = os.listdir(path)
            for directory in dirs:
                new_path = os.path.join(path, directory)
                print(r'--', end='')
                self.show_dir(str(new_path))
        elif os.path.isfile(path):
            print(r'--', end='')
            # print(path)
            print(os.path.basename(path))
        else:
            raise ValueError("Invalid directory")

dir_lister = DirLister()
dir_lister.show_dir(r'd:/PythonProjects/test0/')