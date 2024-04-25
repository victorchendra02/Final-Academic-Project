import os


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


def classification_evaluation(y_actual: list, y_pred: list):
    import numpy as np
    import matplotlib.pyplot as plt
    
    from sklearn.metrics import accuracy_score
    from sklearn.metrics import precision_score
    from sklearn.metrics import recall_score
    from sklearn.metrics import f1_score
    from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay

    l = np.array(["Algebra", "Geometry", "Combinatorics", "Number Theory"])
    
    accuracy = accuracy_score(y_actual, y_pred)
    precision = precision_score(y_actual, y_pred, average='weighted')
    recall = recall_score(y_actual, y_pred, average='weighted')
    f1 = f1_score(y_actual, y_pred, average='weighted')
    
    print("Overall model accuracy:")
    print(f"Accuracy  = {accuracy*100:<.2f}%")
    print(f"Precision = {precision*100:<.2f}%")
    print(f"Recall    = {recall*100:<.2f}%")
    print(f"F1-score  = {f1*100:<.2f}%\n")
    
    cm = confusion_matrix(y_actual, y_pred, labels=l)

    heatmap = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=l)
    labels = np.unique(y_actual)

    print("Model accuracy for each label:")
    for label in labels:
        idx = np.where(l == label)[0][0]
        label_accuracy = cm[idx, idx] / np.sum(cm[idx, :])
        print(f"{label:<14s}= {label_accuracy*100:.2f}%")

    heatmap.plot()
    plt.show()
    
    print(classification_report(y_actual, y_pred, digits=4))
    
