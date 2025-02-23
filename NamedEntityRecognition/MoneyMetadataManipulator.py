import pandas as pd


def date_money_dict(dataset: pd.DataFrame, date_type="submissionTimestamp"):
    date_money_dict = dict()
    date_options = ["issueDate", "submissionTimestamp"]

    if date_type not in date_options:
        raise ValueError("Invalid date_type. Expected one of: %s" % date_options)
    dataset = dataset.sort_values(date_type, ascending=True)
    for i, row in dataset.iterrows():
        date_money_dict.setdefault(row[date_type].date(), []).append(row["money"])

    return date_money_dict


def date_str_money_dict(dataset: pd.DataFrame, date_type="submissionTimestamp"):
    date_money_dict = dict()
    date_options = ["issueDate", "submissionTimestamp"]
    if date_type not in date_options:
        raise ValueError("Invalid date_type. Expected one of: %s" % date_options)

    dataset = dataset.sort_values(date_type, ascending=True)
    for i, row in dataset.iterrows():
        dt_item = row[date_type]
        date_money_dict.setdefault(dt_item.strftime('%d/%m/%Y'), []).append(row["money"])
    return date_money_dict


def month_str_money_dict(dataset: pd.DataFrame, date_type="submissionTimestamp"):
    month_money_dict = dict()
    date_options = ["issueDate", "submissionTimestamp"]
    if date_type not in date_options:
        raise ValueError("Invalid date_type. Expected one of: %s" % date_options)

    dataset = dataset.sort_values(date_type, ascending=True)
    for i, row in dataset.iterrows():
        dt_item = row[date_type]
        month_money_dict.setdefault(dt_item.strftime('%m/%Y'), []).append(row["money"])
    return month_money_dict


def month_decision_str_money_dict(dataset: pd.DataFrame, date_type="submissionTimestamp"):
    month_decision_money_dict = dict()
    date_options = ["issueDate", "submissionTimestamp"]
    if date_type not in date_options:
        raise ValueError("Invalid date_type. Expected one of: %s" % date_options)

    dataset = dataset.sort_values(date_type, ascending=True)
    for i, row in dataset.iterrows():
        dt_item = row[date_type]
        month_decision_money_dict.setdefault(row["decisionTypeLabel"] + "\n" + dt_item.strftime('%m/%Y'), []).append(
            row["money"])
    return month_decision_money_dict


def decision_label_uid(dataset: pd.DataFrame):
    label_uid = dict()
    for i, row in dataset.iterrows():
        label_uid[row["decisionTypeLabel"]] = [row["decisionTypeUid"]]
    return label_uid


def label_number_dict(dataset1: pd.DataFrame, dataset2: pd.DataFrame, dataset1_name: str, dataset2_name: str):
    label_number = dict()
    label_number[dataset1_name] = dataset1["labelCount"].sum()
    label_number[dataset2_name] = dataset2["labelCount"].sum()
    return label_number


# def decision_label_uid(dataset):
#     label_uid = dict()
#     for i, row in dataset.iterrows():
#         label_uid[row["decisionTypeLabel"]] = [row["decisionTypeUid"]]
#     return label_uid


def decision_type_money_dict(dataset: pd.DataFrame):
    decision_type_money = dict()

    for i, row in dataset.iterrows():
        decision_type_money.setdefault(row["decisionTypeLabel"], []).append(row["money"])
    return decision_type_money


def money_sum_dict(data_dict: dict):
    plot_dict = dict()
    for key in data_dict:
        total_money = 0
        for value in data_dict[key]:
            total_money = total_money + value
        plot_dict[key] = total_money
    return plot_dict


def money_sum_df(data_dict: dict):
    plot_dict = dict()
    for key in data_dict:
        total_money = 0
        for value in data_dict[key]:
            total_money = total_money + value
        plot_dict[key] = total_money
    result = pd.DataFrame(plot_dict, index=[0])
    return result


def money_submission_sum_df(data_dict: dict):
    plot_dict = dict()
    for key in data_dict:
        total_money = 0
        for value in data_dict[key]:
            total_money = total_money + value
        plot_dict[key] = total_money
    result = pd.DataFrame(plot_dict, index=[0])

    return result.sort_index(axis=1)
