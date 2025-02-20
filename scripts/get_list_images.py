from pdf2image import convert_from_path


def get_list_images(pdf_path: str, directory_list_images_path: str) -> None:
    images = convert_from_path(pdf_path)

    for i, image in enumerate(images):
        image.save(f"{directory_list_images_path}/page_{i+1}.png", "PNG")
