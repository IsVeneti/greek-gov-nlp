from pprint import pprint

from NamedEntityRecognition.MoneyMetadataManipulator import date_str_money_dict, money_sum_dict, money_sum_df, \
    decision_type_money_dict, date_money_dict, decision_label_uid
from Plots.BarNER import categorical_horizontal_bar_numbers, categorical_horizontal_bar
from Utils.FeatherUtils import read_feather_local_dataset
import pandas as pd

money_test = read_feather_local_dataset("MetadataWithMoney")

money_dict = date_str_money_dict(money_test,"issueDate")
money_dict2 = date_str_money_dict(money_test)


result_df = money_sum_df(money_dict)
result_dict = money_sum_dict(money_dict)

result_df2 = money_sum_df(money_dict)
result_dict2 = money_sum_dict(money_dict)


# categorical_horizontal_bar(result_df, "issue_date_money_bar", title="Issue Date - Money Bar Chart",
#                            y_label="Issue Date", x_label="Money", fig_dim=(12, 13))
# categorical_horizontal_bar(result_df2, "submission_date_money_bar",
#                                    title="Submission Date - Money Bar Chart", y_label="Submission Date",
#                                    x_label="Money", fig_dim=(12, 8))


# categorical_horizontal_bar_numbers(result_dict, "issue_date_money_num_bar_readable",title="Issue Date - Money Bar Chart",
#                            y_label="Issue Date", x_label="Money", fig_dim=(15, 13))
# categorical_horizontal_bar_numbers(result_dict2, "submission_date_money_num_bar_readable",
#                                    title="Submission Date - Money Bar Chart", y_label="Submission Date",
#                                    x_label="Money", fig_dim=(15, 13))

decision_money_dict = decision_type_money_dict(money_test)
result1_df = money_sum_df(decision_money_dict)
result1_dict = money_sum_dict(decision_money_dict)


# categorical_horizontal_bar(result1_df, "decision_money_num_bar",title="Decision Label - Money Bar Chart",
#                            y_label="Decision Label", x_label="Money", fig_dim=(15, 13))
categorical_horizontal_bar_numbers(result1_dict, "decision_money_num_bar_readable",title="Decision Label - Money Bar Chart",
                           y_label="Decision Label", x_label="Money", fig_dim=(15, 13),data_type="decision")

# pprint(decision_label_uid(money_test))
# result_dict = money_sum_dict(decision_money_dict)
# print(result_df)
