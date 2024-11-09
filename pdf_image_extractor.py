import os
import sys
from pypdf import PdfReader
from PIL import Image


def save(image: Image.Image, file_name: str):
    file_type = image.format.lower()
    image.save(f"{file_name}.{file_type}")


if __name__ == "__main__":
    args = sys.argv
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
        print(f"extracting image... {i + 1}/{page_nums}")
        image_nums = len(page.images)

        if image_nums > 1:
            for j, image in enumerate(page.images):
                save(image.image, f"{i}-{j}")
            if image_nums == page_nums:
                break
        else:
            save(page.images[0].image, i)

    print("image extraction completed !")
