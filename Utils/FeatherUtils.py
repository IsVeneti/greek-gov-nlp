import pandas as pd

from Utils.PathUtils import add_path_to_local_dataset_str


def save_dict_list_to_feather(dataset_list: list, filename: str):
    print("Writing dataset to feather...")
    filename = filename + ".ftr"
    path = add_path_to_local_dataset_str(filename)
    dataset_list_df = pd.DataFrame(dataset_list)
    dataset_list_df.to_feather(path)


def read_feather_local_dataset(filename):
    filename = filename + ".ftr"
    path = add_path_to_local_dataset_str(filename)
    return pd.read_feather(path)
