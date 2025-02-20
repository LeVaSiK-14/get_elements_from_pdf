import os
from scripts.configs import *
import shutil


def create_dirs():
    if not os.path.exists(media):
        os.mkdir(media)

    if not os.path.exists(directory_list_images_path):
        os.mkdir(directory_list_images_path)

    if not os.path.exists(directory_drowing_images_path):
        os.mkdir(directory_drowing_images_path)

    if not os.path.exists(directory_all_elements_contours_path):
        os.mkdir(directory_all_elements_contours_path)


def delete_dirs():
    if os.path.exists(directory_list_images_path):
        shutil.rmtree(directory_list_images_path)

    if os.path.exists(directory_drowing_images_path):
        shutil.rmtree(directory_drowing_images_path)
