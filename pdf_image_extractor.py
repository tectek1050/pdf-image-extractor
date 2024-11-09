from logging import getLogger
import os
import sys
from pypdf import PdfReader
from PIL import Image

_logger = getLogger(__name__)

def save(image, page_num):
    if isinstance(image, Image.Image):
        file_type = image.format.lower()
        image.save(f"{page_num}.{file_type}")


if __name__=="__main__":
    args  = sys.argv
    file_name = args[1]

    splited_file_name = file_name.split(".")

    if not len(splited_file_name) == 2:
        raise ValueError("ファイル名が不正です。")
    
    dir_name, file_type = splited_file_name
    output_dir = f"output/{dir_name}"

    if not file_name or not file_type.lower() == "pdf":
        raise ValueError
    
    reader = PdfReader(file_name)

    os.makedirs(output_dir, exist_ok=True)
    os.chdir(output_dir)
    page_nums = len(reader.pages)
    for i, page in enumerate(reader.pages):
        print(f"extracting image... {i+1}/{page_nums}")
        if len(page.images) > 1:
            for j, image in enumerate(page.images):
                save(image.image, f"{i}-{j}")
        else:
            save(page.images[0].image, i)

    print("image extraction completed !")




