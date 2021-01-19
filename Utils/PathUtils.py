import os
from pathlib import Path


def get_project_root() -> Path:
    """Take a string with folders and/or file and add it to the local dataset path

             Returns:
                 The full path to the project root
    """
    return Path(__file__).parent.parent


def add_path_to_project_root(paths_list: list) -> Path:
    """Take a list with folders and/or file and add it to the project root path

        Args:
            paths_list: A list with folders and/or file needed to be added to the path, as

        Returns:
            The full path to the project root, with the added path to the folder/file
    """
    full_path = get_project_root()
    for path in paths_list:
        full_path = full_path / path
    return full_path


def add_path_to_project_root_str(path: str) -> Path:
    """Take a string with folders and/or file names and add it to the project root path

        Args:
            path: A string with folders and/or file needed to be added to the path

        Returns:
            The full path to the project root, with the added path to the folder/file
    """
    project_root = get_project_root()
    full_path = project_root / path
    return full_path


def add_path_to_local_dataset_str(path: str) -> Path:
    """Take a string with file name and add it to the local dataset path

        Args:
            path: A string with folders and/or file needed to be added to the path

        Returns:
            The full path to the project root, with the added path to the folder/file
    """
    local_dataset = get_project_root() / "LocalDataset"
    full_path = local_dataset / path
    return full_path


def add_path_to_local_dataset_list(paths_list: list) -> Path:
    """Take a list with folders and/or file names and add it to the local dataset path

        Args:
            paths_list: A list with folders and/or file needed to be added to the path

        Returns:
            The full path to the project root, with the added path to the folder/file
    """
    full_path = get_project_root() / "LocalDataset"
    for path in paths_list:
        full_path = full_path / path
    return full_path


def make_recursive_dir(path: Path):
    if not os.path.exists(path):
        os.makedirs(path)
