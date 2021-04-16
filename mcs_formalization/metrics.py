import pandas as pd
import os
from sklearn import metrics
from path import DATA_DIR_PATH, ROOT_DIR_PATH
import csv
from scipy import stats

annotators = ["1", "2", "3", "4", "5"]


def get_scores(threshold):

    categories = [
        "Values-and-Quantities",
        "Events",
        "Classes-and-Instances",
        "Space",
        "Time",
        "Sets",
        "Physical-Entities",
        "World-States",
    ]

    for category in categories:
        print(category)
        file_path = DATA_DIR_PATH / f"results/{category}_{threshold}.csv"

        if os.path.exists(file_path):
            append_write = "a"
        else:
            append_write = "w"

        with open(file_path, append_write) as file_:

            writer = csv.writer(file_)

            with open(
                DATA_DIR_PATH / f"categorizations/{category}_Binary_{threshold}.csv"
            ) as csv_file:
                df = pd.read_csv(csv_file)

                for init in annotators:

                    y_test = df[init]

                    others = [i for i in annotators if i != init]

                    accuracy_list = ["Accuracy"]
                    balanced_accuracy_list = ["Balanced Accuracy"]
                    pvalue_list = ["P-value"]

                    for other in others:
                        print(init + " vs. " + other)

                        y_pred = df[other]

                        accuracy_list.append(metrics.accuracy_score(y_test, y_pred))
                        balanced_accuracy_list.append(
                            metrics.balanced_accuracy_score(y_test, y_pred)
                        )
                        pvalue_list.append(stats.ttest_ind(y_test, y_pred)[1])

                    header_row = [init] + others
                    writer.writerow(header_row)
                    writer.writerow(accuracy_list)
                    writer.writerow(balanced_accuracy_list)
                    writer.writerow(pvalue_list)
                    writer.writerow([])


if __name__ == "__main__":

    thresholds = [1, 2, 3, 4, 5]

    for threshold in thresholds:
        get_scores(threshold)
