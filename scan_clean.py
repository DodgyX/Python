import os
import time
import shutil


def delete_old_files(folder):
    threshold_seconds=604800
    now = time.time()
    files = [os.path.join(folder, filename) for filename in os.listdir(folder)]

    for path in files:
        try:
            if os.path.isfile(path) and (now - os.stat(path).st_mtime) > threshold_seconds:
                os.remove(path)
                print(f"Deleted file: {path}")

            elif os.path.isdir(path):
                if os.path.isdir(path) and (now - os.stat(path).st_mtime) > threshold_seconds:
                    shutil.rmtree(path)
                    print(f"Deleted folder 1: {path}")
                
                elif os.path.isdir(path) and not os.listdir(path):
                    os.rmdir(path)
                    print(f"Deleted folder 2: {path}")

                elif os.path.isdir(path):
                    delete_old_files(path)

        except Exception as e:
            print(f"Error deleting {path}: {e}")


delete_old_files(r'C:\Users\yoann.wiss\Desktop\Nouveau dossier')