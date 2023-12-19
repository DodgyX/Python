import os
import time
import shutil

def delete_old_files(folder, threshold_seconds=604800):
    now = time.time()
    files = [os.path.join(folder, filename) for filename in os.listdir(folder)]

    for path in files:
        try:
            if os.path.isfile(path) and (now - os.stat(path).st_mtime) > threshold_seconds:
                os.remove(path)
                # print(f"Deleted file: {path}")
            elif os.path.isdir(path) and (now - os.stat(path).st_mtime) > threshold_seconds:
                shutil.rmtree(path)
                # print(f"Deleted folder and its contents: {path}")
        except Exception as e:
            print(f"Error deleting {path}: {e}")

delete_old_files(r'C:\Users\yoann.wiss\Desktop\Nouveau dossier\CCE-BRO')
delete_old_files(r'C:\Users\yoann.wiss\Desktop\Nouveau dossier\CID-KYO')
delete_old_files(r'C:\Users\yoann.wiss\Desktop\Nouveau dossier\COURRIER-KYO')
delete_old_files(r'C:\Users\yoann.wiss\Desktop\Nouveau dossier\CREATION-E-BRO')
delete_old_files(r'C:\Users\yoann.wiss\Desktop\Nouveau dossier\CREATION-E-KYO')
delete_old_files(r'C:\Users\yoann.wiss\Desktop\Nouveau dossier\CRMH-KYO')
delete_old_files(r'C:\Users\yoann.wiss\Desktop\Nouveau dossier\DIC-E-KYO')
delete_old_files(r'C:\Users\yoann.wiss\Desktop\Nouveau dossier\DOCPAT-KYO')
delete_old_files(r'C:\Users\yoann.wiss\Desktop\Nouveau dossier\RH-KYO')
delete_old_files(r'C:\Users\yoann.wiss\Desktop\Nouveau dossier\SG-KYO')
delete_old_files(r'C:\Users\yoann.wiss\Desktop\Nouveau dossier\SRA-KYO')
delete_old_files(r'C:\Users\yoann.wiss\Desktop\Nouveau dossier\UDAP67-KYO')