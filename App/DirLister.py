import os

class DirLister:

    def __init__(self,):
        pass

    def showDir(self, dir: str):
        path = os.path.normpath(dir)
        print(r'--', sep=' ', end='', flush=True)
        if os.path.isdir(path):

            print(path)
            dirs = os.listdir(path)
            for directory in dirs:
                new_path = os.path.join(path, directory)
                print(r'--', sep=' ', end='', flush=True)
                self.showDir(str(new_path))
        elif os.path.isfile(path):
            print(r'-- ', sep=' ', end='', flush=True)
            print(path)
        else:
            raise ValueError("Invalid directory")

dir_lister = DirLister()
dir_lister.showDir(r'd:/PythonProjects/test0/')