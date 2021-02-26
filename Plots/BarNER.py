import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.ticker import EngFormatter

from NamedEntityRecognition.MoneyMetadataManipulator import decision_type_money_dict, money_sum_dict, date_money_dict, \
    date_str_money_dict, money_sum_df
from Utils.FeatherUtils import read_feather_local_dataset
from Utils.PathUtils import add_path_to_project_root_str, add_path_to_plot_images_str


def categorical_horizontal_bar(dataset_df: pd.DataFrame, filename: str, fig_dim=(10, 5), title="", x_label="",
                               y_label=""):
    sns.set_theme(style="whitegrid")

    fig, ax = plt.subplots(figsize=fig_dim)
    g = sns.barplot(data=dataset_df, ax=ax, palette="dark", orient='h')
    # ax.despine(left=True)
    g.set(xlabel=x_label, ylabel=y_label)
    g.set_title(title)
    # plt.gca().invert_yaxis()
    png_file = filename + ".png"
    path_to_png = add_path_to_plot_images_str(png_file)
    plt.savefig(path_to_png)
    plt.show()


def categorical_horizontal_bar_numbers(dataset, filename: str,fig_dim=(10, 5), title="", x_label="",
                               y_label="",data_type= "date",title_fontsize=35):
    fmt = EngFormatter(places=0)
    data_options = ["date", "decision","label"]
    if data_type not in data_options:
        raise ValueError("Invalid date_type. Expected one of: %s" % data_options)

    fig, ax = plt.subplots(figsize=fig_dim)
    width = 0.75  # the width of the bars
    ind = np.arange(len(dataset.values()))  # the x locations for the groups
    ax.barh(ind, dataset.values(), width, color="#004561")
    plt.rcParams["font.weight"] = "bold"
    ax.set_yticks(ind + width / 2)
    ax.set_yticklabels(dataset.keys(), minor=False)
    plt.grid(False)
    plt.title(title,fontsize=title_fontsize)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    ax.xaxis.set_major_formatter(fmt)
    for i, v in enumerate(dataset.values()):
        if data_type == data_options[0]:
            ax.text(v + 5000000, i, s=fmt.format_eng(v), color='#1e343f',va='center')
        elif data_type == data_options[1]:
            ax.text(v+2000000,i, s=fmt.format_eng(v), color='#1e343f',va='center', fontweight='bold')
            plt.tight_layout()
        elif data_type == data_options[2]:
            ax.text(v + 15, i, s=fmt.format_eng(v), color='#1e343f', va='center', fontweight='bold')
    png_file = filename + ".png"
    path_to_png = add_path_to_plot_images_str(png_file)
    plt.savefig(path_to_png)
    # plt.savefig(path_to_png, format='png', bbox_inches='tight')
    plt.tight_layout()
    plt.show()


def shadowed_horizontal_bar():
    sns.set(style="whitegrid")

    # Initialize the matplotlib figure
    f, ax = plt.subplots(figsize=(6, 15))

    # Load the example car crash dataset
    crashes = sns.load_dataset("car_crashes").sort_values("total", ascending=False)

    # Plot the total crashes
    sns.set_color_codes("pastel")
    sns.barplot(x="total", y="abbrev", data=crashes,
                label="Total", color="b")

    # Plot the crashes where alcohol was involved
    sns.set_color_codes("muted")
    sns.barplot(x="alcohol", y="abbrev", data=crashes,
                label="Alcohol-involved", color="b")

    # Add a legend and informative axis label
    ax.legend(ncol=2, loc="lower right", frameon=True)
    ax.set(xlim=(0, 24), ylabel="",
           xlabel="Automobile collisions per billion miles")
    sns.despine(left=True, bottom=True)
    plt.show()




# mytry()

# print(a)
