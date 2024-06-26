import os
from PIL import Image

def collect_images_from_folders(folder_list):
    images = []
    for folder in folder_list:
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                    file_path = os.path.join(root, file)
                    img = Image.open(file_path)
                    images.append(img)
    return images

def save_images_as_tiff(images, output_file):
    if not images:
        print("Нет изображений")
        return

    images[0].save(
        output_file,
        save_all=True,
        append_images=images[1:],
        compression="tiff_deflate"
    )
    print(f"Сохранено {len(images)} изображений в {output_file}")

def main(folder_list, output_file):
    images = collect_images_from_folders(folder_list)
    save_images_as_tiff(images, output_file)

if __name__ == "__main__":
    folders = ['1369_12_Наклейки 3-D_3']
    output_file = "Result.tif"
    main(folders, output_file)
