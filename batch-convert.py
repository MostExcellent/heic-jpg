import os
import argparse
import pyheif
from PIL import Image

def convert_heic_to_jpg(directory, recursive=False):
    if recursive:
        for root, dirs, files in os.walk(directory):
            for filename in files:
                if filename.lower().endswith(".heic"):
                    convert_file(root, filename)
    else:
        for filename in os.listdir(directory):
            if filename.lower().endswith(".heic"):
                convert_file(directory, filename)

def convert_file(path, filename):
    heic_path = os.path.join(path, filename)
    heif_file = pyheif.read(heic_path)
    
    image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )

    jpg_path = os.path.splitext(heic_path)[0] + '.jpg'
    image.save(jpg_path, "JPEG")

    print(f"Converted {filename} to JPG.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert HEIC files to JPG')
    parser.add_argument('directory', type=str, help='Directory containing HEIC files')
    parser.add_argument('-r', '--recursive', action='store_true', help='Convert files in all subdirectories recursively')
    
    args = parser.parse_args()
    convert_heic_to_jpg(args.directory, args.recursive)