import os
import shutil

def split_file(input_file, output_folder, chunk_size_mb=25):
    chunk_size_bytes = chunk_size_mb * 1024 * 1024  # Convert MB to bytes
    with open(input_file, 'rb') as f:
        while True:
            chunk = f.read(chunk_size_bytes)
            if not chunk:
                break
            part_number = f"{int(f.tell() / chunk_size_bytes):04d}"
            output_file = os.path.join(output_folder, f"{os.path.basename(input_file)}_{part_number}")
            with open(output_file, 'wb') as part:
                part.write(chunk)

# Example usage:
input_file_path = r'C:\Users\yoann.wiss\Desktop\python\Projets\infinite storage\Tests\VSCodeUserSetup-x64-1.84.2.exe'
output_folder_path = r'C:\Users\yoann.wiss\Desktop\python\Projets\infinite storage\Tests\chunks'
chunk_size_mb = 25

split_file(input_file_path, output_folder_path, chunk_size_mb)