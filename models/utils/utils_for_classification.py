import os
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay


def load_text_dataset_from_directory(root_dir: str) -> tuple[list, list]:
    X = []
    y = []
    
    labels = os.listdir(root_dir)  # ["label1", "label2", ...]
    counter = 0
    print(f'Found {len(labels)} labels in "{root_dir}"')
    for label in labels:
        category_path = os.path.join(root_dir, label)  # "..\data\classification\test\<label>"
        if os.path.isdir(category_path):
            files = os.listdir(category_path)  # ["xx.txt", "xx.txt", ...]
            for file in files:
                file_path = os.path.join(category_path, file)  # ..\data\classification\test\<label>\xxx.txt
                if os.path.isfile(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        text = f.read()
                        X.append(text)
                        y.append(label)
        print(f' - Label "{label}" {len(files)} files')
        counter += len(files)
    print(f"Total {counter} files")
    print()
    return X, y


def classification_evaluation(y_actual: list, y_pred: list, label: list=["Algebra", "Geometry", "Combinatorics", "Number Theory"]):
    l = np.array(label)
    
    cm = confusion_matrix(y_actual, y_pred, labels=l)
    heatmap = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=l)
    labels = np.unique(y_actual)

    heatmap.plot()
    plt.show()
    
    report  = classification_report(y_actual, y_pred, digits=4, output_dict=True)
    return report
    
