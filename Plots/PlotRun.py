from pprint import pprint

from NamedEntityRecognition.MoneyMetadataManipulator import date_str_money_dict, money_sum_dict, money_sum_df, \
    decision_type_money_dict, date_money_dict, decision_label_uid, month_str_money_dict, month_decision_str_money_dict, \
    label_number_dict
from Plots.BarNER import categorical_horizontal_bar_numbers, categorical_horizontal_bar
from Utils.FeatherUtils import read_feather_local_dataset
import pandas as pd

money_test = read_feather_local_dataset("MetadataWithMoney")

money_dict = date_str_money_dict(money_test,"issueDate")
money_dict2 = date_str_money_dict(money_test)
money_dict3 = month_str_money_dict(money_test,"issueDate")


result_df = money_sum_df(money_dict)
result_dict = money_sum_dict(money_dict)

result_df2 = money_sum_df(money_dict2)
result_dict2 = money_sum_dict(money_dict2)

result_dict3 = money_sum_dict(money_dict3)

# categorical_horizontal_bar(result_df, "issue_date_money_bar", title="Issue Date - Money Bar Chart",
#                            y_label="Issue Date", x_label="Money", fig_dim=(12, 13))
# categorical_horizontal_bar(result_df2, "submission_date_money_bar",
#                                    title="Submission Date - Money Bar Chart", y_label="Submission Date",
#                                    x_label="Money", fig_dim=(12, 8))


categorical_horizontal_bar_numbers(result_dict3, "issue_month_money_num_bar_readable",title="Issue Month - Money Bar Chart",
                           y_label="Issue Month", x_label="Money", fig_dim=(25, 13))
categorical_horizontal_bar_numbers(result_dict, "issue_date_money_num_bar_readable",title="Issue Date - Money Bar Chart",
                           y_label="Issue Date", x_label="Money", fig_dim=(25, 13))
categorical_horizontal_bar_numbers(result_dict2, "submission_date_money_num_bar_readable",
                                   title="Submission Date - Money Bar Chart", y_label="Submission Date",
                                   x_label="Money", fig_dim=(25, 17))
#
decision_money_dict = decision_type_money_dict(money_test)
result1_df = money_sum_df(decision_money_dict)
decision_money_dict1 = month_decision_str_money_dict(money_test,"issueDate")

result1_dict = money_sum_dict(decision_money_dict)
result2_dict = money_sum_dict(decision_money_dict1)
# print(type(result2_dict))
#
categorical_horizontal_bar(result1_df, "decision_money_num_bar",title="Decision Label - Money Bar Chart",
                           y_label="Decision Label", x_label="Money", fig_dim=(15, 13))
categorical_horizontal_bar_numbers(result1_dict, "decision_money_num_bar_readable",title="Decision Label - Money Bar Chart",
                           y_label="Decision Label", x_label="Money", fig_dim=(30, 13),data_type="decision")
categorical_horizontal_bar_numbers(result2_dict, "issue_month_decision_money_num_bar_readable",title="Decision Label per Issue Month - Money Bar Chart",
                           y_label="Decision Label per Issue Month", x_label="Money", fig_dim=(30, 17),data_type="decision")
#
# categorical_horizontal_bar_numbers
# pprint(decision_label_uid(money_test))
# result_dict = money_sum_dict(decision_money_dict)
# print(result_df)

label_CNERD = read_feather_local_dataset("LabelCountCNERD")
label_LG = read_feather_local_dataset("LabelCountLG")

label_dict = label_number_dict(label_CNERD,label_LG,"CNERD Model","LG Model")
# print(label_dict)
categorical_horizontal_bar_numbers(label_dict, "entities_sum_bar_readable",title="Model - Entities Number Bar Chart",
                           y_label="Model", x_label="Entities Number",data_type="label",fig_dim=(12,6),title_fontsize=25)

