import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from NamedEntityRecognition.MoneyMetadataManipulator import decision_type_money_dict, money_sum_dict, date_money_dict, \
    date_str_money_dict, money_sum_dict_df
from Utils.FeatherUtils import read_feather_local_dataset
from Utils.PathUtils import add_path_to_project_root_str, add_path_to_plot_images_str


def categorical_horizontal_bar(dataset_df: pd.DataFrame, filename: str, fig_dim=(10, 5), title="", x_label="", y_label=""):
    sns.set_theme(style="whitegrid")

    fig, ax = plt.subplots(figsize=fig_dim)
    g = sns.barplot(data=dataset_df, ax=ax, palette="dark", orient='h')
    # ax.despine(left=True)
    g.set(xlabel=x_label, ylabel=y_label)
    g.set_title(title)
    # plt.gca().invert_yaxis()
    png_file = filename + ".png"
    path_to_png = add_path_to_plot_images_str(png_file)
    # plt.show()
    plt.savefig(path_to_png)


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


money_test = read_feather_local_dataset("MetadataWithMoney")
money_dict = date_str_money_dict(money_test)
# print(type(money_dict['submissionTimestamp']))
a = money_sum_dict_df(money_dict)
print(a)
categorical_horizontal_bar(a, "date_money_bar", title="Date - Money Bar Chart", y_label="Date", x_label="Money", fig_dim=(10, 5))
# mytry()

# print(a)
