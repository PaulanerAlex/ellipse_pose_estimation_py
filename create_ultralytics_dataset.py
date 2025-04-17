import yaml
import os
import random
import shutil
from bb_picker import bb_picker


def write_to_yaml(data, filename):
    """Writes data to a YAML file with name of dataset"""
    with open(filename, 'w') as file:
        yaml.dump(data, file, default_flow_style=False)

def create_folder_structure(project_name):
    """Creates folder structure for dataset"""
    os.makedirs(f"{project_name}/images/train", exist_ok=True)
    os.makedirs(f"{project_name}/images/val", exist_ok=True)
    os.makedirs(f"{project_name}/labels/train", exist_ok=True)
    os.makedirs(f"{project_name}/labels/val", exist_ok=True)

def create_yaml_structure(project_name):
    """Creates YAML structure for dataset"""
    yml_content = {
        'path': project_name,
        'train': f"{project_name}/images/train",
        'val': f"{project_name}/images/val",
        'nc': 1,
        'names': ['ellipse']
    }
    return yml_content

def annotate_img(image_path, validating=False):
    """
    Annotates image using bb_picker and saves image and txt
    in the corresponding folders
    """

    purpose = "train" if not validating else "val"

    # get bounding box coordinates by user input
    [(x1, y1), (x2, y2), (x3, y3), (x4, y4)] = bb_picker(image_path, True)
    
    shutil.copy(image_path, f"images/{purpose}/" + os.path.basename(image_path))

    # Save the coordinates to a text file
    with open(f"labels/{purpose}/{os.path.basename(image_path).replace('.jpg', '.txt')}", 'w') as f:
        f.write(f"0 {x1} {y1} {x2} {y2} {x3} {y3} {x4} {y4}\n")

def dataset_tool(project_name):
    """
    guide for dataset creation for the user
    """

    print(f"Creating folder structure and YAML file for {project_name} dataset...")
    create_folder_structure(project_name)

    print("how many images should be annotated for training? \n >>> ")

    num_train_images = int(input())

    print("how many images should be annotated for validation? \n >>> ")

    num_val_images = int(input())

    annotated_imgs = []

    for i in range(num_train_images):
        print(f"Annotating training image {i + 1} of {num_train_images}...")
        image_path = random.choice(os.listdir("img"))
        while image_path in annotated_imgs:
            image_path = random.choice(os.listdir("img"))
        annotate_img(image_path)
        annotated_imgs.append(image_path)
        print("continue? \n >>> ")
        cont = input()
        if cont.lower() != 'yes' or cont.lower() != 'y':
            break

    print(f"Annotated {i + 1} out of {num_train_images} training images.")

    for i in range(num_val_images):
        print(f"Annotating validation image {i + 1} of {num_val_images}...")
        image_path = random.choice(os.listdir("img"))
        while image_path in annotated_imgs:
            image_path = random.choice(os.listdir("img"))
        annotate_img(image_path, validating=True)
        annotated_imgs.append(image_path)
        print("continue? \n >>> ")
        cont = input()
        if cont.lower() != 'yes' or cont.lower() != 'y':
            break
    
    print(f"Annotated {i + 1} out of {num_val_images} validation images.")
    
    print("Annotation complete.")


    yml_content = create_yaml_structure(project_name)
    write_to_yaml(yml_content, f"{project_name}.yml")


if __name__ == "__main__":
    project_name = "ellipse_recognition"
    dataset_tool(project_name)
