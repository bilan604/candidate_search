
from selenium_helper import SeleniumHelper

sh = SeleniumHelper()
sh.load_driver()


inp = input("Ready to 1?")
sh.switch_to(1)
inp = input("Ready to 0?")
sh.switch_to(0)

inp = input("Ready to 1?")
sh.switch_to(1)
inp = input("Ready to 0?")
sh.switch_to(0)


"""
import re
import os



def get_pdf_path(self, name):
    path = "/Users/lan/Downloads"
    try:
        os.listdir(path)
    except:
        path = "C:\\Users\\darkg\\Downloads"
        
    # Get full paths of all files in the directory
    full_paths = [os.path.join(path, f) for f in os.listdir(path)]

    # Sort by creation time
    files_sorted_by_ctime = sorted(full_paths, key=os.path.getctime)

    # Just the filenames (without full path), sorted
    filenames_sorted_by_ctime = [os.path.basename(f) for f in files_sorted_by_ctime]

    filename = filenames_sorted_by_ctime[-1]
    if "脉脉招聘" not in filename:
        return None
    if name not in filename:
        return None
    return filename

r = "阮超雄"
print(get_pdf_path(None, r))

"""
