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
    project_root = get_project_root()
    for path in paths_list:
        project_root = project_root / path
    return project_root


def add_path_to_project_root_str(path: str) -> Path:
    """Take a string with folders and/or file names and add it to the project root path

        Args:
            path: A string with folders and/or file needed to be added to the path

        Returns:
            The full path to the project root, with the added path to the folder/file
    """
    project_root = get_project_root()
    total_path = project_root / path
    return total_path
