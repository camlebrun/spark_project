import os
import glob
import shutil



path = os.getcwd()
all_dirs = glob.glob(path + "/*exp")
target_dir = os.path.join(path, "for_streamlit")

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

for dirname in all_dirs:
    all_files = glob.glob(dirname + "/*.csv")
    for filename in all_files:
        shutil.move(filename, os.path.join(target_dir, os.path.basename(filename)))