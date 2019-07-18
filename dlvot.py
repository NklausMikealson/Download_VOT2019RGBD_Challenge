#!/usr/bin/env python3

"""This is a script to download VOT Challenge data sets."""

import os.path
import zipfile
import json

import wget

__version__ = "1.0"


def _make_symlink(target, link):
    if os.path.exists(link):
        print(link, "already exists, so not creating a symlink.")
    else:
        os.symlink(target, link)

def _make_symlink_1(target, link1):
    if os.path.exists(link1):
        print(link1, "already exists, so not creating a symlink.")
    else:
        os.symlink(target, link1)


def _download_images(images_url, directory):
    zip_file = os.path.join(directory, "images.zip")
    url = images_url
    print(url)
    try:
        wget.download(url, zip_file)
        with zipfile.ZipFile(zip_file) as file_:
            file_.extractall(path=directory)
        os.remove(zip_file)
    except:
        pass
    print()

def _download_depth(depth_url, directory):
    zip_file = os.path.join(directory, "depth.zip")
    url = depth_url
    print(url)
    try:
        wget.download(url, zip_file)
        with zipfile.ZipFile(zip_file) as file_:
            file_.extractall(path=directory)
        os.remove(zip_file)
    except:
        pass
    print()


def _download_annotations(annotations, directory):
    zip_file = os.path.join(directory, "annotations.zip")
    url = annotations["url"]
    print(url)
    wget.download(url, zip_file)
    print()
    with zipfile.ZipFile(zip_file) as file_:
        file_.extractall(path=directory)
    os.remove(zip_file)


def _make_directory_structure(sequence_name):
    sequence_directory = os.path.join(ROOT_DIRECTORY,"sequences" , sequence_name)
    images_directory = os.path.join(
        ROOT_DIRECTORY, "sequences", sequence_name, "color"
    )
    depth_directory = os.path.join(
        ROOT_DIRECTORY, "sequences", sequence_name, "depth"
        )
    os.makedirs(sequence_directory, exist_ok=True)
    print(sequence_directory)
    os.makedirs(images_directory, exist_ok=True)
    print(images_directory)
    os.makedirs(depth_directory, exist_ok=True)
    print(depth_directory)
    # os.mkdir(sequence_directory)
    # os.mkdir(images_directory)
    # os.mkdir(depth_directory)
    return {"sequence": sequence_directory, "images": images_directory, "depth":depth_directory}


def _download_sequences(sequences):
    for sequence in sequences:
        directories = _make_directory_structure(sequence["name"])
        print("Downloading", sequence["name"])
        if len(os.listdir(directories["sequence"])) < 15:
            _download_annotations(
                sequence["annotations"], directories["sequence"]
            )
        else:
            print('skip')
        if len(os.listdir(directories["images"])) < 100:
            _download_images(
                sequence["channels"]["color"]["url"], directories["images"]
            )
        else:
            print("skip")
        if len(os.listdir(directories["depth"])) < 10:
            _download_depth(
                sequence["channels"]["depth"]["url"], directories["depth"])
        else:
            print('skip')
        # _make_symlink(
        #     directories["images"],
        #     os.path.join(directories["sequence"], "color")
        #     )
        # _make_symlink(
        #     directories["depth"],
        #     os.path.join(directories["sequence"], "depth")
        # )


def _download_dataset_description():

    # Download json
    s = open(".\description.json")
    response = json.load(s)
    # if response.status_code != 200:
    #     print(
    #         f"Failed to download the data set description for {year}. Here is "
    #         "the response text:"
    #     )
    #     print(response.reason)
    try:
        return response
    except ValueError:
        print("Failed to parse the downloaded JSON content for {year}.")


def _download_dataset():
    description = _download_dataset_description()
    sequences = description["sequences"]
    _download_sequences(sequences)


if __name__ == "__main__":
    ROOT_DIRECTORY = os.path.join(os.getcwd(), "Videos", "vot")
    print(ROOT_DIRECTORY)
    for i in range(100):
        print(i)
        try:
            _download_dataset()
        except:
            pass


