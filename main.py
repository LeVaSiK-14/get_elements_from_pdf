from scripts.configs import (
    directory_drowing_images_path,
    directory_list_images_path,
    pdf_path
)
from scripts.create_dirs import(
    create_dirs,
    delete_dirs,
)
from scripts.get_drowing import(
    get_drowings,
)
from scripts.get_list_images import(
    get_list_images,
)


def main():
    delete_dirs()
    create_dirs()
    get_list_images(
        pdf_path=pdf_path,
        directory_list_images_path=directory_list_images_path
    )
    get_drowings(
        directory_path=directory_list_images_path,
        directory_drowing_images_path=directory_drowing_images_path
    )


if __name__ == "__main__":
    main()
